import requests
from bs4 import BeautifulSoup

# Making the GET request
r = requests.get(
    "https://docs.pola.rs/user-guide/getting-started/#with_columns")

# Parsing the HTML
soup = BeautifulSoup(r.content, "html.parser")

s = soup.find('div', class_='highlight')
content = soup.find_all('span')

print(content)
