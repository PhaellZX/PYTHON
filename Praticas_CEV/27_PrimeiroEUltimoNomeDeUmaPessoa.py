nomeCompleto = str(input('Digite o seu nome completo: ')).strip()
dividir = nomeCompleto.split()
print('Muito prazer em ti conhecer!')
print(f'Seu primeiro nome é {dividir[0]}\n'
      f'Seu último nome é {dividir[len(dividir) - 1]}')