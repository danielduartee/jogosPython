import random

def jogo2():
    abertura()
    palavra_secreta = opcoes_palavras_secretas()
    
    letras_acertadas = inicializa_letras_acerdatas(palavra_secreta)
    print(letras_acertadas)


    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
       
       chute = pede_chute()


       if(chute in palavra_secreta):
          marca_chute_correto(chute, letras_acertadas, palavra_secreta)

       else:
            erros = erros + 1
            desenha_forca(erros)

       erros = erros == 6
       acertou = "_" not in letras_acertadas

       print(letras_acertadas)
       
    if(acertou):
        mensagem_campeao()
    else:
       mensagem_acabou(palavra_secreta)

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
  index = 0
  for letra in palavra_secreta:
      if (chute == letra):
          letras_acertadas[index] = letra
      index = index + 1

def mensagem_campeao():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mensagem_acabou(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def abertura():
    print("*********************")
    print("***JOGUITO*CARALHO***")
    print("*********************")    

def opcoes_palavras_secretas():
    arquivo = open("palavras.txt", "r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()


    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_letras_acerdatas(palavra):
    return ["_" for letra in palavra]

def pede_chute(chute):
    input("Qual a letra? ")
    chute = chute.strip().upper()

    return chute    

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
if(__name__ == "__main__"):
    jogo2()
