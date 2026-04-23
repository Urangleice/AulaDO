lado1 = int(input("Qual o primeiro tamanho: "))
lado2 = int(input("Qual o segundo tamanho: "))
lado3 = int(input("Qual o terceiro tamanho: "))

if lado1 == lado2 and lado2 == lado3:
    print(f"\nSeu triângulo é equilatero")

if lado1 == lado2 != lado3 or lado1 != lado2 == lado3 or lado1 == lado3 != lado2:
    print(f"\nSeu triângulo é isósceles")

if lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print(f"\nSeu triângulo é escaleno")
