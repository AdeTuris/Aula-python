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


def exercicio_numeros_1_a_10():
    print("\n=== EXERCICIO 6: NUMEROS DE 1 A 10 ===")

    while True:
        for numero in range(1, 11):
            print(f"Numero {numero}")

        continuar = input("Tentar novamente neste exercicio? (sim/nao): ").strip().lower()
        if continuar != "sim":
            break


def exercicio_pares_1_a_20():
    print("\n=== EXERCICIO 7: PARES DE 1 A 20 ===")

    while True:
        for numero in range(1, 21):
            if numero % 2 == 0:
                print(numero)

        continuar = input("Tentar novamente neste exercicio? (sim/nao): ").strip().lower()
        if continuar != "sim":
            break


def exercicio_tabuada_aula05():
    print("\n=== EXERCICIO 8: TABUADA AULA 05 ===")

    while True:
        tabuada = int(input("Digite um numero para a tabuada: "))

        for numero in range(1, 11):
            print(f"{tabuada} x {numero} = {tabuada * numero}")

        continuar = input("Tentar novamente neste exercicio? (sim/nao): ").strip().lower()
        if continuar != "sim":
            break


def exercicio_digitar_ate_zero():
    print("\n=== EXERCICIO 9: DIGITAR NUMEROS ATE ZERO ===")

    while True:
        numero = int(input("Digite um numero (0 para encerrar): "))

        if numero == 0:
            print("Encerrando leitura de numeros.")
            break


def exercicio_media_5_notas():
    print("\n=== EXERCICIO 10: MEDIA DE 5 NOTAS ===")

    while True:
        soma = 0.0

        for indice in range(1, 6):
            nota = float(input(f"Digite a nota {indice}: "))
            soma += nota

        media = soma / 5
        print(f"Soma das notas: {soma:.2f}")
        print(f"Media: {media:.2f}")

        if media >= 7:
            print("Status: Aprovado")
        else:
            print("Status: Reprovado")

        continuar = input("Tentar novamente neste exercicio? (sim/nao): ").strip().lower()
        if continuar != "sim":
            break


def exercicio_sequencia_condicional_dinamica():
    print("\n=== EXERCICIO 11: SEQUENCIA CONDICIONAL DINAMICA ===")
    print("Regra: multiplo de 3 = Fizz, multiplo de 5 = Buzz, ambos = FizzBuzz")

    while True:
        limite = int(input("Digite um numero inteiro N: "))

        for numero in range(1, limite + 1):
            if numero % 3 == 0 and numero % 5 == 0:
                print("FizzBuzz")
            elif numero % 3 == 0:
                print("Fizz")
            elif numero % 5 == 0:
                print("Buzz")
            else:
                print(numero)

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
        print("6 - Exibir numeros de 1 a 10")
        print("7 - Mostrar numeros pares de 1 a 20")
        print("8 - Tabuada aula 05")
        print("9 - Pedir numeros ate digitar zero")
        print("10 - Pedir 5 notas e calcular media")
        print("11 - Sequencia condicional dinamica (FizzBuzz)")
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
        elif opcao == "6":
            exercicio_numeros_1_a_10()
        elif opcao == "7":
            exercicio_pares_1_a_20()
        elif opcao == "8":
            exercicio_tabuada_aula05()
        elif opcao == "9":
            exercicio_digitar_ate_zero()
        elif opcao == "10":
            exercicio_media_5_notas()
        elif opcao == "11":
            exercicio_sequencia_condicional_dinamica()
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opcao invalida. Tente novamente.")


main()