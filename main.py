#PEDRA & PAPEL & TESOURA - BY: Kayck Gabriel.

pedra = 0
papel = 1
tesoura = 2
novamente = "Sim"

while (novamente == "Sim"):

    jogador01=int(input("Jogador01, Digite: \n 0 para PEDRA\n 1 para PAPEL\n 2 para TESOURA\n : "))
    jogador02=int(input("Jogador02, Digite: \n 0 para PEDRA\n 1 para PAPEL\n 2 para TESOURA\n : "))

    if 0 <= jogador01 <= 2 and 0 <= jogador02 <= 2:

        if jogador01 == jogador02:
            print("Empate! Ninguém ganhou.")

        elif jogador01 - jogador02 == -2 or jogador01 - jogador02 == 1:
            print("Jogador 01 ganhou.")

        else:
            print("Jogador 02 ganhou.")

    else:
        print("ERROR404 - Opção inválida.")

    novamente = input("Deseja tentar novamente? Digite S/N: ")

print("Fim!")
