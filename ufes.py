import requests
from bs4 import BeautifulSoup as bs

# Solicita a data para busca do cardápio correspondente àquele dia
data = input("Digite a data no modelo aaaa-mm-dd:")

# URL do site do cardápio do dia informado
url = f"https://ru.ufes.br/cardapio/{data}"

# Envia uma solicitação HTTP GET para a página do perfil
response = requests.get(url)

# Quebra o código caso não consiga acessar a página
if response.status_code != 200:
    print("Não foi possivel acessar a página!")
    exit(1)

#CASO TENHA CHEGADO ATÉ AQUI, FOI POSSÍVEL ABRIR A PÁGINA

# Parseia o conteúdo HTML da página (organiza o código da página HTML para ficar mais fácil de ser trabalhada)
html = bs(response.text, 'html.parser')

#caixa (div) que contém o cardápio do RU daquele dia
cardapio = html.find("div", class_="view-content")

print(cardapio.get_text())