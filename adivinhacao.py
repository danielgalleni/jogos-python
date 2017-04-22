import random

def jogar():
    numero_secreto = random.randrange(1,101)
    mensagem = "\nVocê deve digitar um número entre 1 e 100!"
    pontos = 1000

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    print("")
    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Dfícil")

    nivel = int(input("Escolha o nível:"))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada  in range(1, total_de_tentativas + 1):
        print("")
        print("******* Tentativa {} de {} *******".format(rodada, total_de_tentativas))
        print(mensagem)

        chute_str = input("Digite seu número: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if (chute < 1) or (chute > 100):
            continue

        acertou = numero_secreto == chute
        maior   = numero_secreto < chute
        menor   = numero_secreto > chute

        if(acertou):
            print("Você acertou!")
            print("Pontos: {}".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! Seu chute foi maior que o número secreto!")
            elif(menor):
                print("Você errou! Seu chute foi menor que o número secreto!")
            pontos_perdidos = abs(numero_secreto - chute) // 3
            pontos = pontos - pontos_perdidos

    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()