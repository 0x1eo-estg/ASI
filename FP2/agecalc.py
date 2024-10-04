from datetime import datetime

def classificar_idade(data_nascimento):
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    hoje = datetime.today()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

    if idade <= 12:
        return "criança"
    elif 13 <= idade <= 17:
        return "juvenil"
    elif 18 <= idade <= 64:
        return "adulto"
    else:
        return "sénior"

data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
classificacao = classificar_idade(data_nascimento)
print(f"A classificação etária é: {classificacao}")