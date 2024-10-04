str = "8200123;Ana Maria;931221012;12/05/2000"

lista = str.split(";")
print(lista)
print(len(lista))
lista.append("SOL")

string = ", ".join(lista)
print(string)