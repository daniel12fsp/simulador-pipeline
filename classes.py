import bisect
import utils

class Flags():
	def __init__(self):
		self.flags = {
					"neg":0,
					"zero":0,
					"carry":0,
					"negzero":0,
					"overflow":0
				}

	def __getitem__(self, index):
		return self.regs[index]

	def	__setitem__(self, index, valor):
		self.regs[index] = valor 
	
	def items(self):
		return self.flags.items()

class Registradores():
	def __init__(self):
		self.regs = {
					"r0":0,
					"r1":0,
					"r2":0,
					"r3":0,
					"r4":0,
					"r5":0,
					"r6":0,
					"r7":0,
					"ra":0,
					"pc":0,
					"fp":0,
					"sp":0
				}
	def key(self, key):
		return key.replace("$", "")

	def ler(self, reg):
		reg = self.key(reg)
		return self.regs[reg]

	def	escrever(self, reg, valor):
		reg = self.key(reg)
		self.regs[reg] = valor 

	def items(self):
		return self.regs.items()

class Memoria():
	def __init__(self, qtd_max):
		self.qtd_max = qtd_max
		self.dados = [None] * qtd_max

	def __getitem__(self, endereco):
		if(len(self.dados) > endereco/2):
			return self.dados[endereco/2]
		else:
			return None

	def carregar_instrucoes(self, nome_do_arquivo):
		self.dados = utils.carregar_instrucoes(nome_do_arquivo)
	
	def __repr__(self):
		return str(self.dados)
		
class ALU():
	def __init__(self):
		self.funcs = {
			#Inicio - Instrucoes do Tipo R com tres registradores 
			"add" : lambda (x,y): x+y,
			"addinc" : lambda (x,y): x+y+1,
			"and" : lambda (x,y): x & y,
			"andnota" : lambda (x,y): (~x) & y, 
			"nand" : lambda (x,y): ~(x & y),
			"nor": lambda (x,y): ~(x | y),
			"or": lambda (x,y): x | y,
			"ornotb": lambda (x,y): x | (~y),
			"sub": lambda (x,y): x - y,
			"subdec": lambda (x,y): x - y - 1,
			"xnor": lambda (x,y): ~(x ^ y),
			"xor": lambda (x,y): x ^ y,
			#Fim - Instrucoes do Tipo R com tres registradores 
			#Inicio - Instrucoes do Tipo R com dois registradores 
			"asl": lambda (y): y << 1,
			"asr": lambda (y): y >> 1,
			"deca": lambda (y): y-1,
			"inca": lambda (y): y+1,
			"lsl": lambda (y): None,
			"lsr": lambda (y):None
			#Fim - Instrucoes do Tipo R com dois registradores 
		}
		
	def exec_funcao(self, func, regs):
		
		if(self.funcs.get(func, None) != None):
			#print(func ,tuple(arg for arg in regs))
			return self.funcs[func](arg for arg in regs)
			

class Processador():
	def __init__(self, nome_arq):
		self.mem_instrucao = Memoria(64)
		self.mem_instrucao.carregar_instrucoes(nome_arq)
		self.mem_dados = Memoria(64)
		self.regs = Registradores()
		self.alu = ALU()
		self.flags = Flags()
	


	
	def tipo(self, instrucao):
		#Falta colocar a instrucao 'ones' e zeros
		r2 = ["asl","asr","deca","inca","lsl", "lsr"]

		if(index(r2, instrucao)):
			return "r2"

		i = ["store", "load"]
		if(index(i, instrucao)):
			return "i"

		j = ["j", "jal", "jf.cond", "jr"]
		if(index(j, instrucao)):
			return "j"
		else:
			return "r3" #tipo r

		#r3 = ["add","addinc","and","andnota","nand","nor","or","ornotb","sub","subdec","xnor","xor"]
def index(a, x):
	'Locate the leftmost value exactly equal to x'
	i = bisect.bisect_left(a, x)
	if i != len(a) and a[i] == x:
		return True
	return False
