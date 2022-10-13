from aula7_televisao import Televisao
from aula7_calculadora import Calculadora
from aula8_palavras import contador_letras

televisao = Televisao()
calc = Calculadora(5, 10)
lista = ['gato', 'cachorro', 'elefante']

print(televisao.ligada)
print(calc.soma())
print(contador_letras(lista))
total_letras = contador_letras(lista)
print('total letras', total_letras)