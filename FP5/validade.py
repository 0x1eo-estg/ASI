import re

cc = input("Introduzir nº de cartão de cidadão: ")

pattern = re.compile(r'^\d{8}\s\d\s[A-Z]{2}\d$')

if pattern.match(cc):
    print("Cartão de cidadão válido")
else:
    print("Cartão de cidadão inválido")