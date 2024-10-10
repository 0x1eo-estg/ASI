def ler_ficheiro_para_hashtables():
    veiculos = {}
    imoveis = {}

    with open('veimo.txt', 'r') as f:
        reader = (line.strip().split(';') for line in f)
        for row in reader:
            nif = row[0]
            matricula = row[2]
            valor_iuc = row[3]
            artigo_matricial = row[4]
            valor_imi = row[5]

            if matricula:
                if nif not in veiculos:
                    veiculos[nif] = {}
                veiculos[nif][matricula] = valor_iuc
            if artigo_matricial:
                if nif not in imoveis:
                    imoveis[nif] = {}
                imoveis[nif][artigo_matricial] = valor_imi

    return veiculos, imoveis

veiculos, imoveis = ler_ficheiro_para_hashtables()

print("Veículos:", veiculos)
print("Imóveis:", imoveis)

def nif_mais_taxa_imi(imoveis):
    max_nif = None
    max_valor_imi = 0

    for nif, artigos in imoveis.items():
        total_imi = sum(float(valor) for valor in artigos.values())
        if total_imi > max_valor_imi:
            max_valor_imi = total_imi
            max_nif = nif

    return max_nif, max_valor_imi

nif, valor_imi = nif_mais_taxa_imi(imoveis)
print(f"O NIF que pagou mais taxa IMI é {nif} com um total de {valor_imi:.2f} euros.")

def imposto_total_por_nif(veiculos, imoveis):
    total_por_nif = {}

    for nif, veiculo in veiculos.items():
        total_por_nif[nif] = sum(float(valor) for valor in veiculo.values())

    for nif, imovel in imoveis.items():
        if nif in total_por_nif:
            total_por_nif[nif] += sum(float(valor) for valor in imovel.values())
        else:
            total_por_nif[nif] = sum(float(valor) for valor in imovel.values())

    return total_por_nif

total_por_nif = imposto_total_por_nif(veiculos, imoveis)
print("Total de imposto por NIF:", total_por_nif)