#Curso de Python 3 - Desafio 26

#Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra “A”. Em que posição ela aparece a primeira vez. Em que posição ela aparece a última vez.

frase = str(input("Escreva uma frase: ")).strip().upper() #Remove os espaços extras no começo e no final, tranforma toda a string em letras maiúsculas.

print(frase.count("A")) #Conta quantos "A" existem.
print(frase.find("A")) #Retorna o índice do primeiro "A".
print(frase.rfind("A")) #Retorna o índice do último "A" da direita.