#Curso de Python 3 - Desafio 20

#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle #Utilizamos a biblioteca random e seus métodos 

a1 = input("Escreva o nome do primeiro aluno: ")
a2 = input("Escreva o nome do segundo aluno: ")
a3 = input("Escreva o nome do terceiro aluno: ")
a4 = input("Escreva o nome do quarto aluno: ")
lista = [a1, a2, a3, a4]

#Reordena os valores da lista de forma aleatória
shuffle(lista)
print("A ordem de apresentação será {}.".format(lista))