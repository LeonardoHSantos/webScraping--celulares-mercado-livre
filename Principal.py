import pandas as pd
import requests
from bs4 import BeautifulSoup
headers = {
    'UserAgent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41"
}


class AlternaPaginas:

    def __init__(self, valor_pagina_incial, tamanho_lista, valor_incremento):
        self.valor_pagina_incial = valor_pagina_incial
        self.tamanho_lista = tamanho_lista
        self.valor_incremento = valor_incremento
        self.url_pagina_celular = f'https://celulares.mercadolivre.com.br/_Desde_{valor_pagina_incial}_NoIndex_True'

        site = requests.get(self.url_pagina_celular, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        descricao = soup.find_all(
            'div', class_='ui-search-result__content-wrapper')

        quantidade_lista = len(descricao)
        self.tamanho_lista = quantidade_lista

    def quantidade_item_por_pagina(self):
        self.quantidade_itens = self.tamanho_lista
        print('Qte itens:', self.quantidade_itens)

    def funcao_loop_celulares(self):
        incremento = self.valor_incremento
        valor_pag_incial = self.valor_pagina_incial
        listagem_paginas = []
        lista_produtos = []
        lista_valor = []
        self.listagem_itens = []

        while True:
            url_padrao = f'https://celulares.mercadolivre.com.br/_Desde_{valor_pag_incial}_NoIndex_True'
            listagem_paginas.append(url_padrao)
            print(url_padrao)

            site = requests.get(url_padrao, headers=headers)
            soup = BeautifulSoup(site.content, 'html.parser')

            descricao = soup.find_all(
                'div', class_='ui-search-result__content-wrapper')
            tamanho_lista = len(descricao)

            if tamanho_lista >= 1:
                proxima_pagina = valor_pag_incial + incremento
                valor_pag_incial = proxima_pagina
                print(valor_pag_incial)
                # inicio do loop produtos

                tam = 0
                while tam <= self.tamanho_lista:
                    try:
                        nome = descricao[tam]
                        marca = nome.find(
                            'h2', class_='ui-search-item__title').get_text().strip()

                        preco = descricao[tam]
                        valor = preco.find(
                            'span', class_='price-tag-amount').get_text().strip()

                        lista_produtos.append(marca)
                        lista_valor.append(valor)
                        self.listagem_itens = (
                            {'Marca': lista_produtos, 'Valor': lista_valor})

                        print(tam, marca, valor)
                        tam = tam + 1

                    except (IndexError, IndentationError):
                        break
            else:
                print('Fim das páginas')
                break

    def informarcoes_pagina(self):
        print(self.tamanho_lista)

    def exporta_lista_itens(self):
        lista_finalizada_celulares = self.listagem_itens
        print("Conversão de arquivo\n1 - Converter para CVS \n2 - Converter para EXCEL")
        opcao = int(input('Escolha uma opção para converter o arquivo: '))
        if opcao == 1:
            lista_finalizada_celulares = pd.DataFrame(
                lista_finalizada_celulares)
            lista_finalizada_celulares.to_csv('lista de celulares.csv')
            lista_finalizada_celulares = pd.read_csv('lista de celulares.csv')
            print(lista_finalizada_celulares)
        if opcao == 2:
            lista_finalizada_celulares = pd.DataFrame(
                lista_finalizada_celulares)
            lista_finalizada_celulares.to_excel('lista de celulares.xlsx')
            lista_finalizada_celulares = pd.read_excel(
                'lista de celulares.xlsx')
            print(lista_finalizada_celulares)
        else:
            print('Não foi possível realizar a conversão do arquivo!')


paginacao = AlternaPaginas(51, 0, 50)
paginacao.informarcoes_pagina()
paginacao.quantidade_item_por_pagina()
paginacao.funcao_loop_celulares()
paginacao.exporta_lista_itens()
