import bisect
import utils
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

	def __getitem__(self, index):
		return self.regs[index]

	def	__setitem__(self, index, valor):
		self.regs[index] = valor 

class Memoria():
	def __init__(self, qtd_max):
		self.qtd_max = qtd_max
		self.dados = [None] * qtd_max

	def __getitem__(self, end_hex):
		endereco = int(str(end_hex), base=16)
		if(len(self.dados) < endereco):
			return None
		else:
			return self.dados[endereco]

	def carregar_instrucoes(self, nome_do_arquivo):
		self.dados = utils.carregar_instrucoes(nome_do_arquivo)
		
class ALU():
	def __init__(self):
		self.func = {
			#Inicio - Instrucoes do Tipo R com tres registradores 
			"add" : lambda x,y: x+y,
			"addinc" : lambda x,y: x+y+1,
			"and" : lambda x,y: x & y,
			"andnota" : lambda x,y: (~x) & y, 
			"nand" : lambda x,y: ~(x & y),
			"nor": lambda x,y: ~(x | y),
			"or": lambda x,y: x | y,
			"ornotb": lambda x,y: x | (~y),
			"sub": lambda x,y: x - y,
			"subdec": lambda x,y: x - y - 1,
			"xnor": lambda x,y: !(x ^ y),
			"xor": lambda x,y: x ^ y,
			#Fim - Instrucoes do Tipo R com tres registradores 
			#Inicio - Instrucoes do Tipo R com dois registradores 
			"asl": lambda y: y << 1,
			"asr": lambda y: y >> 1,
			"deca": lambda y: y-1,
			"inca": lambda y: y+1,
			"lsl": lambda y: None,
			"lsr": lambda y:None
			#Fim - Instrucoes do Tipo R com dois registradores 
		}

class Processador():
	def __init__(self, nome_arq):
		self.mem_instrucao = Memoria(64)
		self.mem_instrucao.carregar_instrucoes(nome_arq)
		self.mem_dados = Memoria(64)
		self.regs = Registradores()
		self.alu = ALU()
	


	
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
