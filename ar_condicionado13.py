comprimento = float(input("Qual o comprimento da sala (m²): "))
largura = float(input("Qual a largura da sala (m²): "))
area = comprimento * largura
btus = area * 600
kWh = (btus / 12000) * 1.2 * 8
preco = kWh * 0.85

print(f"Se o seu aparelho ficar ligado por 8 horas ele te custara R${preco:.2f} e {int(btus)}BTUs")