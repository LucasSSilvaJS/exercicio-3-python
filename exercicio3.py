import os

compras = []
while True:
    produto = input('Digite um produto que deseja comprar: ')
    os.system('cls')
    if produto.strip():
        compras.append(produto)
    else:
        continue
    opcao = input('Digite [s] para sair e [enter] para continuar: ')
    os.system('cls')
    if opcao.lower() == 's':
        break

print('lista de compras:')
for index, compra in enumerate(compras):
    print(f'{index + 1}) {compra}')