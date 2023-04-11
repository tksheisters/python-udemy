"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

try:
    valor = input('Digite um número inteiro (números sem ponto): ')
    valor_int = int(valor) % 2
    if valor_int == 0:
        print(f'{valor} é um número par')
    else:
        print(f'{valor} é um número ímpar')
except:
    print(f'{valor} não é um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

try:
    horas = input('Por favor informe que horas são (0 - 23): ')
    horas_int = int(horas)
    if horas_int >= 0 and horas_int <= 11:
        print(f'Bom dia! São {horas}h')
    elif horas_int >= 12 and horas_int <= 17:
        print(f'Boa tarde! São {horas}h')
    elif horas_int >= 18 and horas_int <= 23:
        print(f'Boa noite! São {horas}h')
    else:
        print('Por favor digite um número inteiro de 0 a 23')
except:
    print('Digite somente números inteiros')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

try:
    primeiro_nome = input('Digite seu primeiro nome: ')
    tamanho_nome = len(primeiro_nome)
    if ' ' not in primeiro_nome and primeiro_nome:
        if tamanho_nome <= 4:
            print('Seu nome é curto')
        elif tamanho_nome == 5 or tamanho_nome == 6:
            print('Seu nome é normal')
        else:
            print('Seu nome é muito grande')
    else:
        print('Por favor digite um nome')
except:
    ...