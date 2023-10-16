import csv
import openai

# Set your OpenAI API key here
openai.api_key = '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'

# Read the CSV file into a list of dictionaries
with open('ml_project1_data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    dataset_list = list(reader)

def get_chatbot_response(user_input, dataset):
    # Process user input to extract keywords (e.g., column names)
    keywords = list(dataset[0].keys())

    # Check if any keyword is present in the user input
    relevant_keywords = [kw for kw in keywords if kw.lower() in user_input.lower()]

    if relevant_keywords:
        # Filter the dataset based on the first relevant keyword (assuming it's an ID)
        filtered_data = [entry for entry in dataset if entry[relevant_keywords[0]] == user_input.split()[-1]]

        if filtered_data:
            # If data is found, retrieve information from the first entry
            response_data = filtered_data[0]
            response_text = ', '.join(f"{kw}: {value}" for kw, value in response_data.items())
            return f"Here is the information: {response_text}"
        else:
            return "No information found for the specified ID."
    else:
        # If no relevant keywords are found, return a default response
        return "I couldn't find information related to your query."

# Example usage
user_query = input("You: ")
while user_query.lower() != 'exit':
    chatbot_response = get_chatbot_response(user_query, dataset_list)
    print("Chatbot:", chatbot_response)
    user_query = input("You: ")
