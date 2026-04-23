op = input("Digite o sinal do operador (+, -, *, /): ")
n1 = float(input("Digite o número 1: "))
n2 = float(input("Digite o número 2: "))

match op:
    case "+":
        resultado = n1+n2
    case "-":
        resultado = n1-n2
    case "*":
        resultado = n1*n2
    case "/":
        resultado = n1/n2 if n2 != 0 else "ERRO: Divisão por zero"





print(f"Resultado é {resultado}.")