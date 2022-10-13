
def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

if __name__ == '__main__':
    atualizar_arquivo('Segunda linha.\n')
