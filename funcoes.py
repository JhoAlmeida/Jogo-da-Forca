import os
def limparTela():
    os.system ("cls")

def loginDesafiante (nomeDesafiante):
    nome = input (nomeDesafiante)
    return nome

def loginCompetidor (nomeCompetidor):
    nome = input (nomeCompetidor)
    return nome

def dicas():
    x=1
    listaDica = []
    while(x < 4):
        dica = input(f"Digite a {x} dica: ")  
        listaDica.append(dica)
        x = x + 1
    return listaDica

def desenho (erro):
    print ("  _______     ")
    print (" |/      |    ")
    
    if(erro == 1):
        print(" |      (;_;)   ")
        print(" |              ")
        print(" |              ")
        print(" |              ")

    if(erro == 2):
        print(" |      (;_;)   ")
        print(" |        |     ")
        print(" |              ")
        print(" |              ")
 
    if(erro == 3):
        print(" |      (;_;)   ")
        print(" |        | \   ")
        print(" |              ")
        print(" |              ")

    if(erro == 4):
        print(" |      (;_;)    ")
        print(" |      / | \    ")
        print(" |               ")
        print(" |               ")

    if(erro == 5):
        print(" |      (;_;)   ")
        print(" |      / | \   ")
        print(" |        |     ")
        print(" |              ")

    if(erro == 6):
        print(" |      (;_;)    ")
        print(" |      / | \    ")
        print(" |        |      ")
        print(" |      /        ")

    if (erro == 7):
        print(" |      (;_;)    ")
        print(" |      / | \    ")
        print(" |        |      ")
        print(" |       / \     ")

    print(" |               ")
    print("_|___            ")
    print()

