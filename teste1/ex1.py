full_name = input("Nome: ")
dominio = "asi24.pt"
names = full_name.split()

pri_nome = names[0]
pen_nome = names[-2]
ult_nome = names[-1]
email = f"{pri_nome}.{pen_nome[0]}.{ult_nome}@{dominio}".lower()
print(f"O seu email é: {email}")