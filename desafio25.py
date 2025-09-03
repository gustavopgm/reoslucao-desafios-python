#Curso de Python 3 - Desafio 25

#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input("Escreva seu nome: ")).strip().upper() #Remove os espaços extras no começo e no final, tranforma toda a string em letras maiúsculas.

print("SILVA" in nome) #Verifica se existe a palavra "SILVA" na string.