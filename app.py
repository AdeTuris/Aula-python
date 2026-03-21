def exercicio_autenticacao():
    print("\n=== EXERCICIO 1: SISTEMA DE AUTENTICACAO ===")

    usuario = "admin"
    senha = "1234"

    while True:
        login = input("Usuario: ")
        password = input("Senha: ")

        if login == usuario and password == senha:
            print("Acesso permitido")
        else:
            print("Acesso negado")

        continuar = input("Tentar novamente neste exercicio? (sim/nao): ").strip().lower()
        if continuar != "sim":
            break


def exercicio_nota():
    print("\n=== EXERCICIO 2: CLASSIFICACAO DE NOTA ===")

    while True:
        nota = float(input("Digite a nota (0 a 10): "))

        if nota >= 7:
            print("Aprovado")
        elif nota >= 4:
            print("Recuperacao")
        else:
            print("Reprovado")

        continuar = input("Tentar novamente neste exercicio? (sim/nao): ").strip().lower()
        if continuar != "sim":
            break


def exercicio_tabuada():
    print("\n=== EXERCICIO 3: TABUADA ===")

    while True:
        numero = int(input("Digite um numero para ver a tabuada: "))

        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")

        continuar = input("Tentar novamente neste exercicio? (sim/nao): ").strip().lower()
        if continuar != "sim":
            break


def exercicio_media_sentinela():
    print("\n=== EXERCICIO 4: MEDIA COM SENTINELA ===")
    print("Digite notas de 0 a 10. Para finalizar, digite -1.")

    while True:
        soma = 0.0
        quantidade = 0

        while True:
            nota = float(input("Digite uma nota (-1 para encerrar): "))

            if nota == -1:
                break

            if 0 <= nota <= 10:
                soma += nota
                quantidade += 1
            else:
                print("Nota invalida. Digite um valor entre 0 e 10.")

        if quantidade > 0:
            media = soma / quantidade
            print(f"Media da turma: {media:.2f}")
        else:
            print("Nenhuma nota valida foi informada.")

        continuar = input("Tentar novamente neste exercicio? (sim/nao): ").strip().lower()
        if continuar != "sim":
            break


def exercicio_fatorial():
    print("\n=== EXERCICIO 5: FATORIAL ===")

    while True:
        numero = int(input("Digite um numero inteiro nao negativo: "))

        if numero < 0:
            print("Valor invalido. Digite um numero maior ou igual a zero.")
        else:
            resultado = 1
            for i in range(1, numero + 1):
                resultado *= i
            print(f"{numero}! = {resultado}")

        continuar = input("Tentar novamente neste exercicio? (sim/nao): ").strip().lower()
        if continuar != "sim":
            break


def main():
    while True:
        print("\n===== MENU DE EXERCICIOS =====")
        print("1 - Exercicio de autenticacao")
        print("2 - Exercicio de nota")
        print("3 - Exercicio de tabuada")
        print("4 - Exercicio de media com sentinela")
        print("5 - Exercicio de fatorial")
        print("0 - Sair")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            exercicio_autenticacao()
        elif opcao == "2":
            exercicio_nota()
        elif opcao == "3":
            exercicio_tabuada()
        elif opcao == "4":
            exercicio_media_sentinela()
        elif opcao == "5":
            exercicio_fatorial()
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opcao invalida. Tente novamente.")


main()