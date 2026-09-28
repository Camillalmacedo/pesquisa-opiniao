#Boas vindas
print("Bem-vindo(a) à pesquisa de opinião da empresa TudoWeb!")

#Entrada de dados
excelente = 0
ruim = 0

#Estrutura de repetição para coleta de dados
for i in range(1, 51):
    print("ENTREVISTADO", i)
    nome = input("Digite o seu nome: ")
    idade = input("Digite a sua idade: ")
    
    opiniao = input(f'''Qual a sua opinião sobre o atendimento prestado?
    1: EXCELENTE
    2: BOM
    3: RUIM
    Digite apenas o número de sua escolha: ''')

    if opiniao == "1":
        excelente = excelente + 1
   
    elif opiniao == "3":
            ruim = ruim + 1

print(f'''Quantidade de respostas EXCELENTE: {excelente}''')
print(f'''Quantidade de respostas RUIM: {ruim}''')