#Curso de Python 3 - Desafio 13

#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Qual o salário do funcionário ? R$ "))

reajuste = salario * 15 / 100
novosalario = salario + reajuste
print("O salário do funcionário é de R${: .2f}, mas com o reajuste de 15%, foi para R${: .2f}.".
format(reajuste, novosalario))

#Para obtermos o valor do reajuste salarial, multiplicamos o salário pela percentagem do aumento salarial e dividimos o resultado obtido por 100. Depois, somamos o valor do salário com o valor do reajuste, obtendo assim, o valor do salário reajustado.

#Utilizamos dentro da chave {: .2f} quando desejarmos exibir apenas duas casas decimais após o "ponto flutuante".