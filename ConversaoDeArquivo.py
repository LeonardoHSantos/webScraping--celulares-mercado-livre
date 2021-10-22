import pandas as pd
import Principal as PC


class ExportaListaItens():
    def exporta_lista_itens(self):
        print("Conversão de arquivo\n1 - Converter para CVS \n2 - Converter para EXCEL")
        opcao = int(input('Escolha uma opção para converter o arquivo: '))
        if opcao == 1:
            listagem_itens = pd.DataFrame(listagem_itens)
            listagem_itens.to_csv('lista de celulares.csv')
            listagem_itens = pd.read_csv('lista de celulares.csv')
            print(listagem_itens)
        if opcao == 2:
            listagem_itens = pd.DataFrame(listagem_itens)
            listagem_itens.to_excel('lista de celulares.xlsx')
            listagem_itens = pd.read_excel('lista de celulares.xlsx')
            print(listagem_itens)

        else:
            print('Não foi possível realizar a conversão do arquivo!')
