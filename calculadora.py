while True:
    try:
        numero1 = float(input("Digite aqui o primeiro número: "))
        numero2 = float(input("Digite aqui o segundo número: "))
    except ValueError:
        print("Você não digitou um número.")
        continue
    
    operacao = input("Qual operação você gostaria de realizar? Escolha algum desses: 'adicao', 'subtracao', 'multiplicacao' ou 'divisao': ")

    adicao = numero1 +numero2
    subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2
    divisao = numero1 / numero2

    if operacao == "adicao":
        print(f'O resultado de {numero1} + {numero2} é:  {adicao}')
    elif operacao == "subtracao":
        print(f'O resultado de {numero1} - {numero2} é:  {subtracao}')
    elif operacao == "multiplicacao":
        print(f'O resultado de {numero1} x {numero2} é: {multiplicacao}')
    elif operacao =="divisao":
        print(f'O resultado de {numero1} / {numero2} é: {divisao}')
    else:
        print("Digite as opções corretas, são essas: 'adicao', 'subtracao', \
                    'multiplicacao' ou 'divisao'")
        
    sair = input("Você deseja sair da calculadora? [s]im ou [n]ão: ")

    if sair == "s":
        break
    elif sair == "n":
        continue
    else:
        print("Digite apenas 's' para sim ou 'n' para não: ")
