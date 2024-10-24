import re

pattern = re.compile(r'^(?P<nome>.*);(?P<idade>.*)$')
with open("dados2.txt") as fp:
	for linha in fp:
		linha = linha.strip()
		matchObj = pattern.match(linha)
		if (int(matchObj.group('idade')) < 18):
			print (matchObj.group('nome'), "Menor")
		if (int(matchObj.group('idade')) >= 18 and int(matchObj.group('idade')) < 65):
			print (matchObj.group('nome'), "Maior")
		if (int(matchObj.group('idade')) >= 65):
			print (matchObj.group('nome'), "Senior")