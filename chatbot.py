import os
import csv
import openai

# Retrieve your OpenAI API key from the environment variable
openai.api_key = os.environ.get('OPENAI_API_KEY')

# Read the CSV file into a list of dictionaries
with open('ml_project1_data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    dataset_list = list(reader)

# Data dictionary for mapping feature names to descriptions
data_dictionary = {
    "AcceptedCmp1": "1 if the customer accepted the offer in the 1st campaign, 0 otherwise",
    "AcceptedCmp2": "1 if the customer accepted the offer in the 2nd campaign, 0 otherwise",
    "AcceptedCmp3": "1 if the customer accepted the offer in the 3rd campaign, 0 otherwise",
    "AcceptedCmp4": "1 if the customer accepted the offer in the 4th campaign, 0 otherwise",
    "AcceptedCmp5": "1 if the customer accepted the offer in the 5th campaign, 0 otherwise",
    "Response": "1 if the customer accepted the offer in the last campaign, 0 otherwise",
    "Complain": "1 if the customer complained in the last 2 years, 0 otherwise",
    "DtCustomer": "Date of the customer's enrollment with the company",
    "Education": "Customer's level of education",
    "Marital": "Customer's marital status",
    "Kidhome": "Number of small children in the customer's household",
    "Teenhome": "Number of teenagers in the customer's household",
    "Income": "Customer's yearly household income",
    "MntFishProducts": "Amount spent on fish products in the last 2 years",
    "MntMeatProducts": "Amount spent on meat products in the last 2 years",
    "MntFruits": "Amount spent on fruits in the last 2 years",
    "MntSweetProducts": "Amount spent on sweet products in the last 2 years",
    "MntWines": "Amount spent on wines in the last 2 years",
    "MntGoldProds": "Amount spent on gold products in the last 2 years",
    "NumDealsPurchases": "Number of purchases made with a discount",
    "NumCatalogPurchases": "Number of purchases made using the catalog",
    "NumStorePurchases": "Number of purchases made directly in stores",
    "NumWebPurchases": "Number of purchases made through the company's website",
    "NumWebVisitsMonth": "Number of visits to the company's website in the last month",
    "Recency": "Number of days since the last purchase",
}

def get_chatbot_response(user_input, dataset, data_dictionary):
    # Process user input to extract keywords (e.g., column names)
    keywords = list(dataset[0].keys())

    # Check if any keyword is present in the user input
    relevant_keywords = [kw for kw in keywords if kw.lower() in user_input.lower()]

    if relevant_keywords:
        # Extract the ID from the user input
        user_input_words = user_input.split()
        user_id = next((word for word in user_input_words if word.isdigit()), None)

        if user_id:
            # Filter the dataset based on the extracted ID
            filtered_data = [entry for entry in dataset if entry[relevant_keywords[0]] == user_id]

            if filtered_data:
                # If data is found, retrieve information from the first entry
                response_data = filtered_data[0]
                response_text = ', '.join(f"{kw}: {value}" for kw, value in response_data.items())
                return f"Here is the information: {response_text}"
            else:
                return "No information found for the specified ID."
        else:
            return "I couldn't find the ID in your question."
    else:
        # If no relevant keywords are found, return a default response
        return "I couldn't find information related to your query."


# Example usage
user_query = input("You: ")
while user_query.lower() != 'exit':
    chatbot_response = get_chatbot_response(user_query, dataset_list, data_dictionary)
    print("Chatbot:", chatbot_response)
    user_query = input("You: ")
