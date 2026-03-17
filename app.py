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


def main():
    while True:
        print("\n===== MENU DE EXERCICIOS =====")
        print("1 - Exercicio de autenticacao")
        print("2 - Exercicio de nota")
        print("0 - Sair")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            exercicio_autenticacao()
        elif opcao == "2":
            exercicio_nota()
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opcao invalida. Tente novamente.")


main()