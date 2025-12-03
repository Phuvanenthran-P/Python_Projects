import requests
from bs4 import BeautifulSoup
from db import save_data

URL = "https://quotes.toscrape.com/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")

data = [q.text for q in quotes]

save_data(data)

print("Quotes saved successfully.")
