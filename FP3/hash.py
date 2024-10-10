def get_values():
    data = {}
    with open ('input.txt', 'r') as input:
        for i, line in enumerate(input):
            parts = line.strip().split(';')
            id, nome, _, _, _ = parts
            data[id] = {
                "valor": nome,
            }
    return data

def search_by_id():
    data = get_values()
    id = input('Insira o id: ')
    if id in data:
        print(data[id])
    else:
        print('Não existe nenhum registo com esse id')

def save_to_file(data):
    with open('output.txt', 'w') as output:
        for id, values in data.items():
            output.write(f'{id};{values["nome"]};{values["idade"]};{values["sexo"]};{values["num"]}\n')

print(get_values())
#save_to_file(get_values())

search_by_id()