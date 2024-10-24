import re

str="Ana Almeida Da Silva"
#str="AnA Almeida Da Silva"
#str="Ana Almeida da Silva"
#str="Ana Almeida da silva"

pattern = re.compile(r'^[A-Z][a-z]+(\s[A-Z][a-z]+)*$')
if pattern.match(str):
	print ("Nome valido")
else:
	print ("Nome invalido")