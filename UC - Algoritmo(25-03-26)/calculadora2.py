def calculadora():
    opcao = ""

    while opcao != "0":
        print("\nCalculadora")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Fim do programa")

        elif opcao == "1":
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print("Resultado:", a + b)

        elif opcao == "2":
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print("Resultado:", a - b)

        elif opcao == "3":
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print("Resultado:", a * b)

        elif opcao == "4":
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            
            if b == 0:
                print("Erro: não pode dividir por zero")
            else:
                print("Resultado:", a / b)

        else:
            print("Opção inválida")

calculadora()