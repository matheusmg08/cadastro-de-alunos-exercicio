"""
Vamos supor que precisamos criar um programa para cadastrar alunos em uma escola, armazenando informações como nome, idade e nota. Podemos utilizar um dicionário para representar cada aluno, onde a chave será o número de matrícula e o valor será outro dicionário contendo as informações do aluno.
"""
opcao = 1
alunos = {}
while opcao != 2:
        print('=' *50)
        print("1- Cadastro de alunos ")
        print("2- Sair")
        opcao = int(input("Digite a opção >>>> "))
        if opcao == 1:                 
            print("Cadastro de dados de alunos:")    
            numero_matricula = input("Digite o número de matrícula: ")
            nome = input("Digite seu nome: ")
            idade = input("Digite sua idade: ")
            nota = input("Digite sua nota: ")
            alunos[numero_matricula] = nome, idade, nota
            print("Adicionado com sucesso! ")
            print (f'Número de matrícula: {numero_matricula}, Nome: {nome}, Idade: {idade}, Nota: {nota}')
        else:
            print("Fim do programa")
