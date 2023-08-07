from time import sleep
from emoji import emojize
print('\033[1;31m—\033[m' * 50)
print('\033[1;33m{:^50}\033[m'.format('{}SNACK`S{}'.format(emojize(':bala:', language='pt'),
                                                           emojize(':bala:', language='pt'))))
print('\033[1;31m—\033[m' * 50)
print('\033[1;33m     Bem Vindo(a), a geladeira de snack´s!'
      '\n     Aqui você pode colocar algumas moedas '
      '\n     e escolher um snack delicioso!\033[m')
print('\033[1;31m{:-^50}\033[m'.format('INSIRA SUAS MOEDAS!'))
um = int(input('\033[1;30;43m[ 1.0  ]\033[m\033[1;33m 1 real - Quantas dessa?: \033[m'))
cinqcents = int(input('\033[1;30;43m[ 0.50 ]\033[m \033[1;33mcinquentas centavos - Quantas dessa?: \033[m'))
cinquenta = cinqcents / 2
vintcents = int(input('\033[1;30;43m[ 0.25 ]\033[m \033[1;33mvinte e cinco centavos - Quantas dessa?: \033[m'))
vinte = vintcents / 4
quantia = um + cinquenta + vinte
print('\033[1;31m-\033[m' * 50)
print(f'\033[1;33mMuito Bem! Seu saldo é de\033[m \033[1;31mR${quantia:.2f}\033[m')
print('\033[1;31m-\033[m' * 50)
sleep(1)
opcoes = [1, 2, 3]
precosneackers = 2.50
precobala = 5.00
precorefri = 7.00
continua = 'S'
print('''\033[1;30;43m                      SNACK´S:                    \033[m
\033[1;30;41m[ 1 ]\033[m \033[1;31m {}SNICKERS - R$2.50\033[m  
\033[1;30;41m[ 2 ]\033[m \033[1;31m{}BALA FINI - R$5.00\033[m  
\033[1;30;41m[ 3 ]\033[m \033[1;31m{}REFRIGERANTE - R$7.00\033[m'''.format(emojize(':chocolate:', language='pt'),
                                                                           emojize(':pirulito:', language='pt'),
                                                                           emojize(':copo_com_canudo:', language='pt')))
escolha = int(input('\033[1;33mQual você vai querer?\033[m'))
sleep(1)
troco = True
print('\033[1;31m-\033[m' * 50)
while True:
    while escolha not in opcoes:
        escolha = int(input('\033[1;33mQual você vai querer?\033[m'))
        sleep(1)
        print('\033[1;31m-\033[m' * 50)
    while continua in 'S':
        if escolha == 1:
            if quantia >= precosneackers:
                troco = quantia - precosneackers
                print('\033[1;33mAqui está seu\033[m \033[1;31m{}SNICKERS!\033[m'.format(emojize(':chocolate:',
                                                                                                 language='pt')))
                if troco >= 0.00:
                    print(f'\033[1;33mSeu troco é de\033[m \033[1;31m{troco:.2f}\033[m\033[1;33m!\033[m')
                    quantia = troco
                    troco = True
                    continua = str(input('\033[1;33mQuer mais snack´s? [S/N]: \033[m')).upper().strip()[0]
                    if continua in 'S':
                        if troco is False:
                            print('\033[1;31m-\033[m' * 50)
                            print('\033[1;33mNão é possível comprar mais snacks!\033[m')
                            print('\033[1;31m-\033[m' * 50)
                            break
                        sleep(1)
                        escolha = int(input('\033[1;33mQual você vai querer?\033[m'))
                        print('\033[1;31m-\033[m' * 50)
                    elif continua in 'N':
                        print('\033[1;31m-\033[m' * 50)
                        print('\033[1;33mVOLTE SEMPRE!\033[m')
                        break
                    else:
                        while continua not in 'SN':
                            continua = str(input('\033[1;33mQuer mais snack´s? [S/N]: \033[m')).upper().strip()[0]

            elif quantia < precosneackers:
                falta = precosneackers - quantia
                print('\033[1;33mVocê não tem saldo o suficiente!\033[m')
                print(f'\033[1;33mVocê precisa de mais:\033[m \033[1;31m{falta:.2f}\033[m \033[1;33mreais.\033[m')
                if troco == 0:
                    troco = False
                continua = str(input('\033[1;33mQuer mais snack´s? [S/N]: \033[m')).upper().strip()[0]
                if continua in 'S':
                    if troco is True:
                        quantia = troco
                    else:
                        print('\033[1;31m-\033[m' * 50)
                        print('\033[1;33mNão é possível comprar mais snacks!\033[m')
                        print('\033[1;31m-\033[m' * 50)
                        break
                    sleep(1)
                    escolha = int(input('\033[1;33mQual você vai querer?\033[m'))
                    print('\033[1;31m-\033[m' * 50)
                elif continua in 'N':
                    print('\033[1;31m-\033[m' * 50)
                    print('\033[1;33mVOLTE SEMPRE!\033[m')
                    break
                    break
                else:
                    while continua not in 'SN':
                        continua = str(input('\033[1;33mQuer mais snack´s? [S/N]: \033[m')).upper().strip()[0]
                print('\033[1;31m-\033[m' * 50)
        elif escolha == 2:
            if quantia >= precobala:
                troco = quantia - precobala
                print('\033[1;33mAqui está sua\033[m \033[1;31m{}BALA FINI!\033[m'.format(emojize(':pirulito:',
                                                                                                  language='pt')))
                if troco >= 0.00:
                    print(f'\033[1;33mSeu troco é de\033[m \033[1;31m{troco:.2f}\033[m\033[1;33m!\033[m')
                    quantia = troco
                    troco = True
                    continua = str(input('\033[1;33mQuer mais snack´s? [S/N]: \033[m')).upper().strip()[0]
                    if continua in 'S':
                        if troco is False:
                            print('\033[1;33mNão é possível comprar mais snacks!\033[m')
                            break
                        sleep(1)
                        escolha = int(input('\033[1;33mQual você vai querer?\033[m'))
                        print('\033[1;31m-\033[m' * 50)
                    elif continua in 'N':
                        print('\033[1;31m-\033[m' * 50)
                        print('\033[1;33mVOLTE SEMPRE!\033[m')
                        break
                    else:
                        while continua not in 'SN':
                            continua = str(input('\033[1;33mQuer mais snack´s? [S/N]: \033[m')).upper().strip()[0]
            elif quantia < precobala:
                falta = precobala - quantia
                print('\033[1;33mVocê não tem saldo o suficiente!\033[m')
                print(f'\033[1;33mVocê precisa de mais:\033[m \033[1;31m{falta:.2f}\033[m \033[1;33mreais.\033[m')
                if troco == 0:
                    troco = False
                continua = str(input('\033[1;33mQuer mais snack´s? [S/N]: \033[m')).upper().strip()[0]
                if continua in 'S':
                    if troco is True:
                        quantia = troco
                    else:
                        print('\033[1;31m-\033[m' * 50)
                        print('\033[1;33mNão é possível comprar mais snacks!\033[m')
                        print('\033[1;31m-\033[m' * 50)
                        break
                    sleep(1)
                    escolha = int(input('\033[1;33mQual você vai querer?\033[m'))
                    print('\033[1;31m-\033[m' * 50)
                elif continua in 'N':
                    print('\033[1;31m-\033[m' * 50)
                    print('\033[1;33mVOLTE SEMPRE!\033[m')
                    break
                else:
                    while continua not in 'SN':
                        continua = str(input('\033[1;33mQuer mais snack´s? [S/N]: \033[m')).upper().strip()[0]
                print('\033[1;31m-\033[m' * 50)
        elif escolha == 3:
            if quantia >= precorefri:
                troco = quantia - precorefri
                print('\033[1;33mAqui está seu\033[m \033[1;31m{}REFRIGERANTE\033[1;31m\033[1;33m!\033[m'
                      .format(emojize(':copo_com_canudo:', language='pt')))
                if troco >= 0.00:
                    print(f'\033[1;33mSeu troco é de\033[m \033[1;31m{troco:.2f}\033[m\033[1;33m!\033[m')
                    quantia = troco
                    troco = True
                    continua = str(input('\033[1;33mQuer mais snack´s? [S/N]: \033[m')).upper().strip()[0]
                    if continua in 'S':
                        if troco is False:
                            print('\033[1;31m-\033[m' * 50)
                            print('\033[1;33mNão é possível comprar mais snacks!\033[m')
                            print('\033[1;31m-\033[m' * 50)
                            break
                        sleep(1)
                        escolha = int(input('\033[1;33mQual você vai querer?\033[m'))
                        print('\033[1;31m-\033[m' * 50)
                    elif continua in 'N':
                        print('\033[1;31m-\033[m' * 50)
                        print('\033[1;33mVOLTE SEMPRE!\033[m')
                        break
                    else:
                        while continua not in 'SN':
                            continua = str(input('\033[1;33mQuer mais snack´s? [S/N]: \033[m')).upper().strip()[0]
            elif quantia < precorefri:
                falta = precorefri - quantia
                print('\033[1;33mVocê não tem saldo o suficiente!\033[m')
                print(f'\033[1;33mVocê precisa de mais:\033[m \033[1;31m{falta:.2f}\033[m \033[1;33mreais.\033[m')
                if troco == 0:
                    troco = False
                continua = str(input('\033[1;33mQuer mais snack´s? [S/N]: \033[m')).upper().strip()[0]
                if continua in 'S':
                    if troco is True:
                        quantia = troco
                    else:
                        print('\033[1;31m-\033[m' * 50)
                        print('\033[1;33mNão é possível comprar mais snacks!\033[m')
                        print('\033[1;31m-\033[m' * 50)
                        break
                    sleep(1)
                    escolha = int(input('\033[1;33mQual você vai querer?\033[m'))
                    print('\033[1;31m-\033[m' * 50)
                elif continua in 'N':
                    print('\033[1;31m-\033[m' * 50)
                    print('\033[1;33mVOLTE SEMPRE!\033[m'.center(50))
                    break
                else:
                    while continua not in 'SN':
                        continua = str(input('\033[1;33mQuer mais snack´s? [S/N]: \033[m')).upper().strip()[0]
                print('\033[1;31m-\033[m' * 50)
