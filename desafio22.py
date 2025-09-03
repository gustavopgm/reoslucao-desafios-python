#Curso de Python 3 - Desafio 22

#Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas. O nome com todas minúsculas. Quantas letras ao todo (sem considerar espaços). Quantas letras tem o primeiro nome.

nome = str(input("Escreva seu nome completo: ")).strip() #Remove os espaços extras do final e do início do código.

print(nome.upper()) #Transforma as letras em maiúsculas. 

print(nome.lower()) #Transforma as letras em minúsculas.

print(len(nome) - nome.count(" ")) #Conta quantidade de caracteres da string menos (-) a quantidade de contagem de espaços em branco (" ").

divisao = nome.split()
print(divisao[0], len(divisao[0])) #Dividimos a string em uma lista, depois exibimos o índice referente ao que precisamos, nesse caso o primeiro índice, ou seja [0], depois contamos a quantidade de letras que o índice escolhido possui.