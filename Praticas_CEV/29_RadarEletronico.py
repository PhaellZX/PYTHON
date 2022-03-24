velocidade = float(input('Qual é a sua velocidade atual do carro? '))
if velocidade > 80:
    print(f'\33[0;31mMULTADO! Você excedeu o limite permitido que é de 80km/h\n'
          f'Você deve pagar uma multa de R${(velocidade - 80) * 7:.2f}')
print('\33[0;33mTenha um bom dia! Digija com segurança!')