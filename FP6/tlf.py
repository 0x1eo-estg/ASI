import re

pattern = re.compile(r'^(?P<pri>.*);(?P<tlf>\d{9}$)')
with open("dados.txt") as fp:
	for linha in fp:
		linha = linha.strip()
		print (pattern.sub(r"\g<pri>;00351\g<tlf>", linha)) 