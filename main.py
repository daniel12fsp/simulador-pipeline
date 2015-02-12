from classes import Processador

def if_estagio():
	#Pega a instrucao do pc
	instrucao = proc.mem_instrucao[proc.regs["pc"]]
	#pc + 2
	proc.regs["pc"] += 2 
	return instrucao 

def if_id_registradores(instrucao):
	#Guarda o registrador em estagio anterior
	return instrucao

def id_estagio(instrucao):
	# Divide a instrucao pelo espaco
	ins = instrucao.split()
	registros = ins.pop()
	ins.extend(registros.split(","))
	print(ins)
	if(proc.tipo(ins[0]) == "r3"):
		rs = proc.regs[ins[2]]
		rt = proc.regs[ins[3]]
		return ins[0], ins[1], rs, rt # rd, rs, rt

	elif(proc.tipo(ins[0]) == "r2"):
		rs = proc.regs[ins[2]]
		return ins[0], ins[1], rs

	elif(proc.tipo(ins[0]) == "j"):
		pass
	#elseif proc.tipo(instrucao) == "i")
	else:
		pass

def id_exmen_registradores(registros):
	return registros

def exmen_estagio(registros):
	
	if(proc.tipo(registros[0])):
	#Executa as instrucoes do tipo R
		func, rd, rs, rt = registros
		resultado = proc.alu.func[func](rs, rt)
	return rd, resultado
	
	#Falta fazer a parte da MEM


def exmen_wb_registradores(rd, resultado):
	return rd, resultado

def wb_estagio(rd, resultado):
	proc.regs[rd] = resultado

proc = Processador("teste2.asm")

while(True):
	instrucao = if_estagio()
	if(instrucao == None):
		break
	instrucao = if_id_registradores(instrucao)
	registros = id_estagio(instrucao)
	registros = id_exmen_registradores(registros)
	rd, resultado = exmen_estagio(registros)
	rd, resultado = exmen_wb_registradores(rd, resultado)
	wb_estagio(rd, resultado)
	print(resultado)

