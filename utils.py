import re

def carregar_instrucoes(nome_arq):
	texto = open(nome_arq).read()
	texto = re.sub(";.*\n", "\n", texto)
	texto = re.sub("\n+", "\n", texto.strip())
	return texto.splitlines()

