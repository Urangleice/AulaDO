# ENTRADA DE DADOS
print("--- ANÁLISE DE CRÉDITO ---")
   
renda_mensal = float(input("Digite sua renda mensal: "))
idade = int(input("Digite sua idade: ")) 
# Adicionado () em .upper() para o método funcionar
historico = input("Seu histórico de crédito é 'RUIM' ou 'BOM'? ").upper()
score = int(input("Digite o valor da sua nota de crédito (score de 0 a 10): "))
credito_solicitado = float(input("Digite o crédito a ser solicitado: "))
parcelas_solicitadas = int(input("Digite o número de parcelas a serem solicitadas: "))

credito_disponivel = 0
prazo_anos = 0  

# FILTROS INICIAIS + CRÉDITO DISPONÍVEL
if idade < 18 or idade > 60:
    print("CRÉDITO NEGADO: fora da faixa etária permitida.")
elif historico == "RUIM":
    print("CRÉDITO NEGADO: histórico com restrições.")
else:
    # Correção: Usando '=' para atribuir e removendo pontos/vírgulas dos números
    if renda_mensal <= 2000.00:
        credito_disponivel = 0.00
    elif renda_mensal <= 5000.00:
        credito_disponivel = 50000.00 
    elif renda_mensal <= 8000.00:
        credito_disponivel = 150000.00 
    elif renda_mensal <= 14000.00:
        credito_disponivel = 300000.00
    else:
        credito_disponivel = 0.00
        
    # PRAZO MÁXIMO E CÁLCULO FINAL (Só executa se passou nos filtros iniciais)
    if credito_disponivel == 0:
        print("CRÉDITO NEGADO: Sem crédito disponível para esta faixa de renda.")
    else:
        # DEFINIÇÃO DO PRAZO MÁXIMO
        if 18 <= idade <= 30:
            prazo_anos = 35 if score >= 7 else 25
        elif 31 <= idade <= 60:
            prazo_anos = 25 if score >= 7 else 15

        # CÁLCULOS
        valor_parcela = credito_solicitado / parcelas_solicitadas
        limite_comprometimento = renda_mensal * 0.25
        prazo_maximo = parcelas_solicitadas / 12
        prazo_meses = parcelas_solicitadas -(int(prazo_maximo) * 12)

        print(f"\n--- RESULTADO DA ANÁLISE ---")
        print(f"CRÉDITO DISPONÍVEL: R$ {credito_disponivel:.2f}")
        print(f"PRAZO MÁXIMO: {prazo_anos} anos.")
        print(f"VALOR DA PARCELA: R$ {valor_parcela:.2f}")

        if valor_parcela <= limite_comprometimento:
            print(f"CRÉDITO APROVADO! Valor: R$ {credito_solicitado:.2f}, em {int(prazo_maximo)} anos e {prazo_meses} meses, com parcelas de R$ {valor_parcela:.2f}.")
        else:
            print("CRÉDITO NEGADO: Valor da parcela excede o limite de comprometimento de renda (25%).")

    
    
