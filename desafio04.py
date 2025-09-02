#Curso de Python 3 - Desafio 04

#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele. 

nome = input("Escreva seu nome: ")

print(type(nome)) #Verifica o tipo da classe do objeto armazenado na variável.

#Métodos da classe STRING.

print(nome.isalpha()) #Verifica se todos os caracteres são letras.

print(nome.isnumeric()) #Verifica se todos os caracteres são numéricos.

print(nome.isalnum()) #Verifica se contém apenas letras e números.

print(nome.isdigit()) #Semelhante ao .isnumeric(), mas também verifica números e dígitos especiais.

print(nome.istitle()) #Verifica se está no formato de título (com letras maiúsculas).

print(nome.lower()) #Verifica se está todo em minúsculas.

print(nome.isspace()) #verifica se contém apenas espaços.

print(nome.isupper()) #Verifica se está todo em maiúsculas.