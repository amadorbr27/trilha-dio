class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        self.canal += 1

    def diminui_canal(self):
        self.canal -= 1

if __name__ == '__main__':

    televisao = Televisao()
    print('TV ligada?',televisao.ligada)
    televisao.power()
    print('TV ligada?',televisao.ligada)
    televisao.power()
    print('TV ligada?',televisao.ligada)

    print('Canal:', televisao.canal)
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal:', televisao.canal)
    televisao.diminui_canal()
    print('Canal:', televisao.canal)