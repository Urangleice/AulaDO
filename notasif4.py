print("        --- SISTEMA DE NOTAS ---")
n1 = float(input("          Qual foi a nota 1: "))
n2 = float(input("          Qual foi a nota 2: "))
n3 = float(input("          Qual foi a nota 3: "))
n4 = float(input("          Qual foi a nota 4: "))
print("")
media = (n1 + n2 + n3 + n4) / 4

maior_nota = n1
menor_nota = n1

if n2 > maior_nota:
    maior_nota = n2
if n3 > maior_nota:
    maior_nota = n3
if n4 > maior_nota:
    maior_nota = n4

if n2 < menor_nota:
    menor_nota = n2
if n3 < menor_nota:
    menor_nota = n3
if n4 < menor_nota:
    menor_nota = n4

print(f"   A maior nota é {maior_nota} e a menor é {menor_nota}.")

"""
OPÇÃO 2 PARA VER QUAL A MAIOR E MENOR NOTA

if n1 >= n2 and n1 >= n3 and n1 >= n4:
    print(f"A primeira nota, {n1}, é a maior.")
if n2 >= n1 and n2 >= n3 and n2 >= n4:
    print(f"A segunda nota, {n2}, é a maior.")
if n3 >= n1 and n3 >= n2 and n3 >= n4:
    print(f"A terceira nota, é {n3}, a maior.")
if n4 >= n1 and n4 >= n2 and n4 >= n3:
    print(f"A quarta nota, {n4}, é a maior.")
if n1 <= n2 and n1 <= n3 and n1 <= n4:
    print(f"A primeira nota, {n1}, é a menor.")
if n2 <= n1 and n2 <= n3 and n2 <= n4:
    print(f"A segunda nota, {n2}, é a menor.")
if n3 <= n1 and n3 <= n2 and n3 <= n4:
    print(f"A terceira nota, {n3}, é a menor.")
if n4 <= n1 and n4 <= n2 and n4 <= n3:
    print(f"A quarta nota, {n4}, é a menor.")"""
print("")

print("  --- VERIFICANDO SE HÁ NOTAS IGUAIS... ---")
if n1 == n2:
    print(f"     As notas n1 e n2 são iguais a {n1}.")

if n1 == n3:
    print(f"     As notas n1 e n3 são iguais a {n1}.")

if n1 == n4:
    print(f"     As notas n1 e n4 são iguais a {n1}.")

if n2 == n3:
    print(f"     As notas n2 e n3 são iguais a {n2}.")

if n2 == n4:
    print(f"     As notas n2 e n4 são iguais a {n2}.")

if n3 == n4:
    print(f"     As notas n3 e n4 são iguais a {n3}.")
print("")

print(f"        A média nas notas é {media:.2f}.")
if media >= 7 and media <= 10:
    print("              APROVADA(O)!")

if media >= 5 and media < 7:
    print("              RECUPERAÇÃO!")

if media >= 0 and media < 5:
    print("              REPROVADA(O)!")
