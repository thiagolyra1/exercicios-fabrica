while True:
    # Validando os números do usuário
    try:
        numero1 = float(input("Digite aqui o primeiro número: "))
        numero2 = float(input("Digite aqui o segundo número: "))
    except ValueError:
        print("Você não digitou um número. Digite novamente do primeiro número")
        continue
    
    while True:
        # Operação a ser utilizada na calculadora
        operacao = input("Qual operação você gostaria de realizar? Para somar digite: +, subtrair: -, multiplicar: x ou dividir: /: ")

        # Lógica das operações
        adicao = numero1 + numero2
        subtracao = numero1 - numero2
        multiplicacao = numero1 * numero2
        divisao = numero1 / numero2

        # Condição para escolher a operação
        if operacao == "+":
            print(f'O resultado de {numero1} + {numero2} é:  {adicao}')
            break
        elif operacao == "-":
            print(f'O resultado de {numero1} - {numero2} é:  {subtracao}')
            break
        elif operacao == "x":
            print(f'O resultado de {numero1} x {numero2} é: {multiplicacao}')
            break
        elif operacao =="/":
            print(f'O resultado de {numero1} / {numero2} é: {divisao}')
            break
        else:
            print("Não é uma operação válida, escolha novamente.")
            continue
    
    while True:
        # Pergunta para continuar ou sair do projeto
        sair = input("Você deseja sair da calculadora? [s]im ou [n]ão: ")

        # Condição para sair ou continuar no projeto
        if sair == "s":
            print("Obrigado por utilizar a calculadora. Volte sempre!")
            exit()
        elif sair == "n":
            print("Vamos começar uma nova conta!")
            break
        else:
            print("Digite apenas 's' para sim ou 'n' para não: ")
            continue
