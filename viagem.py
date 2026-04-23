print("--- SIMULADOR DE VIAGEM INTERNACIONAL PERSONALIZADA ---\n")

duracao = int(input("Quantidade de dias que pretende ficar no local: "))
destino_desejado = int(input("-> Destinos disponíveis <- \n 1- Nova York \n 2- Paris \n 3-Tóquio \n Digite o número do destino desejado: "))
passaporte_valido = input("Possui passaporte válido (Sim/Não): ").upper()
orcamento_disponivel = float(input("Digite o orçamento disponível para essa viagem(R$): "))
idade = int(input("Digite a idade de viajante: "))
nota_fluencia = int(input("Digite a nota de fluência do viajante no idioma local (0 a 10): "))
custo_fixo = 0
falha1 = 0
falha2 = 0
falha3 = 0
falha4 = 0
falha5 = 0


if destino_desejado == 1:
    destino_desejado = "Nova York"
    custo_fixo = 10000
elif destino_desejado == 2:
    destino_desejado = "Paris"
    custo_fixo = 12000
else:
    destino_desejado = "Tóquio"
    custo_fixo = 15000

if passaporte_valido != "SIM":
    print("VIAGEM NEGADA: passaporte inválido.")
    falha1 = 1

if destino_desejado == "Tóquio" and idade <18:
    print("VIAGEM NEGADA: idade mínima para o destino não atingida.") 
    falha2 = 1
if destino_desejado == "Paris" and idade <16:
    print("VIAGEM NEGADA: idade mínima para o destino não atingida.") 
    falha2 = 1
if destino_desejado == "Nova York" and idade <16:
    print("VIAGEM NEGADA: idade mínima para o destino não atingida.") 
    falha2 = 1
    
    
if destino_desejado == "Nova York" and orcamento_disponivel < custo_fixo:
    print(f"VIAGEM NEGADA: orçamento de R$ {orcamento_disponivel} é insuficiente para o custo fixo de {destino_desejado} (R$ {custo_fixo}).")
    falha3 = 1
if destino_desejado == "Paris" and orcamento_disponivel < custo_fixo:
    print(f"VIAGEM NEGADA: orçamento de R$ {orcamento_disponivel} é insuficiente para o custo fixo de {destino_desejado} (R$ {custo_fixo}).")
    falha3 = 1
if destino_desejado == "Tóquio" and orcamento_disponivel < 10000:
    print(f"VIAGEM NEGADA: orçamento de R$ {orcamento_disponivel} é insuficiente para o custo fixo de {destino_desejado} (R$ {custo_fixo}).")
    falha3 = 1
    
duracao_maxima = 0
if nota_fluencia > 7:
    duracao_maxima = 90
elif nota_fluencia > 4 and nota_fluencia < 8:
    duracao_maxima = 30
else:
    duracao_maxima = 15
    
if duracao > duracao_maxima:
    print(f"VIAGEM NEGADA: Sua fluência (Nota {nota_fluencia}) permite apenas {duracao_maxima} dias, mas você solicitou {duracao} dias.")
    falha4 = 1
    
saldo_restante = orcamento_disponivel - custo_fixo
custo_diario = saldo_restante / duracao

if custo_diario < 500:
    print(f"VIAGEM NEGADA: Saldo restante insuficiente para manter o custo de R$ 500/dia durante {duracao} dias.")
    falha5 = 1 
    
if (falha1 + falha2 + falha3 + falha4 + falha5) == 0:
    print(f"VIAGEM APROVADA! \n Destino: {destino_desejado}. \n Duração:{duracao} dias. \n Saldo para gastos diários: R$ {custo_diario}.")

if falha1 or falha2 or falha3 or falha4 or falha5 == 1:
    print('VIAGEM CANCELADA! MOTIVO(S):\n')
    if falha1 == 1:
        print(f"Passaporte inválido.")

    if falha2 == 1:
        print(f"Idade mínima para o destino não atingida.")

    if falha3 == 1:
        print(f"Orçamento de R$ {orcamento_disponivel} é insuficiente para o custo fixo de {destino_desejado} (R$ {custo_fixo}).")

    if falha4 == 1:
        print(f"Sua fluência (Nota {nota_fluencia}) permite apenas {duracao_maxima} dias, mas você solicitou {duracao} dias.")

    if falha5 == 1:
        print(f"Saldo restante insuficiente para manter o custo de R$ 500/dia durante {duracao} dias.")

