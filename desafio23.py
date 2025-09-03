#Curso de Python 3 - Desafio 23

#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

#Exemplo:
#Digite um número: 1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1

numero = int(input("Digite um número: "))

#Realizamos a divisão real do número, depois realizamos o módulo (resto da divisão) por 10.

#Utilizamos a divisão por 1, 10, 100, 1000 para remover os dígitos a direita. Como se dividíssemos o número por 100, obtendo um resultado decimal, e a partir disso, cortariamos os números após a vírgula.
#Ex: 1234 / 100 = 12.34 Resultado ficaria 12

#Realizamos o módulo por 10, porque o sistema decimal é baseado em grupos de 10. Cada casa (unidade, dezena, centena, milhar..) é um múltiplo de 10. O módulo pega somente o último dígito do número.

#Unidade:                  Dezena:
#1234 // 1 = 1234      1234 // 10 = 123
#1234 % 10 = 4        123 % 10 = 3
#Unidade = 4           Dezena = 3

#Centena:                 Milhar:
#1234 // 100 = 12      1234 // 1000 = 1
#12 % 10 = 2              1 % 10 = 1
#Centena = 2            Milhar = 1

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10 

print("Número: {}".format(numero))
print("Unidade: {}".format(unidade))
print("Dezena: {}".format(dezena))
print("Centena: {}".format(centena))
print("Milhar: {}".format(milhar))