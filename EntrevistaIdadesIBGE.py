print("\t>> ENTREVISTA DE IDADES DO IBGE <<\n",
      "__________" * 4, "\n")
while True:
    try:
        qtdEntrevistados = int(input("Qual a quantidade de pessoas a serem entrevistadas?\n"))
    except ValueError:
        print("\nDado informado deve ser um número inteiro. Tente novamente...")
        continue
    break
maisNovo = 9999  #Truque para testar os mais novos
maisVelho = 0  #Truque para testar os mais velhos
qtdMenoresIdade = 0
somaIdades = 0
for i in range(qtdEntrevistados):  #O iterador percorre a quantidade de dados requisitados
    while True:  #Loop infinito para coletar idades
        try:
            idadeInformada = int(input("Por favor, informe a {}ª idade: ".format(i+1)))
        except ValueError:
            print("\nDado informado deve ser um número inteiro. Tente novamente..")
            continue
        break
    if idadeInformada >= maisVelho:  #Verificar se a idade informada é a mais velja
        maisVelho = idadeInformada
    if idadeInformada <= maisNovo:  #Verificar se a idade informada é a mais nova
        maisNovo = idadeInformada
    if idadeInformada < 18:  #Verificar se a idade informada é menor que 18 anos
        qtdMenoresIdade += 1
    qtdEntrevistados += 1  #Variável de controle contadora
    somaIdades += idadeInformada
porcentMenorIdade = (100/qtdEntrevistados) * qtdMenoresIdade * 2
mediaIdades = (somaIdades/qtdEntrevistados) * 2
print("\n\t\t>> RESULTADOS <<\n",
      "__________" * 3, "\n",
      "> Menor idade: {}\n".format(maisNovo),
      "> Maior idade: {}\n".format(maisVelho),
      "> Porcentagem dos menores de idade: {}%\n".format(porcentMenorIdade),
      "> Média das idades: {}".format(mediaIdades))