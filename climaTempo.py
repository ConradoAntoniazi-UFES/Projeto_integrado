#importando bibliotecas necessárias
from bs4 import BeautifulSoup
import requests

cidade = input("Digite uma cidade na grande Vitória:\n")

#Qual cidade será analisada
if cidade.lower() == 'cariacica':
    html = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/723/cariacica-es").content
elif cidade.lower() == 'vitoria':
    html = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/84/vitoria-es").content
elif cidade.lower() == 'vila velha':
    html = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/83/vilavelha-es").content
elif cidade.lower() == 'serra':
    html = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/80/serra-es").content


soup = BeautifulSoup(html, 'html.parser')

#print(soup.prettify())

#pegando a tag html inteira
temperatura_min = soup.find(id="min-temp-1")
temperatura_max = soup.find(id="max-temp-1")

#print(temperatura_max)
#print(temperatura_min)

print(f"\nA temperatura máxima em {cidade} é de {temperatura_max.string}")
print(f"A temperatura máxima em {cidade} é de {temperatura_min.string}")