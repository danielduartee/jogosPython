import jogo1
import jogo2

def escolha_jogo():
    print("*********************")
    print("***JOGUITO*CARALHO***")
    print("*********************")
    
    print("(1) Jogo (2)Jogo2")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("Advinhação")
        jogo1.jogo1()
    elif(jogo == 2):
        print("Game0") 
        jogo2.jogo2()

if(__name__ == "__main__"):
    escolha_jogo()