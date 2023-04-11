""" Calculadora com while """

print('Iniciando calculadora...')
print(' ')


condicao = True

while condicao:
    print('+ = Adição')
    print('- = Subtração')
    print('* = Multiplicação')
    print('/ = Divisão')
    print('0 = Encerrar programa')
    print(' ')
    
    try:
        op = input('Digite a operação desejada: ')
        op_permitido = '/*-+'
        if len(op) < 1 or len(op) > 1:
            print('Digite um operador válido')
            continue
        if op != '':
            if op in op_permitido:
                valor1 = input('Digite o primeiro valor: ')
                valor2 = input('Digite o segundo valor: ')
                print(' ')
                valor1_float = float(valor1)
                valor2_float = float(valor2)

                if op == '+':
                    resultado = valor1_float + valor2_float
                elif op == '-':
                    resultado = valor1_float - valor2_float
                elif op == '*':
                    resultado = valor1_float * valor2_float
                elif op == '-':
                    resultado = valor1_float / valor2_float
                else:
                    print('ERRO!')

                print(' ')
                print(f'TOTAL = {resultado}')
                print(' ')

            elif op == '0':
                condicao = False
                print(' ')
                print('Calculadora encerrada.')

            else:
                print('Operação inválida!')
                print(' ')
                continue

    except:
        print('Por favor digite um valor ou operação válido!')