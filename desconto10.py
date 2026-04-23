vt = float(input("Digite o valor total da compra: "))

if vt > 200:
    vt = vt * 0.90
    print(f"Desconto aplicado, valor final: {vt:.2f}")
else:
    print(f"Sem desconto, valor final: {vt:.2f}")
