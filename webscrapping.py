import requests #For giving request to http to get the content
from bs4 import BeautifulSoup #Package for content extraction

# URL of the website to scrape
url = "http://quotes.toscrape.com/"

# Make a GET request to fetch the webpage content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup with the lxml parser
    soup = BeautifulSoup(response.content, "lxml")
    
    # Find all quote blocks on the page
    quotes = soup.find_all("div", class_="quote")
    
    # Loop through each quote and extract details
    for quote in quotes:
        # Extract the quote text
        text = quote.find("span", class_="text").get_text(strip=True)
        # Extract the author name
        author = quote.find("small", class_="author").get_text(strip=True)
        # Extract all tags associated with the quote
        tags = [tag.get_text(strip=True) for tag in quote.find_all("a", class_="tag")]
        
        # Print the scraped details
        print(f"Quote: {text}")
        print(f"Author: {author}")
        print(f"Tags: {tags}")
        print("-" * 40)
else:
    print(f"Failed to retrieve the page. Status Code: {response.status_code}")
