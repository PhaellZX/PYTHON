import math
num = float(input('Digite o ângulo que você deseja: '))
print(f'O ângulo de {num} tem o SENO de {math.sin(math.radians(num)):.2f}\n'
      f'O ângulo de {num} tem o COSSENO de {math.cos(math.radians(num)):.2f}\n'
      f'O ângulo de {num} tem o TANGENTE de {math.tan(math.radians(num)):.2f}\n')
