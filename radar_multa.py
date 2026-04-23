vel_carro=int(input("Digite a velocidade do carro: "))
tipo_via=int(input("Tipo de via, urbana = 1, rodovia = 2, escolar = 3: "))

multa = (vel_carro - 60) /100

if tipo_via == 2:
    if multa <= 0.2:
        print("Multa Leve.")
    elif multa <= 0.50:
        print("Multa Grave.")
    else:
        print("Multa Gravíssima e Suspensão de Carteira.")

if tipo_via == 1:
    if multa <= 0.2:
        print("Multa Leve.")
    elif multa <= 0.50:
        print("Multa Grave.")
    else:
        print("Multa Gravíssima e Suspensão de Carteira.")

if tipo_via == 3:
    if multa <= 0.2:
        print("Multa Leve.")
    elif multa <= 0.50:
        print("Multa Grave.")
    else:
        print("Multa Gravíssima e Suspensão de Carteira.")
