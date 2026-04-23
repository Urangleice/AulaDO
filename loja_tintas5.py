largura = float(input("Qual a largura da área(m²): "))
comprimento = float(input("Qual o comprimento da área(m²): "))

area = largura * comprimento
area_real = area
litros = area/6

latas = litros/18
galoes = litros/3.6

print(f"Você gastou {latas:.2f} latas")
print(f"Você gastou {galoes:.2f} galoes")

litros_tot = litros * 1.1
litros = litros_tot

latas = litros_tot//18
litros_tot = litros_tot - latas*18
galoes = litros//3.6

print(f"Você gastou {latas} e {galoes} com {int(litros)}L")