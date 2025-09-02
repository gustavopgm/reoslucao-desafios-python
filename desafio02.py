#Curso de Python 3 - Desafio 02

#Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

nome = input("Escreva seu nome: ")
dia = input("Em que dia você nasceu? ")
mes = input("Em que mês você nasceu? ")
ano = input("Em que ano você nasceu? ")

print("Seu nome é {} e você nasceu no dia {}, de {}, no ano de {}".format(nome, dia, mes, ano))