from __future__ import print_function
import re


def carregar_instrucoes(nome_arq):
	texto = open(nome_arq).read()
	texto = re.sub(";.*\n", "\n", texto)
	texto = re.sub("\n+", "\n", texto.strip())
	return texto.splitlines()

def imprimir_registradores(proc):
	print("-"*71)
	print("\t\tStatus do processador")
	print("\t\tREGISTRADORES\t\tFlags")
	flags = proc.flags.items()
	for (chave, valor) in sorted(proc.regs.items()):
		print("\t\t%s=%0.5d" % (chave,valor), end="")
		if(flags != []):
			flag = flags.pop(0)
			print("\t\t\t%8s=%1d" % (flag[0], flag[1]), end="")
		print()
	
	print(proc.mem_instrucao[proc.regs.ler("pc") - 2])
		
	print("-"*71)
