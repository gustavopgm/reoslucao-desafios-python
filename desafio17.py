#Curso de Python 3 - Desafio 17

#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import sqrt, hypot #Utilizamos a biblioteca math e seus métodos 

oposto = float(input("Determine o valor cateto oposto: "))
adjacente = float(input("Determine o valor do cateto adjacente: "))

hipotenusa1 = (oposto ** 2) + (adjacente ** 2)
print("A hipotenusa vai medir: {:.2f}".
format(sqrt(hipotenusa1))) #Usando sqrt() - Realiza a raiz quadrada do número.

hipotenusa2 = (oposto ** 2 + adjacente ** 2) ** (1/2)
print("A hipotenusa vai medir: {:.2f}".
format(hipotenusa2)) #Elevando a 0.5 - Fórmula de raiz quadrada através da exponenciação.

#Para descobrir o valor da hipotenusa, realizamos a exponenciação do cateto oposto e adjacente a dois, somamos os dois resultados obtidos, depois realizamos a sua raiz quadrada.

#Utilizando o método  hypot()

hipotenusa3 = hypot(oposto, adjacente)
print("A hipotenusa vai medir: {:.2f} ".
format(hipotenusa3)) #Usando hypot() - Realiza o cálculo direto da hipotenusa, sem a necessidade de somar, fazer exponenciação e realizar a raiz quadrada.