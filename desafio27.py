#Curso de Python 3 - Desafio 27

#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Exemplo:
#Ana Maria de Souza
#primeiro = Ana
#último = Souza

nome = str(input("Escreva seu nome completo: ")).strip() #Remove os espaços extras no começo e no final.

nome = nome.split() #Transforma as palavras da string em uma lista.

print("Seu primerio nome é: {}".format(nome[0])) 
#Retorna a primeira palavra da lista, utilizamos índice 0 para indicar isso.

print("Seu último nome é: {}".format(nome[-1]))
#Retorna a última palavra da lista, utilizamos índice -1 para indicar isso.