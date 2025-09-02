#Curso de Python 3 - Desafio 06

#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input("Digite um número: "))

dobro = numero * 2
triplo = numero * 3
raizq = (numero ** (1/2))

print("Seu número é: {}, o seu dobro é {}, o seu triplo é {} e sua raiz quadrada é {: .2f}".format(numero, dobro, triplo, raizq))

#Para obter a raiz quadrada, realizamos a divisão de (1/2) que resultará em 0,5. Depois fazemos a exponenciação (Elevamos) do valor armazenado na variável á 0,5 resultando assim em sua raiz quadrada.