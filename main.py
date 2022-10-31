from funcoes import (limparTela, loginCompetidor, loginDesafiante, dicas, desenho)

limparTela()
print ("Bem-vindo ao jogo da forca!")

desafiante = loginDesafiante ("Informe o nome do desafiante: ")
competidor = loginCompetidor ("Informe o nome do competidor: ")

limparTela()

letrasValidas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letrasChutadas = []
quantasDicas = 2
tentativas = 0
chances = 5
n = ['0', '1']
dica = 0
erro = 0

palavraChave = input ("Desafiante informe a palavra chave aqui: ")
palavras = list(palavraChave)
letras = palavras
if letras not in letrasValidas:
    print('Escreva um caractere válido!')
limparTela()

arquivo = open ("jogo.forca", "w")
arquivo.write (desafiante)
arquivo.write ("\n")
arquivo.write(competidor)
arquivo.write ("\n")
arquivo.write (palavraChave)
arquivo.write ("\n")
arquivo.close 

arquivo = open ("jogo.forca", "r")
letras = len(palavraChave)
listaDicas = dicas()
limparTela()

numLetras = ['*'] * len(palavraChave)
print(f'A palavra é {numLetras}')

def desafianteVencedor ():
    print(f"Você, {desafiante},venceu o JOGO DA FORCA!")
    print("\nA palavra era:", palavraChave)

def competidorVencedor ():
    print(f"Você, {competidor},venceu o JOGO DA FORCA!")
    print("\nA palavra era:", palavraChave)

try:
    
    while True:
        tentar = input("\nVocê deseja Jogar [0] ou Solicitar uma dica [1]? ")
        limparTela()

        if tentar == "1":
            quantasDicas = quantasDicas - dica 
            dica = dica + 1
            print ("""A sua dica é: ", listaDicas.pop()
            f"\nVocê já pediu {dica} dica(s), agora restam {quantasDicas} dicas!""")
            print("\nAgora você tem que chutar uma letra!")
            chute = input("Informe a letra que deseja chutar: ")
            letrasChutadas.append(chute.upper())

            if chute not in letrasValidas:
                print("Escreva um caractere válido!")
            
            if chute in palavraChave:
                print("Parabéns, você acertou a letra!")
                for i in range(len(palavraChave)):
                    if chute == palavraChave[i]:
                        numLetras[i] = chute
                        print(f"\nAqui é como está até agora: {numLetras}")
                        print(f"\nAqui são as letras que já foram: {letrasChutadas}")
                        letrasChutadas.append(chute.upper())

            else:
                print("\nQue pena! Essa letra não está na palavra")
                erro = erro + 1
                desenho(erro)
                tentativas = tentativas + 1
                restam = (chances - tentativas)
                print(f"Você já errou {tentativas} vez(es), lhe restam {restam} tentativa(s).")
                letrasChutadas.append(chute.upper())

        elif tentar == "0":
            chute = input("Informe a letra que deseja chutar: ")
            letrasChutadas.append(chute.upper())

            if chute not in letrasValidas:
                print("Escreva um caractere válido!")
            
            if chute in palavraChave:
                print("Parabéns, você acertou a letra!")
                for i in range(len(palavraChave)):
                    if chute == palavraChave[i]:
                        numLetras[i] = chute
                        print(f"\nAqui é como está até agora: {numLetras}")
                        print(f"\nAqui são as letras que já foram: {letrasChutadas}")
                        letrasChutadas.append(chute.upper())

            else:
                print("\nQue pena! Essa letra não está na palavra") 
                tentativas = tentativas + 1
                restam = (chances - tentativas)
                print(f"Você já errou {tentativas} vez(es), lhe restam {restam} tentativa(s).")
                erro = erro + 1
                desenho(erro)
                letrasChutadas.append(chute.upper())
        
        else:
            print("Comando invalido")
            tentar == 1 
        
        if tentativas == 5:
            desafianteVencedor() 
            break

        elif numLetras == palavras:
            competidorVencedor()
            break
except:
    if tentar not in n:
        print("Esse caractere não é válido! Tente novamente!")
        limparTela()
