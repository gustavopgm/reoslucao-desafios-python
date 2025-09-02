#Curso de Python 3 - Desafio 15

#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

diasAlugado = int(input("Dias rodados com o carro: "))
kmPercorridos = float(input("Kilômetros percorridos com o carro: "))

diariaPorAluguel = (diasAlugado * 60)
custoPorKm = (kmPercorridos * 0.15)
gastoTotal = diariaPorAluguel + custoPorKm

print("O carro ficou alugado por {} dias, e percorreu {:.2f}Km. O valor do aluguel diário foi de R${:.2f} e seu custo por km percorridos foi R${:.2f}, resultando no gasto total de R${:.2f}.".
format(diasAlugado, kmPercorridos, diariaPorAluguel, custoPorKm, gastoTotal))