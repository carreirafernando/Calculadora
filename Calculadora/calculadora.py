def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def divisao(a, b):
    return a / b

def multiplicacao(a, b):
    return a * b

def potencia(a, b):
    return a ** b

def raiz(a, b):
    return a ** (1 / b)

def porcentagem(a, b):
    return (a / 100) * b

def escolha(valor):
    if o == '+':
        return soma(a, b)
    elif o == '-':
        return subtracao(a, b)
    elif o == '/':
        return divisao(a, b)
    elif o == '*':
        return multiplicacao(a, b)
    elif o == '^':
        return a ** b
    elif o == 'raiz':
        return raiz(a, b)
    elif o == '%':
        return porcentagem(a, b)

while True:
    a = float(input('Digite o primeiro valor: '))
    o = input('Qual a operação: ').strip().lower()
    b = float(input('Digite o segundo valor: '))
    resp = escolha(o)
    print('{}'.format(resp))
    saida = str(input('Quer sair: ')).strip().lower()
    if saida == 'sim':
        break
