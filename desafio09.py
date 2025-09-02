#Curso de Python 3 - Desafio 09

#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = int(input("Digite um número para ver sua tabuada: "))

print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))

#Quando usamos :2 indicamos que o valor deve ser exibido ocupando pelo menos dois espaços na tela, garantindo que os números fiquem alinhados, mesmo que cheguem a dois dígitos, exemplo:

#Sem utilizar :2
#12 x 1 = 12
#12 x 2 = 24
#12 x 10 = 120

#Utilizando :2            Repare que os números 1 e 2
#12 x  1 = 12                aparecem alinhados com 
#12 x  2 = 24             o número 10
#12 x 10 = 120