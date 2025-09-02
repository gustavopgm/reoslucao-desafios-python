#Curso de Python 3 - Desafio 10

#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$1,00 = R$3,27.

salario = float(input("Digite seu salário: R$ "))
conversao = salario / 3.27

print("Seu salário é R${: .2f}, você pode comprar U${: .2f}." .format(salario, conversao))

#Para convertemos Real em Dólar, dividimos o valor em real pela taxa de câmbio do dólar.