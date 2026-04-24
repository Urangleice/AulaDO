print("--- LOCAÇÃO DE CARROS ---\n")

categoria_carro = int(input("--- Categoria do Carro ---\n |1- sport \n |2- suv luxury \n |3-electric \n Escolha a categoria: "))
renda_mensal = float(input("Digite sua renda mensal em reais: R$"))
idade_condutor = int(input("Digite a idade do condutor: "))
tempo_cnh = int(input("Digite há quantos anos possui a CNH: "))
pontos_cnh = int(input("Digite quantos pontos na CNH o condutor tem atualmente: "))
valor_carro = float(input("Digite o valor do carro desejado em reais: R$"))
print()

if idade_condutor < 21 or tempo_cnh < 2:
    print("Assinatura Negada: Experiência insuficiente para a categoria selecionada.")
    exit()

if categoria_carro == 1 and (idade_condutor < 25 or tempo_cnh < 5):
    print("Assinatura Negada: Experiência insuficiente para a categoria selecionada.")
    exit()

if pontos_cnh > 20:
    print("Assinatura Negada: Pontuação na CNH excede o limite de segurança.")
    exit()
elif categoria_carro == 3 and pontos_cnh > 10:
    print("Assinatura Negada: Pontuação na CNH excede o limite de segurança.")
    exit()

if renda_mensal <= 5000 and valor_carro > 80000:
    print(f"Assinatura Negada: Valor do veículo (R$ {valor_carro:,.2f}) incompatível com a renda mensal.")
    exit()
elif renda_mensal <= 10000 and valor_carro > 150000:
    print(f"Assinatura Negada: Valor do veículo (R$ {valor_carro:,.2f}) incompatível com a renda mensal.")
    exit()
elif renda_mensal > 10000 and valor_carro > 300000:
    print(f"Assinatura Negada: Valor do veículo (R$ {valor_carro:,.2f}) incompatível com a renda mensal.")
    exit()
    
mensalidade = valor_carro * 0.015
if mensalidade > (renda_mensal * 0.3):
    print(f"Assinatura Negada: Mensalidade de R$ {mensalidade:,.2f} excede o limite de 30% da renda.")
    exit()
    
print(f"CONTRATO LIBERADO! Categoria: {categoria_carro}. Carro: R${valor_carro:,.2f}. Mensalidade: R${mensalidade:,.2f}. Aproveite seu veículo!")