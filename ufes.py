from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.ufes.br/").content

soup = BeautifulSoup(html, 'html.parser')

text = soup.find(id="quicktabs-container-quicktabs_noticias")

print(text.get_text())