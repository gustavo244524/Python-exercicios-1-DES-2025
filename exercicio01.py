# Gabriel está acompanhando o desempenho de dois cursos online que lançou: Python Básico e JavaScript Essencial.
# Ele quer saber qual curso teve mais avaliações no último mês.

# Crie um programa que receba o número de avaliações de cada curso e exiba qual teve mais.
# Caso as quantidades sejam iguais, exiba uma mensagem dizendo que houve empate.
curso01 = int(input("digite a quantidade de acessos no curso01:"))
curso02 = int(input("digite a quantidade de acessos no curso02:"))

if curso01 > curso02 :
    print("curso01 tem mais acessos. ")
elif curso02 > curso01 :
    print("curso02 tem mais acessos")
else:
    print("ambos os cursos tiveram a mesma quantidade de acessos.")
