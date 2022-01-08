import random

def jogo1():

    print("*********************")
    print("***JOGUITO*CARALHO***")
    print("*********************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 3
    pontos = 1000

    print("Qaul nivel de ficiculdade?")
    print("(1) Facil (2) Medio (3) Dificil")

    nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:total_de_tentativas == 5

    for rodada in range(1,  total_de_tentativas + 1):
        print("Tentativa {} de {}" .format(rodada, total_de_tentativas))
        chute_str = input("Digite um  numero entre 1 e 100")
        print("você digitou " , chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você tem que digitar um numero entre 1 e 100!")
            continue

        acertou  = chute == numero_secreto
        maior    = chute > numero_secreto
        menor    = chute < numero_secreto

        if(numero_secreto == chute):
            print("UHUL, você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("exagerou")
            elif(menor):
                print("foi muito abaixo")
            
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos 

    print("FIM")

if(__name__ == "__main__"):
    jogo1()
