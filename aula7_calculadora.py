class Calculadora:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def soma(self):
        return self.a + self.b

if __name__ == '__main__':

    calc = Calculadora(2, 5)
    print(calc.a)
    print(calc.soma())
