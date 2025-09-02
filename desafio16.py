#Curso de Python 3 - Desafio 16

#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira. Ex: Digite um número: 6.127... O número 6.127 tem a parte Inteira 6.

import math #Utilizamos a biblioteca math e seus métodos 

numero1 = float(input("Escreva um número: "))
print("O número digitado foi {} e sua parte inteira é {}.".format(numero1, math.ceil(numero1))) #Arredonda os números pra cima.

numero2 = float(input("Escreva um número: "))
print("O número digitado foi {} e sua parte inteira é {}.".format(numero2, math.floor(numero2))) #Arredonda os números pra baixo.

numero3 = float(input("Escreva um número: "))
print("O número digitado foi {} e sua parte inteira é {}.".format(numero3, math.trunc(numero3))) #Corta os números que estão após a vírgula.

numero4 = float(input("Escreva um número: "))
print("O número digitado foi {} e sua parte inteira é {}.".format(numero4, int(numero4))) #Podemos utilizar  também o tipo de dado primitivo int, que irá converter o valor que está em float (decimal) para int (inteiro).