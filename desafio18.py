#Curso de Python 3 - Desafio 18

#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians #Utilizamos a biblioteca math e seus métodos 

#Calcula o seno
angulo = float(input("Digite o ângulo desejado: "))
seno = sin(radians(angulo))
print("O seno do ângulo {} é {:.2f}.".format(angulo, seno))

#Calcula o cosseno
cosseno = cos(radians(angulo))
print("O cosseno do ângulo {} é {:.2f}.".format(angulo, cosseno))

#Calcula a tangente
tangente = tan(radians(angulo))
print("A tangente do ângulo {} é {:.2f}.".format(angulo, tangente))