from playsound import playsound
print('\33[33;40mMPY3 - ♪ TOCADOR DE MÚSICA NO PHYTON ♫\33[m')
print('\33[35;40m-=' * 20)
opcao = 0
while True:
    print('\33[34;40m♪ Selecione uma Música:')
    print('1 - Megaman 2 - Dr Wily Stage Remix.')
    print('2 - Megaman X5 - X vs Zero Remix.')
    print('3 - Megaman Zero 3 - Cannonball Remix.')
    print('0 - Sair.\33[m')
    opcao = int(input())
    if opcao == 1:
        print('\33[30;47m♪ ♫ ♪ ♫ ' * 5)
        playsound('MPY3/Megaman2WilyStageRemix.wav')
    elif opcao == 2:
        print('\33[30;47m♪ ♫ ♪ ♫ ' * 5)
        playsound('MPY3/MegamanX5XvsZeroRemix.wav')
    elif opcao == 3:
        print('\33[30;47m♪ ♫ ♪ ♫ ' * 5)
        playsound('MPY3/MegamanZero3CannonBallRemix.wav')
    elif opcao == 0:
        print('\33[32;40mSaindo do MPY3... ')
        break