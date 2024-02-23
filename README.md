# webScrapeCsv
This project aims to create a Python script that allows users to scrape Tally online practical / mock test Series from various websites and store them in a CSV file. 
The script utilizes the 'request' library to send HTTP requests to the specified URL and the 'BeautifulSoup' library to parse the HTML content of the webpage.

Key Features :
1. User Input: The script promts the user to input the URL of the website they wanted to scrape for Tally questions and answers.
2. Scraping Functionality: It contains a function 'scrape_websire(url)' that extracts text from HTML elements such as heading, paragraphs and labels.
3. CSV output: The scraped questions and answers are stored in a CSV file names 'scraped_data.csv'
4. Error Handling: The script includes error handling to handle cases where the URL is invalid or the scraping process fails due to network issues or invalid HTML content.
5. User Feedback: It provides clear feedback to the user, indicating whether the scraping process was successful and where the scraped data is saved.

This project can be useful for the individuals or organizations needing to collect data from various websites for research, analysis or other coaching purposes. 
It provides a convienient and customizable solution for web scraping tasks, allowing users to easily extract and store structures data from online resources.
