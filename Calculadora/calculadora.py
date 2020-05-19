class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def soma(self):
        print(self.a + self.b)
    
    def subtracao(self):
        print(self.a - self.b)
    
    def multiplicacao(self):
        print(self.a * self.b)
    
    def divisao(self):
        print(self.a / self.b)
    
    def potencia(self):
        print(self.a ** self.b)
    
    def raiz(self):
        print(self.a ** (1 / self.b))
    
    def escolha(self, acao):
        if acao == '+':
            saida.soma()
        elif acao == '-':
            saida.subtracao()
        elif acao == '*':
            saida.multiplicacao()
        elif acao == '/':
            saida.divisao()
        elif acao == '**':
            saida.potencia()
        elif acao == 'raiz':
            saida.raiz()


while True:
    numero_1 = input('Digite um número ou digite "sair" para terminar: ')
    if numero_1 == 'sair':
        break
    operacao = str(input('Qual a operação: '))
    numero_2 = float(input('Digite um número: '))
    saida = Calc(float(numero_1), numero_2)
    saida.escolha(operacao)
