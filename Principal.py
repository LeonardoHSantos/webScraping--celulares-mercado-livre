
import pandas as pd
import requests
from bs4 import BeautifulSoup
headers = {
    'UserAgent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41"
}

tamanho_da_lista = 40
valor_alterna = 50
valor_atual_link = 51

listagem_marca = []
listagem_valor = []
listagem_produtos = []
p = 0


class paginacao:
    def __init__(self, lista_atual):

        self.lista_atual = lista_atual
        self.valor_atual_lik = ''


listagem = []
for valor_lista_inicial in range(tamanho_da_lista):

    url = f'https://celulares.mercadolivre.com.br/_Desde_{valor_atual_link}_NoIndex_True'
    print('Página atual', valor_lista_inicial,  url)
    listagem.append(url)

    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    soma = valor_atual_link + valor_alterna
    valor_atual_link = soma

    descricao = soup.find_all(
        'div', class_='ui-search-result__content-wrapper')
    tamanho_lista = len(descricao)

    print('Itens', tamanho_lista)

    tam = 0
    while tam <= tamanho_da_lista:

        nome = descricao[tam]
        marca = nome.find(
            'h2', class_='ui-search-item__title').get_text()

        preco = descricao[tam]
        valor = preco.find(
            'span', class_='price-tag-amount').get_text()

        listagem_marca.append(marca)
        listagem_valor.append(valor)
        listagem_produtos = (
            {'Marca': listagem_marca, 'Valor': listagem_valor})

        tam = tam + 1

        print(marca, valor)

valor_lista_inicial = paginacao(0)

listagem_produtos = pd.DataFrame(listagem_produtos)
listagem_produtos.to_csv('lista de mercadoria.csv')
listagem_produtos = pd.read_csv('lista de mercadoria.csv')
print(listagem_produtos)
