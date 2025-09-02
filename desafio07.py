#Curso de Python 3 - Desafio 07

#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

print("A soma das notas é: {: .1f}\nE sua média foi: {:.1f}" .format((nota1 + nota2), ((nota1 + nota2) / 2)))

#Para calcular a média, dividimos a soma das notas por dois: (nota1 + nota2) /2. Devido a Hierarquia aritmética, ele resolverá primeiro o que está entre parênteses e depois a divisão.

#Utilizamos dentro da chave {:.1f} quando desejarmos exibir apenas uma casa decimal após o "ponto flutuante".