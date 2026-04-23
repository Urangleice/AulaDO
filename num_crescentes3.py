n1 = int(input("Digite o número 1: "))
n2 = int(input("Digite o número 2: "))
n3 = int(input("Digite o número 3: "))
n4 = int(input("Digite o número 4: "))

if n1 > n2:
    n1, n2 = n2, n1
if n2 > n3:
    n2, n3 = n3, n2
if n3 > n4:
    n3, n4 = n4, n3

if n1 > n2:
    n1, n2 = n2, n1
if n2 > n3:
    n2, n3 = n3, n2

if n1 > n2:
    n1, n2 = n2, n1

print(f"Ordem crescente: {n1}, {n2}, {n3}, {n4}")
