import random  #Função que gera números aleatórios

def mostrarOpcoes():
    print("Digite 1 para Pedra," +
          "\n       2 para Papel," +
          "\n       3 para Tesoura" +
          "\n       ou 0 para encerrar.")
def validarEscolha(pergunta):  #Função para validar dados de entrada
    while True:
        try:
            escolha = int(input(pergunta))
        except ValueError:
            print("Apenas números inteiros!")
            mostrarOpcoes()
            continue
        if escolha < 0 or escolha > 3:
            print("Os valores devem ser de 0 até 3!")
            mostrarOpcoes()
            continue
        break
    return escolha
def mostrarJogadas():  #Função para mostrar as jogadas a cada rodada
    global jogadaUsuario, jogadaPc, jogadas
    jogadas.append([jogadaUsuario, jogadaPc])
    print("\n\tJOGADAS ATÉ AGORA:")
    for jogada in jogadas:
        print("_" * 25 +
              "\nJogada do Usuário: {}".format(jogada[0]) +
              "\nJogada do Computador: {}".format(jogada[1]))
    print("_" * 25)
def vencedor(usuario, pc):  #Função para definir o vencedor de cada jogada
    global vitoriasUsuario, vitoriasPc, empates
    if usuario == 1:  #Pedra
        if pc == 1:  #Pedra
            empates += 1
        elif pc == 2:  #Papel
            vitoriasPc += 1
        elif pc == 3:  #Tesoura
            vitoriasUsuario += 1
    elif usuario == 2:  #Papel
        if pc == 1:  #Pedra
            vitoriasUsuario += 1
        elif pc == 2:  #Papel
            empates += 1
        elif pc == 3:  #Tesoura
            vitoriasPc += 1
    elif usuario == 3:  #Tesoura
        if pc == 1:  #Pedra
            vitoriasPc += 1
        elif pc == 2:  #Papel
            vitoriasUsuario += 1
        elif pc == 3:  #Tesoura
            empates += 1
    resultados = [vitoriasUsuario, vitoriasPc, empates]
    #"resultados" é uma var local que armazena
    #as vitórias do usuário, do PC e os empates
    #em seus índices 0, 1 e 2, respectivamente
    return resultados
#Programa principal
print("\t!! JOKENPÔ !!")
mostrarOpcoes()
jogadas = []
vitoriasUsuario = 0
vitoriasPc = 0
empates = 0
while True:
    jogadaUsuario = validarEscolha(">> Escolha sua jogada: ")
    if not jogadaUsuario:  #jogadasUsuario == 0
        break
    jogadaPc = random.randint(1, 3)  #Jogada do PC é aleatória
    mostrarJogadas()
    resultados = vencedor(jogadaUsuario, jogadaPc)
    #"resultados" é uma variável global
    #para armazenar os dados retornados da função "vencedor"
print("\nPartidas encerradas!")
print("Número de vitórias do Usuário: {}".format(resultados[0]))
print("Número de vitórias do Compurtador: {}".format(resultados[1]))
print("Número de empates: {}".format(resultados[2]))