import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Define the URL
url = 'https://quotes.toscrape.com/'

# Step 2: Send a GET request to the website
response = requests.get(url)
if response.status_code != 200:
    print(f"Failed to fetch data: Status {response.status_code}")
    exit()

# Step 3: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 4: Extract specific data (quotes and authors)
quotes_data = []
quotes = soup.find_all('div', class_='quote')

for quote in quotes:
    text = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()
    quotes_data.append([text, author])

# Step 5: Save data into a CSV file
csv_file = 'quotes_dataset.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Quote', 'Author'])
    writer.writerows(quotes_data)

print(f"Scraped and saved {len(quotes_data)} quotes to {csv_file}")
