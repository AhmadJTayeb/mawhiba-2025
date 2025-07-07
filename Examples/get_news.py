import requests

# Define the URL for the CNN news API
url = "https://saurav.tech/NewsAPI/everything/cnn.json"

# Send a GET request to the API and store the response
response = requests.get(url)

# Parse the JSON data from the response
data = response.json()

# Iterate through the articles in the JSON data
for article in data["articles"]:
    # Print the title of the article
    print("Title: ", article["title"])

    # Print the description of the article
    print("Description: ", article["description"])

    # Print a separator for better readability
    print("---")