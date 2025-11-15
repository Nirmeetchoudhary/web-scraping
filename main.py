from bs4 import BeautifulSoup  # Import BeautifulSoup
import requests

# Fetch the page content
page_to_scrape = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

quotes = soup.find_all("span", attrs={"class": "text"}) 
authors = soup.find_all("small", attrs={"class": "author"}) 

# let store data in csv
file = open("scraped_quotes.csv","w")
writer = csv.writer(file)

writer.writerow(["Writer","Author"])

# Loop through the quotes and print them with their corresponding author
for quote, author in zip(quotes, authors):  # Pair quotes with authors
    print(f"Quote: {quote.text} - Author: {author.text}")
    writer.writerow([quote.text, author.text])
file.close()
