def contar_carros_por_nif(ficheiro):
    nif_carros = {}

    with open(ficheiro, 'r') as f:
        linhas = f.readlines()

    for linha in linhas[1:]:  # Ignorar o cabeçalho
        partes = linha.strip().split(';')
        nif = partes[0]

        if nif in nif_carros:
            nif_carros[nif] += 1
        else:
            nif_carros[nif] = 1

    return nif_carros

def iuc_por_nif(ficheiro):
    nif_iuc = {}

    with open(ficheiro, 'r') as f:
        linhas = f.readlines()

    for linha in linhas[1:]:  # Ignorar o cabeçalho
        partes = linha.strip().split(';')
        nif = partes[0]
        iuc = float(partes[2])

        if nif in nif_iuc:
            nif_iuc[nif] += iuc
        else:
            nif_iuc[nif] = iuc

    return nif_iuc

if __name__ == "__main__":
    ficheiro = 'carros.txt'
    resultado = contar_carros_por_nif(ficheiro)
    for nif, contagem in resultado.items():
        print(f"NIF: {nif}, Carros: {contagem}")
    
    for nif, iuc in iuc_por_nif(ficheiro).items():
        print(f"NIF: {nif}, IUC: {iuc}")

