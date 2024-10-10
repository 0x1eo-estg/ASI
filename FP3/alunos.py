def load_hash():
    with open('alunos.txt', 'r') as file:
        data = {}
        for i, line in enumerate(file):
            parts = line.strip().split(';')
            id, nome, idade, sexo, num = parts
            if sexo == 'F':
                data[id] = {
                    "nome": nome,
                    "idade": idade,
                    "sexo": sexo,
                    "num": num
                }
    return data

def search_by_id():
    data = load_hash()
    id = input('Insira o id: ')
    if id in data:
        print(data[id])
    else:
        print('Não existe nenhum registo com esse id')

def calculate_avg_age():
    data = load_hash()
    ages = [int(values['idade']) for values in data.values()]
    return sum(ages) / len(ages)

print(load_hash())