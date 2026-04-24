print("--- LOCAÇÃO DE CARROS ---\n")
categoria_carro = input("--- Categoria do Carro ---\n |1- sport \n |2- suv luxury \n |3-electric \n Escolha a categoria: ")
renda_mensal = float(input("Digite sua renda mensal em reais: R$"))
idade_condutor = int(input("Digite a idade do condutor: "))
tempo_cnh = int(input("Digite há quantos anos possui a CNH: "))
pontos_cnh = int(input("Digite quantos pontos na CNH o condutor tem atualmente: "))
valor_carro = float(input("Digite o valor do carro desejado em reais: R$"))
print()

if idade_condutor < 21 or tempo_cnh < 2:
    print("Assinatura Negada: Experiência insuficiente para a categoria selecionada.")
    exit()
elif categoria_carro == 1 and idade_condutor < 25 or tempo_cnh < 5:
    print("Assinatura Negada: Experiência insuficiente para a categoria selecionada.")
    exit()


    
'''Regra: Para qualquer categoria, o condutor 
deve ter pelo menos 21 anos e 2 anos de CNH.

Aninhamento: Se o carro for da categoria "Sport", 
a idade mínima sobe para 25 anos e o tempo de CNH 
para 5 anos.

Reprovação: "Assinatura Negada: Experiência 
insuficiente para a categoria selecionada."'''