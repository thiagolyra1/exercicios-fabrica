# Loop geral
while True:

    # Funções
    def nao_digitou_numero():
        return print("Você não digitou um número. Digite novamente do primeiro número")
    
    def soma(primeiro,segundo):
        resultado = print(f'O resultado de {primeiro} + {segundo} é:  {primeiro+segundo}')
        return resultado
    def subtracao(primeiro,segundo):
        resultado = print(f'O resultado de {primeiro} - {segundo} é:  {primeiro-segundo}')
        return resultado
    def multiplicacao(primeiro,segundo):
        resultado = print(f'O resultado de {primeiro} + {segundo} é:  {primeiro*segundo}')
        return resultado
    # def divisao(primeiro,segundo):
    #     resultado = print(f'O resultado de {primeiro} + {segundo} é:  {primeiro/segundo}')
    #     return resultado
    
    # Função lambda
    divisao = lambda primeiro, segundo: print(f'O resultado de {primeiro} + {segundo} é: {primeiro/segundo}')
    
    # Validando os números do usuário    
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
    except ValueError:
        nao_digitou_numero()
        continue

    # Loop para escolher operação com validação
    while True:
        # Operação a ser utilizada na calculadora
        operacao = input("Qual operação você gostaria de realizar? \
                         \nPara somar digite: +, subtrair: -, multiplicar: x ou dividir: /: ")

        

        # Condição para escolher a operação
        if operacao == "+":
            soma(numero1,numero2)
            break
        elif operacao == "-":
            subtracao(numero1,numero2)
            break
        elif operacao == "x":
            multiplicacao(numero1,numero2)
            break
        elif operacao =="/":
            try:
                divisao(numero1,numero2)
            except ZeroDivisionError:
                print("Não pode ser dividido por 0.")
            break
        else:
            print("Não é uma operação válida, escolha novamente.")
            continue

    # Loop para sair ou cotinuar no programa, com validação
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