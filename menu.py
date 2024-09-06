from operacao import Operacao

class Menu:
    def __init__(self):
        self.opcao = -1
        self.exer = Operacao()
        self.num1 = 0
        self.num2 = 0

    def mostrarMenu(self):
        print('\n ----  MENU ----\n\n' +
              'Escolha uma das opções abaixo: ' +
              '\n0. Sair' +
              '\n1.Somar' +
              '\n2.Subtrair' +
              '\n3.Dividir' +
              '\n4.Multiplicar' +
              '\n5.Potência' +
              '\n6.Raiz' +
              '\n7.Tabuada'+
              '\n8.Imprimir números de 1 até 10')

    def coletar(self):
        self.num1 = int(input('Informe o primeiro número: '))
        self.num2 = int(input('Informe o segundo número: '))

    def operacao(self):
        while self.opcao != 0:
            self.mostrarMenu()  # Chamando as opções
            self.opcao = int(input('Escolha uma das opções acima: '))
            if self.opcao == 0:
                print('Obrigado!')
            if self.opcao == 1:
                self.coletar()#chamando o input por meio do coletar
                print(f'A soma dos números é: {self.exer.somar(self.num1, self.num2)}')
            elif self.opcao == 2:
                self.coletar()
                print(f'A subtração dos números é: {self.exer.subtrair(self.num1, self.num2)}')
            elif self.opcao == 3:
                self.coletar()
                print(f'A divisão dos números é: {self.exer.dividir(self.num1, self.num2)}')
            elif self.opcao == 4:
                self.coletar()
                print(f'A multiplicação dos números é: {self.exer.multiplicar(self.num1, self.num2)}')
            elif self.opcao == 5:
                self.coletar()
                print(f'\nO resultado da potência é: {self.exer.potencia(self.num1, self.num2)}')
            elif self.opcao == 6:
                self.coletar()
                print(f'\nA raiz de {self.num1} é: {self.exer.raiz(self.num1)}')
                print(f'\nA raiz de {self.num2} é: {self.exer.raiz(self.num2)}')
            elif self.opcao == 7:
                self.coletar()
                print(f'\nA tabuada do {self.num1} é: {self.exer.tabuada(self.num1)}')
                print(f'\nA tabuada do {self.num2} é: {self.exer.tabuada(self.num2)}')
            elif self.opcao == 8:
                print(f'\nOs numeros do 1 até o 10 são: {self.exer.imprimirnumero(self.num)}')





