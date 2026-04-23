print("--- CONSUMO DE ÁGUA --- \n")

cons_inic = float(input("Qual a leitura anterior do hidrômetro (m³): "))
cons_atual = float(input("Qual a leitura do hidrômetro atualmente (m³): "))
cons_real = cons_atual - cons_inic

preco_agua = cons_real * 4.50
taxa_esgt = preco_agua * 0.8
total = preco_agua + taxa_esgt + 12

print(f"\nO preço da água é R${preco_agua:.2f}, a taxa do esgoto é R${taxa_esgt:.2f}")
print(f"O custo total da conta de água é R${total:.2f} e o consumo de água foi {cons_real}m³")