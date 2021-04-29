import random
def jogar():
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 5

    mensagem_de_inicio()

    for rodada in range(1, 6):
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
    print("\nParabéns, você acertou!\n")


def mensagem_maior():
    print("\nVocê errou! O seu chute foi maior que o número secreto\n")


def mensagem_menor():
    print("\nVocê errou! O seu chute foi menor que o número secreto\n")


def mensagem_de_inicio():
    print("*" * 54)
    print("*                Jogo da adivinhação                 *")
    print("*" * 54)


def mensagem_final(numero_secreto):
    print("O número secreto é: ", numero_secreto)
    print("*" * 54)
    print("*                   Fim de jogo!                     *")
    print("*" * 54)

if __name__ == '__main__':
    jogar()