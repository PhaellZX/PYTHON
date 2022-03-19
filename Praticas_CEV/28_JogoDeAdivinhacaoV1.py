from random import randint
from time import sleep
print('\33[0;33m-=' * 30)
print('\33[0;34m     Vou penser em número entre 0 e 5. Tente adivinhar... ')
print('\33[0;33m-=' * 30)
computador = randint(0,5)
resposta = int(input('\33[0;37mEm que número eu pensei? '))
print('\33[0;35mPROCESSANDO...')
sleep(2)
if resposta == computador:
    print('\33[0;32mPARABÉNS! Você conseguiu me vencer!')
else:
    print(f'\33[0;31mGANHEI! Eu pensei no número {computador} e não no {resposta}')
