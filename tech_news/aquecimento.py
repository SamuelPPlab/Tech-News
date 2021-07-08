import requests
import bs4

print("Digite algo para ser buscado:")
termosBuscados = input()

print("Buscando termos " + termosBuscados)

# faz a req ao servidor do google com o termo buscado
res = requests.get("http://google.com/search?q=" + termosBuscados)

# verifica o status apos a requisicao
res.raise_for_status()

# bs4 analisara o html da pagina google retornada
parserSoup = bs4.BeautifulSoup(res.text, features="lxml")

# receber uma lista com os links das primeiras paginas retornados da busca
linksList = parserSoup.select('div#main > div > div > div > a')

# print(linksList[0])

# defino o numero de paginas que quero abrir
numeroDePaginasAbertas = 5

for i in range(numeroDePaginasAbertas):
    print("Abrindo pagina " + linksList[i].get('href')[7:])
