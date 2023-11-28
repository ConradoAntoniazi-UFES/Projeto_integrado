import requests
from bs4 import BeautifulSoup as bs

# retorna um objeto BeautifulSoup contendo a estura da página endereçada por 'url'
def get_html(url):
    # Envia uma solicitação HTTP GET para a página do perfil
    response = requests.get(url)

    # Quebra o código caso não consiga acessar a página
    if response.status_code != 200:
        print("Não foi possivel acessar a página!")
        exit(1)

    #CASO TENHA CHEGADO ATÉ AQUI, FOI POSSÍVEL ABRIR A PÁGINA

    # Parseia o conteúdo HTML da página (organiza o código da página HTML para ficar mais fácil de ser trabalhada)
    html = bs(response.text, 'html.parser')
    return html

# retorna a url da página contendo as ultimas noticas
def faz_url_noticia(indice):

    # URL da página com o numero do indece informado
    return f"https://www.ufes.br/noticias?page={indice}"

# retorna as noticias em si
def acha_texto_noticia(html):
    #caixa (div) que contém o cardápio do RU daquele dia
    noticia_html = html.find_all("div", class_="view-content")
    print(noticia_html)
    exit(1)
    if not noticia_html:
        print("Problema na extração da noticia.")
        exit(1)
    
    noticia_text = noticia_html.get_text().strip()

    return noticia_text


# retorna o cardápio do dia
def retorna_noticia():
    url = faz_url_noticia('0')

    html = get_html(url)

    cardapio_ru = acha_texto_noticia(html)

    return cardapio_ru


noticia = retorna_noticia()
print(noticia)