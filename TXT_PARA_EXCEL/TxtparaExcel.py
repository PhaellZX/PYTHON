import csv
import openpyxl
from time import sleep

input_file = str(input('Digite o nome do arquivo txt(colocando .txt): '))
output_file = f'{input_file[:-4]}.xlsx'

try:
    with open(input_file,'r'):
        wb = openpyxl.Workbook()
        ws = wb.worksheets[0]

        with open(input_file, 'r') as data:
            reader = csv.reader(data, delimiter='\t')
            for row in reader:
                ws.append(row)

        wb.save(output_file)
        print('Arquivo txt convertendo para xls')
        sleep(2)
        print('ARQUIVO CONVERTIDO!!\n''PRESSSIONE QUALQUER BOTÃO...')
        input()
except IOError:
    print('Arquivo não encontrado!')
    input()
