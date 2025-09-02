#Curso de Python 3 - Desafio 11

#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

larg = float(input("Digite a largura da parede em metros: "))
alt = float(input("Digite a altura da parede em metros: "))
area = larg * alt
latadetinta = area / 2

print("A parede tem {}m de largura e {}m de altura, tendo a dimensão total de {}m, gastando {}l litros de tinta." .format(larg, alt, area, latadetinta))