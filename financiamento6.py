carro = float(input("Qual o preco do carro (15000/R$15000,00): ").replace(",",".").replace("R$",""))
taxa_mes = float(input("Qual o valor da taxa (%): ").replace("%","").replace(",","."))
numero_parc = float(input("Qual a quantidade de parcelas: "))

juros = carro * ((taxa_mes/100) * numero_parc)
carro_valor = carro + juros
preco_parc = carro_valor/numero_parc

print(f"\nO seu carro custa sem juros R${carro:.2f}")
print(f"O seu carro com juros fica custando R${carro_valor:.2f} e cara parcela custa R${preco_parc:.2f}")