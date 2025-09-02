#Curso de Python 3 - Desafio 19

#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random #Utilizamos a biblioteca random e seus métodos 

a1 = input("Escreva o nome do primeiro aluno: ")
a2 = input("Escreva o nome do segundo aluno: ")
a3 = input("Escreva o nome do terceiro aluno: ")
a4 = input("Escreva o nome do quarto aluno: ")
lista = [a1, a2, a3, a4]

#Escolhe um valor aleatório da lista
escolhido = random.choice(lista)
print(escolhido) 