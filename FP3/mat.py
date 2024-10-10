def read_to_dict():
    with open('mat.txt', 'r') as file:
        data = {}
        for i, line in enumerate(file):
            parts = line.strip().split(';')
            nif, matricula, iuc = parts
            if nif not in data:
                data[nif] = {}
            data[nif][matricula] = iuc
    return data

def search_by_nif():
    data = read_to_dict()
    nif = input('Insira o nif: ')
    if nif in data:
        print(data[nif])
    else:
        print('Não existe nenhum registo com essa matricula')

#print(read_to_dict())

search_by_nif()