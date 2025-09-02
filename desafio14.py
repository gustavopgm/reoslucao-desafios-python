#Curso de Python 3 - Desafio 14

#Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

c = float(input("Informe a temperatura em C°: "))
fh = 9 / 5 * c + 32

print("A temperatura C° {:.2f}, em F° corresponde a {:.2f}.".format(c, fh))

#Para realizar a conversão de Celsius paraFahrenheit, dividimos 9/5 , multiplicamos oresultado obtido pelo valor em Celsius que estáarmazenado na variável, depois somamos 32. Explicação:

#A escala Celsius define que a água congela em 0 °C e ferve em 100 °C.

#A escala Fahrenheit define que a água congela em 32 °F e ferve em 212 °F.

#Ou seja, 100 °C corresponde a 180 °F (212 - 32).

#A cada 1 °C, aumentam 1,8 °F (ou seja, 9/5).

#Além disso, como 0 °C = 32 °F, precisamos somar 32 no resultado.