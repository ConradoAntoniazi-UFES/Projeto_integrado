#importando bibliotecas necessárias
from bs4 import BeautifulSoup
import requests

cidade = input("Digite uma cidade na grande Vitória:\n")

response = 0

#Qual cidade será analisada
if cidade.lower() == 'cariacica':
    response = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/723/cariacica-es")
elif cidade.lower() == 'vitoria':
    response = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/84/vitoria-es")
elif cidade.lower() == 'vila velha':
    response = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/83/vilavelha-es")
elif cidade.lower() == 'serra':
    response = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/80/serra-es")

if response.status_code != 200:
    print("problema na requisição ao servidor")
    exit(1)

html = response.content

soup = BeautifulSoup(html, 'html.parser')

#print(soup.prettify())

#pegando a tag html inteira
temperatura_min = soup.find(id="min-temp-1")
temperatura_max = soup.find(id="max-temp-1")
#chuva = soup.find("span", class_="_margin-l-5")

#print(temperatura_max)
#print(temperatura_min)

print(f"\nA temperatura máxima em {cidade} é de {temperatura_max.string}")
print(f"A temperatura máxima em {cidade} é de {temperatura_min.string}")
#print(f"chuva: {chuva.string}")