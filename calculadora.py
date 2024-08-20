while True:
    # Validando os números dos usuários
    try:
        numero1 = float(input("Digite aqui o primeiro número: "))
        numero2 = float(input("Digite aqui o segundo número: "))
    except ValueError:
        print("Você não digitou um número.")
        continue
    
    retornar_operacao = True
    while retornar_operacao:
        # Operação a ser utilizada na calculadora
        operacao = input("Qual operação você gostaria de realizar? Escolha algum desses: '+', '-', 'x' ou '/': ")

        # Lógica das operações
        adicao = numero1 +numero2
        subtracao = numero1 - numero2
        multiplicacao = numero1 * numero2
        divisao = numero1 / numero2

        # Condição para escolher a operação
        
        if operacao == "+":
            print(f'O resultado de {numero1} + {numero2} é:  {adicao}')
            retornar_operacao = False
        elif operacao == "-":
            print(f'O resultado de {numero1} - {numero2} é:  {subtracao}')
            retornar_operacao = False
        elif operacao == "x":
            print(f'O resultado de {numero1} x {numero2} é: {multiplicacao}')
            retornar_operacao = False
        elif operacao =="/":
            print(f'O resultado de {numero1} / {numero2} é: {divisao}')
            retornar_operacao = False
        else:
            print("Não é uma operação válida, escolha novamente.")
            retornar_operacao = True
    
    # Pergunta para continuar ou sair do projeto
    sair = input("Você deseja sair da calculadora? [s]im ou [n]ão: ")

    # Condição para sair ou continuar no projeto
    if sair == "s":
        break
    elif sair == "n":
        continue
    else:
        print("Digite apenas 's' para sim ou 'n' para não: ")
