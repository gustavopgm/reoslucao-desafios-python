#Curso de Python 3 - Desafio 08

#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

distancia = float(input("Insira uma distância em metros: "))

mm = distancia * 1000   #Milímetros
cm = distancia * 100    #Centímetros
dm = distancia * 10     #Decímetros
m = distancia           #Metros
dam = distancia / 10    #Decâmetros
hm = distancia / 100    #Hectômetros
km = distancia / 1000   #Kilômetros

print("A distância em metros: {}, tem {}mm, {}cm, {}dm, {}m, {}dam, {}hm, {}km." .format(distancia, mm, cm, dm, m, dam, hm, km))