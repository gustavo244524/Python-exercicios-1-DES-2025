# Crie um programa que receba o peso (kg) e a altura (m) de uma pessoa e calcule o IMC.
# Classifique o resultado de acordo com a faixa:

# Abaixo do peso (< 18.5)
# Peso normal (18.5 a 24.9)
# Sobrepeso (25 a 29.9)
# Obesidade (>= 30)


peso = float(input("Digite o peso (kg): "))  
altura = float(input("Digite a altura (m): ")) 

imc = peso / (altura** 2) 

print(f"IMC: {imc:.2f}")

if imc < 18.5: 
    print("Abaixo do peso.")
elif imc < 25: 
    print("Peso normal") 
else: 
    print("Acima do peso.")
    