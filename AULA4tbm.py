# pontos = 0
# questao = 1
# while questao <= 3:
#     resposta = input(f"Resposta da questão {questao}: ")
#     if questao == 1 and resposta == "b":
#         pontos = pontos + 1
#     if questao == 2 and resposta == "a":
#         pontos = pontos + 1
#     if questao == 3 and resposta == "d":
#         pontos = pontos + 1
#     questao = questao + 1
# print(f"O aluno fez {pontos} ponto(s).")
# ----------------------------------------------------------
# pontos = 0
# questao = 1
# while questao <= 3:
#     resposta = input(f"Resposta da questão {questao}: ")
#     if questao == 1 and resposta == "b":
#         pontos = pontos + 1
#     if questao == 2 and resposta == "a":
#         pontos = pontos + 1
#     elif questao == 3 and resposta == "d":
#         pontos = pontos + 1
#     questao = questao + 1
# print(f"O aluno fez {pontos} ponto(s).")
# ----------------------------------------------------------
# n = 1 #contador
# soma = 0 #acumulador
# while n <= 10:
#     x = float(input(f"Digite o número {n}: "))
#     soma += x
#     n += 1
# print(f"Soma = {soma:.2f}")
# print(f"A Media é =  {(soma/10):.2f}")
# ----------------------------------------------------------
# from time import sleep
# DpInicial = float(input(f"Digite o DpInicial = "))
# TJ = float(input(f"Digite o Valor da Taxa Inicial = "))
# Mês = 0
# while Mês < 24:
#     DpInicial = DpInicial + (DpInicial*(TJ/100))
#     Mês += 1
#     print(f"O Valor a ser Cobrado Sera = {Mês}: R$ {DpInicial:.2f}.")
# print (f"Valor Total Ganho no Final do Mês em R$ = {DpInicial:.2f}.")
# -----------------------------------------------------------
# soma = 0
# while True:
#     num = int(input("Digite um Numero a Somar ou 0 para sair: "))
#     if num == 0:
#         break
#     soma += num
# print(soma)
# -----------------------------------------------------------
