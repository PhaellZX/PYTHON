from math import hypot
catOposto = float(input('Digite o comprimento do cateto oposto: '))
catAdjacente = float(input('Digite o comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {hypot(catOposto,catAdjacente):.2f}')
