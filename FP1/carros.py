dados = [
    "123456789;12-AZ-21;35.00",
    "134676523;34-NU-24;45.00",
    "123456789;01-ON-99;135.00",
    "272729193;00-13-RZ;38.00",
    "726248277;22-DR-87;45.00",
    "134676523;42-AT-12;25.00"
]

contagem_carros = {}
iuc_por_nif = {}

for linha in dados:
    nif, matricula, iuc = linha.split(';')
    if nif in contagem_carros:
        contagem_carros[nif] += 1
    else:
        contagem_carros[nif] = 1

    iuc = float(iuc)

    if nif in iuc_por_nif:
        iuc_por_nif[nif] += iuc
    else:
        iuc_por_nif[nif] = iuc

for nif, count in contagem_carros.items():
    print(f"NIF {nif} tem {count} carro(s).")

for nif, total_iuc in iuc_por_nif.items():
    print(f"NIF {nif} tem um total de IUC de {total_iuc:.2f} euros.")