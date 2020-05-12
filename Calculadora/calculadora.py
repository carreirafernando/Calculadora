def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def divisao(a, b):
    return a / b

def multiplicacao(a, b):
    return a * b

def escolha(valor):
    if resp == 1:
        return soma(a, b)
    elif resp == 2:
        return subtracao(a, b)
    elif resp == 3:
        return divisao(a, b)
    elif resp == 4:
        return multiplicacao(a, b)

print('''Opções
[1] SOMAR
[2] SUBTRAIR
[3] DIVIDIR
[4] MULTIPLICAR''')
while True:
    resp = int(input('Escolha uma opção: '))
    if resp == 1 or resp == 2 or resp == 3 or resp == 4:
        break
    else:
        print('Opção invalida, tente novamente!')
a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
print(escolha(int(resp)))
