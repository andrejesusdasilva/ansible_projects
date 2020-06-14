import csv
import textwrap

"""
A responsabilidade da classe file é de ler o arquivo saas.csv e 
retornar um hasg com as informações do arquivo
"""
class CsvFile:
    def __init__(self,cvsfile):
        self.csvfile = cvsfile

    def opencsvfile(self):
        hashClientes = {}
        line_count = 0
        #TODO adicionar validações para o arquivo
        with open(self.csvfile,mode='r') as file:
            linescsv = csv.reader(file, delimiter=',')

            for row in linescsv:
                if line_count == 0:
                    line_count += 1
                else:
                    #print(f'Linhas processadas {line_count}.')
                    hashClientes[row[0]] = {'gateway': row[1],
                                           'oracle': row[2],
                                           'tomcat': row[3]}
                    line_count += 1

            return hashClientes