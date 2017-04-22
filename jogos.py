import forca
import adivinhacao

def escholha_jogo():
    print("*********************************")
    print("Bem vindo ao menu de Jogos!")
    print("*********************************")
    print("")
    print("Escolha seu jogo?")
    print("(1) Forca (2) Adivinhacao (3) Sair")

    jogo = int(input("Qual jogo?"))

    if (jogo == 1):
        forca.jogar()
    elif (jogo == 2):
        adivinhacao.jogar()
    else:
        print("Obrigado por jogar!")
        exit()

if(__name__ == "__main__"):
    escholha_jogo()