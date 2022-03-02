metros = float(input('Digite um valor em metros(m): '))
print(f'O valor de {metros}m corresponde a: \n'
      f'{metros / 1000}km\n' # Quilometro
      f'{metros / 100}hm\n'  # Hectômetro
      f'{metros / 10}dam\n'  # Decâmetro
      f'{metros * 10}dm\n'   # Decímetro
      f'{metros * 100}cm\n'  # Centímetro
      f'{metros * 1000}mm')  # Milímetro