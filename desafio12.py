#Curso de Python 3 - Desafio 12

#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Quanto custa o produto? R$ "))
desconto = preco - (preco * 5 / 100)
print("O produto custa R$ {}, com o desconto de 5% custará R$ {}.".format(preco, desconto))

#Utilizamos a regra de três

#Para calcular o valor do desconto, primeiro dividimos a porcentagem do desconto por 100, depois multiplicamos o resultado dessa divisão pelo valor inicial do produto.

#Depois subtraímos do valor inicial o resultado obtido pelo cálculo do valor do desconto.

#Ou

#Primeiro vamos calcular o valor do desconto:
#Pegamos o preço do produto, multiplicamos pela porcentagem do desconto, nesse caso cinco (5) e dividimos por 100 para obter o valor do desconto.
#Exemplo: 200 * 5 / 100 = 10 (o desconto será de R$10).

#Agora calculamos o preço inicial com o desconto: Subtraímos do valor inicial, o valor do desconto, para obter o novo preço com desconto.
#Exemplo: 200 - 10 = 190 (preço final com desconto).