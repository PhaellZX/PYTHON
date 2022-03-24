distancia = float(input('Digite a distância da sua viagem: '))
if distancia <= 200:
    print(f'Você está preste a começar uma viagem de {distancia}Km\n'
          f'E o preço da sua passagem será de R${distancia * 0.50:.2f}')
else:
    print(f'Você está preste a começar uma viagem de {distancia}Km\n'
          f'E o preço da sua passagem será de R${distancia * 0.45:.2f}')