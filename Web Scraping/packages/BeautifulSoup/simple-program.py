import requests
from bs4 import BeautifulSoup

r = requests.get(
    "https://docs.pola.rs/user-guide/getting-started/#with_columns")

print(r)  # <Responde [200]>

# Parsing HTML
soup = BeautifulSoup(r.content, "html.parser")
# prettify() is a function to print pretty the html structure
print(soup.prettify())
