import requests
from bs4 import BeautifulSoup
import csv


# Function to scrape the website and extract data
def scrape_website(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        response.raise_for_status()
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the elements containing the data you want to scrape
        questions_elements = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'label'])

        # Extract the text from each question div and append it to the list
        scraped_data = [element.get_text(strip=True) for element in questions_elements]
        return scraped_data
    except requests.RequestException as e:
        print("Error: Unable to retrieve data from the website.")
        print(e)
        return None


# Function to save the scraped data to a CSV file
def save_to_csv(data, filename):
    if data:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Write each data element as a row in the CSV file
            for row in data:
                writer.writerow([row])
        print("Questions scraped successfully and saved to scraped_questions.csv")
    else:
        print("No data scraped.")


# URL of the sample website to scrape
url = input("Enter the URL of the website to be scrapped : ")

# Scrape the website and extract the data
scraped_data = scrape_website(url)

save_to_csv(scraped_data, 'scraped_data.csv')