def ler():
    data = {}
    with open('inquieta.txt', 'r') as file:
        for i, line in enumerate(file):
            if i == 0:
                continue
            parts = line.strip().split(';')
            id, category, _, _, valor_anual, data_fim = parts
            if id not in data:
                data[id] = {}
            data[id][category] = {
                "valor_anual": valor_anual,
                "data_fim": data_fim
            }
    return data

def format_data(data, indent=0):
    result = ""
    indent_str = " " * indent
    if isinstance(data, dict):
        result += "{\n"
        for key, value in data.items():
            result += f'{indent_str}    "{key}": {format_data(value, indent + 4)},\n'
        result = result.rstrip(",\n") + "\n" + indent_str + "}"
    elif isinstance(data, list):
        result += "[\n"
        for item in data:
            result += f'{indent_str}    {format_data(item, indent + 4)},\n'
        result = result.rstrip(",\n") + "\n" + indent_str + "]"
    else:
        result += f'"{data}"'
    return result

data = ler()
print(format_data(data))