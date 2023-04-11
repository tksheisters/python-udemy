primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite um valor: ')

int_primeiro = int(primeiro_valor)
int_segundo = int(segundo_valor)

if(int_primeiro > int_segundo):
    print(f'O primeiro valor {int_primeiro} é maior que o segundo valor {int_segundo}.')
elif(int_segundo > int_primeiro):
    print(f'O segundo valor {int_segundo} é maior que o primeiro valor {int_primeiro}.')
else:
    print(f'Os dois valores são iguais: {int_primeiro} = {int_segundo}')