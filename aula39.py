"""
Iterando strings com while
"""       
nome = 'Matheus'

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

nova_string = ''
i = 0

while i < tamanho_nome:
    nova_string += nome[i] + '#'
    i += 1
    
print(nova_string)