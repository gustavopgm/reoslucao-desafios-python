#Curso de Python 3 - Desafio 24

#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “SANTO”.

cidade = str(input("Escreva o nome de uma cidade: ")).strip().upper() #Remove os espaços extras no começo e no final, tranforma toda a string em letras maiúsculas.

print("SANTO" in cidade) #Verifica se existe a palavra "SANTO" na string.