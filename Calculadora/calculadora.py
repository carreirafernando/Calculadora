def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def divisao(a, b):
    return a / b

def multiplicacao(a, b):
    return a * b

def escolha(valor):
    if o == '+':
        return soma(a, b)
    elif o == '-':
        return subtracao(a, b)
    elif o == '/':
        return divisao(a, b)
    elif o == '*':
        return multiplicacao(a, b)

while True:
    a = float(input('Digite o primeiro valor: '))
    o = input('Qual a operação: ').strip().lower()
    b = float(input('Digite o segundo valor: '))
    resp = escolha(o)
    print(f'{a} {o} {b} = {resp}')
    saida = str(input('Quer sair: ')).strip().lower()
    if saida == 'sim':
        break
