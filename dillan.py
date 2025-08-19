# print("Hello World!")

# # Inteiros
# idade = 20

# # Decimais (float)
# altura = 1.75

# # String
# nome = "Díllan"

# # Booleano
# ativo = True

# Atividade 1

# nome = input ("Qual o seu nome? ")
# idade = input ("Qual a sua idade? ")
# altura = input ("Qual a sua altura? ")

# print (f"Olá, seu nome é {nome}, você tem {idade} anos e {altura} de altura!")

# Atividade 2

# idade = int(input("Qual a sua idade?"))

# if idade >= 18:
#     print ("Você é maior de idade!")
# else:
#     print ("Você é menor de idade!")

# Atividade 3

# idade = int(input("Qual a sua idade?"))

# if idade <= 12:
#     print ("Você é uma criança!")
# elif idade >= 13 and idade <= 17:
#     print ("Você é um adolescente!") 
# elif idade >= 18 and idade <= 59:
#     print ("Você é um adulto!") 
# else:
#     print("Você é um idoso!")

# Atividade 4

# valor = float(input("Qual o valor da sua compra? "))
# categoria = input("Qual o seu plano? ") 

# if categoria.lower() == "vip":
#     valoratualizado = valor * 0.8
#     print (f"Você ganhou 20% de desconto, R${valoratualizado}")

# elif categoria.lower() == "premium":
#     valoratualizado = valor * 0.9
#     print (f"Você ganhou 10% de desconto, R${valoratualizado}")

# elif categoria.lower() == "normal":
#     print (f"Sem desconto, R${valor}")


# Atividade 5

# i = 0
# usuarios = int(input("Quantos úsuarios você quer cadastrar? "))

# for i in range(usuarios):
#     nome = (input("Qual o seu nome? "))
#     nota = int(input("Qual a sua nota? "))
#     if nota >= 7:
#         print (f"Você foi aprovado!")
#     elif nota >= 5 and nota <= 6.9: 
#         print (f"Você foi para a recuperação!")
#     elif nota < 5:
#         print (f"Você foi reprovado!")

# Atividade 6 - chat ajudou

# nomes = []
# notas = []

# alunos = int(input("Quantos alunos você quer cadastrar? "))

# # 1️⃣ Coletando dados
# for i in range(alunos):
#     nome = input("Qual o seu nome? ")
#     nota = float(input("Qual a sua nota? "))
#     nomes.append(nome)
#     notas.append(nota)

# # 2️⃣ Calculando a média depois do loop
# media = sum(notas) / len(notas)
# print(f"A média da turma é {media:.2f}")

# # 3️⃣ Verificando quem está acima ou abaixo da média
# acima_media = []
# abaixo_media = []

# for i in range(alunos):
#     if notas[i] > media:
#         acima_media.append(nomes[i])
#     else:
#         abaixo_media.append(nomes[i])

# print("Alunos acima da média:", acima_media)
# print("Alunos abaixo da média:", abaixo_media)

# Atividade 7

# nums = []
# nums_par = []
# nums_impar = []

# quantidade = int(input("Quantos números você irá digitar? "))

# for i in range(quantidade):
#     nums = int(input("Digite um número "))
#     if nums % 2 == 0:
#         nums_par.append(nums)
#     else:
#         nums_impar.append(nums)

# print (f"Números pares, {sum(nums_par)}")
# print (f"Números impares, {sum(nums_impar)}")

# Atividade 8

# nums = []
# nums_par = []
# nums_impar = []
# soma_par = 0
# soma_impar = 0

# quantidade = int(input("Quantos números você irá digitar? "))

# for i in range(quantidade):
#     nums = int(input("Digite um número "))
#     if nums % 2 == 0:
#         nums_par.append(nums)
#         soma_par += nums
#     else:
#         nums_impar.append(nums)
#         soma_impar += nums

# media_par = sum(nums_par) / len(nums_par)
# media_impar = sum(nums_impar) / len(nums_impar)
    

# print (f"Números pares, {len(nums_par)}, Soma: {soma_par}, Média: {media_par}")
# print (f"Números impares, {len(nums_impar)}, Soma: {soma_impar}, Média: {media_impar}")

# Atividade 9


"""
Faça um programa que:

Pergunte quantos alunos serão cadastrados.

Para cada aluno, pergunte o nome e a nota.

Armazene os nomes e notas em listas separadas.

Para cada nota, determine o conceito do aluno:

Nota >= 9 → Conceito A

Nota >= 7 e < 9 → Conceito B

Nota >= 5 e < 7 → Conceito C

Nota < 5 → Conceito D

No final, mostre:

Quantos alunos tiraram cada conceito.

A média da turma.


"""
# alunos = int(input("Quantos alunos serão cadastrados?"))
# nome = []
# nota = []
# notaadicao = 0
# conceito_a = []
# conceito_b = []
# conceito_c = []
# conceito_d = []

# for i in range(alunos):
#     nome = input("Qual o seu nome?")
#     nota = float(input("Qual a sua nota?"))
#     notaadicao += nota
#     if nota >= 9:
#         conceito_a.append(nota)
#     elif nota >= 7 and nota < 9:
#         conceito_b.append(nota)
#     elif nota >= 5 and nota < 7:
#         conceito_c.append(nota)
#     else:
#         conceito_d.append(nota)

# media = notaadicao / alunos

# print(f"Conceito A - {conceito_a}, Conceito B - {conceito_b}, Conceito C - {conceito_c}, Conceito D - {conceito_d}, a Média é {media}")

# Atividade 10

# usuarios = int(input("Quantos alunos você quer cadastrar?"))
# alunos = []


# for i in range (usuarios):
#     nome = input("Nome do aluno: ")
#     nota = float(input("Nota do aluno: "))
#     alunos.append((nome, nota))

# print (alunos)
# alunos_ordenados = (sorted(alunos, key=lambda aluno: aluno[1], reverse=True))
# print (alunos_ordenados)
# print (f"Maior nota: {alunos_ordenados[0]}, Menor nota: {alunos_ordenados[-1]}")

# Atividade 11

# usuarios = int(input("Quantos alunos você quer cadastrar? "))
# alunos = []
# notas = 0
# alunos_acima = []
# alunos_abaixo = []

# for i in range (usuarios):
#     nome = input("Nome do aluno: ")
#     nota = float(input("Nota do aluno: "))
#     notas += nota
#     alunos.append((nome, nota))
    
# media = notas / usuarios

# for i in range (len(alunos)):
#     if alunos[i][1] >= 7:
#         alunos_acima.append(f"{alunos[i][0]}, {alunos[i][1]}")
#     else:
#         alunos_abaixo.append(f"{alunos[i][0]}, {alunos[i][1]}")
        
# print (media)
# print (f"Alunos acima: {alunos_acima}")
# print (f"Alunos abaixo: {alunos_abaixo}")

#Atividade 12

# usuarios = int(input("Quantos alunos você quer cadastrar? "))
# alunos = []
# notas = 0
# alunos_acima = []
# alunos_abaixo = []

# for i in range (usuarios):
#     nome = input("Nome do aluno: ")
#     nota = float(input("Nota do aluno: "))
#     notas += nota
#     alunos.append((nome, nota))
    
# media = notas / usuarios

# for i in range (len(alunos)):
#     if alunos[i][1] >= 7:
#         alunos_acima.append(f"{alunos[i][0]}, {alunos[i][1]}")
#     else:
#         alunos_abaixo.append(f"{alunos[i][0]}, {alunos[i][1]}")
        
# print ("Média", media)

# print (f"Alunos acima: {alunos_acima}")
# print (f"Alunos abaixo: {alunos_abaixo}")

# alunos_ordenados = (sorted(alunos, key=lambda aluno: aluno[1], reverse=True))
# print ("Alunos em ordem decrescente", alunos_ordenados)

# print (f"Maior nota: {alunos_ordenados[0]}")
# print (f"Menor nota: {alunos_ordenados[-1]}")

# percentual_aprovados = (len(alunos_acima) / len(alunos)) * 100
# print ('Percentual aprovados: ', percentual_aprovados)

# percentual_reprovados = (len(alunos_abaixo) / len(alunos)) * 100
# print ('Percentual reprovados: ', percentual_reprovados)

#Atividade 14

# usuarios = int(input("Quantos alunos você quer cadastrar? "))
# alunos = []
# notas = 0
# alunos_acima = []
# alunos_abaixo = []
# conceito_a = []
# conceito_b = []
# conceito_c = []
# conceito_d = []

# for i in range (usuarios):
#     nome = input("Nome do aluno: ")
#     nota = float(input("Nota do aluno: "))
#     notas += nota
#     alunos.append((nome, nota))
    
# media = notas / usuarios

# for i in range (len(alunos)):
#     if alunos[i][1] >= 7:
#         alunos_acima.append(f"{alunos[i][0]}, {alunos[i][1]}")
#     else:
#         alunos_abaixo.append(f"{alunos[i][0]}, {alunos[i][1]}")
        

# for i in range(usuarios):
#     if alunos[i][1] >= 9:
#         conceito_a.append(f"{alunos[i][0]}, {alunos[i][1]}")
#     elif alunos[i][1] >= 7 and alunos[i][1] < 9:
#         conceito_b.append(f"{alunos[i][0]}, {alunos[i][1]}")
#     elif alunos[i][1] >= 5 and alunos[i][1] < 7:
#         conceito_c.append(f"{alunos[i][0]}, {alunos[i][1]}")
#     else:
#         conceito_d.append(f"{alunos[i][0]}, {alunos[i][1]}")

# print ("Média", media)

# print (f"Alunos acima: {alunos_acima}")
# print (f"Alunos abaixo: {alunos_abaixo}")

# alunos_ordenados = (sorted(alunos, key=lambda aluno: aluno[1], reverse=True))
# print ("Alunos em ordem decrescente", alunos_ordenados)

# print (f"Maior nota: {alunos_ordenados[0]}")
# print (f"Menor nota: {alunos_ordenados[-1]}")

# percentual_aprovados = (len(alunos_acima) / len(alunos)) * 100
# print ('Percentual aprovados: ', percentual_aprovados)

# percentual_reprovados = (len(alunos_abaixo) / len(alunos)) * 100
# print ('Percentual reprovados: ', percentual_reprovados)

# print (f'Conceito A = {conceito_a}')
# print (f'Conceito B = {conceito_b}')
# print (f'Conceito C = {conceito_c}')
# print (f'Conceito D = {conceito_d}')

# print (f"Quantidade - Conceito A = {len(conceito_a)}")
# print (f"Quantidade - Conceito B = {len(conceito_b)}")
# print (f"Quantidade - Conceito C = {len(conceito_c)}")
# print (f"Quantidade - Conceito D = {len(conceito_d)}")

#Atividade 15

# import statistics as st

# usuarios = int(input("Quantos alunos você quer cadastrar? "))
# alunos = []

# for i in range(usuarios):
#     nome = input("Qual o seu nome? ")
#     nota = float(input("Qual a sua nota? "))
#     alunos.append((nome, nota))

# # notas = [alunos[i][1] for i in range(alunos)]
# notas = [nota for _, nota in alunos] #- Já vai para outra tupla

# media = st.mean(notas)
# mediana = st.median(notas)
# moda = st.mode(notas)
# ddp = st.pstdev(notas) # Desvio de Padrão

# alunos_ordenados = (sorted(alunos, key=lambda aluno: aluno[1], reverse=True))
# alunos_ordenados2 = (sorted(alunos, key=lambda aluno: aluno[1], reverse=False))

# def proxima_media(aluno):
#     return abs(aluno[1] - 7)

# mais_proximo = min(alunos, key=proxima_media)
# print("Aluno mais próximo da média:", mais_proximo)

# print ("Alunos em ordem decrescente", alunos_ordenados)
# print ("Alunos em ordem decrescente", alunos_ordenados2)

# print(f"Média, {media}")
# print(f"Mediana, {mediana}")
# print(f"Moda, {moda}")
# print(f"Desvio de Padrão, {ddp}")

# Aprendendo Funções

# def saudacao(nome):
#     return f"Olá, {nome}"

# print (saudacao("Sophia"))

# for i in range(5): Jeito que eu fiz
#     x = int(input("Número? "))
#     def quadrado(numero):
#         return f"Resultado:, {numero * numero}"
#     print (quadrado(x)) 

# def quadrado(numero): # Jeito to chat
#     return numero * numero

# for i in range(5):
#     x = int(input("Número? "))
#     print(quadrado(x))



