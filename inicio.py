import random
def jogar():
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 4

    mensagem_de_inicio()

    for rodada in range(1, 5):
        print("Tentativa {} de {} ".format(rodada, total_de_tentativas))
        chute = int(input("Diga um número de 0 a 100: "))

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            mensagem_acertou()
            break
        elif (maior):
            mensagem_maior()
        elif (menor):
            mensagem_menor()

    mensagem_final(numero_secreto)


def mensagem_acertou():
    print("\nPARABÉNS, VOCÊ ACERTOU!\n")


def mensagem_maior():
    print("\nVocê errou! O seu chute foi maior que o número secreto\n")


def mensagem_menor():
    print("\nVocê errou! O seu chute foi menor que o número secreto\n")


def mensagem_de_inicio():
    print("*" * 56)
    print("*                 JOGO DE ADIVINHAÇÃO                  *")
    print(f'*        Bem vindo(a) ao jogo de adivinhação!          *\n'
          f'* Você terá {4} tentativas para acertar o número secreto *')
    print("*" * 56)



def mensagem_final(numero_secreto):
    print("O número secreto é: ", numero_secreto)
    print("*" * 56)
    print("*                    FIM DE JOGO!                      *")
    print("*" * 56)

if __name__ == '__main__':
    jogar()