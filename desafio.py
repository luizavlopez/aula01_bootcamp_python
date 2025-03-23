# Escreva um programa em Python que:
# 1) Solicita ao usuário para digitar seu nome
# 2) Solicita ao usuário para digitar o valor do seu salário mensal
# 3) Solicita ao usuário para digitar o valor da porcentagem do bônus que recebeu
# E retorna:
# Uma mensagem saudando o usuário pelo nome e informando o valor do salario com o bônus recebido

BONUS_2024 = 1000
nome = input("Digite o seu nome: ")
salario = float(input("Digite o seu salário (utilize . como separador decimal): "))
bonus = float(input("Digite a porcentagem do seu bônus (utilize . como separador decimal): "))
valor_bonus = BONUS_2024 + salario * bonus

print(f"Olá, {nome}! O valor do seu bônus é de R$ {valor_bonus}.")