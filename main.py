from classes import Processador
import utils

def if_estagio():
	#Pega a instrucao de endereco armazenado em pc
	pc = proc.regs.ler("pc")
	instrucao = proc.mem_instrucao[pc]
	#pc + 2
	proc.regs.escrever("pc", pc + 2)
	return instrucao 

def if_id_registradores(instrucao):
	#Guarda o registrador em estagio anterior
	return instrucao

def id_estagio(instrucao):
	# Divide a instrucao pelo espaco
	ins = instrucao.replace(",","").split()
	func = ins.pop(0)
	regs = ins
	print("Tipo:", proc.tipo(func))
	if(proc.tipo(func) == "r3"):
		rd = regs[0]
		rs = proc.regs.ler(regs[1])
		rt = proc.regs.ler(regs[2])
		return func, [rd ,rs, rt] # funct, rd, rs, rt

	elif(proc.tipo(func) == "r2"):
		rd = regs[0]
		rs = proc.regs.ler(regs[1])
		return func, [rd, rs] # funct, rd, rs

	elif(proc.tipo(func) == "r1"):
		rd = proc.regs.ler(regs[0])
		return func, [rd]

	elif(proc.tipo(func) == "j"):
		pass
	#elseif proc.tipo(instrucao) == "i")
	else:
		pass

def id_exmen_registradores(func, regs):
	return func, regs

def exmen_estagio(func, regs):
	#Parte ULA!
	rd = regs.pop(0)
	resultado = proc.alu.exec_funcao(func, regs)
	return rd, resultado

	#Falta fazer a parte da MEM


def exmen_wb_registradores(rd, resultado):
	return rd, resultado

def wb_estagio(rd, resultado):
	proc.regs.escrever(rd, resultado)

proc = Processador("teste2.asm")

while(True):
	instrucao = if_estagio()
	if(instrucao == None):
		break
	instrucao = if_id_registradores(instrucao)
	func, registros = id_estagio(instrucao)
	func, registros = id_exmen_registradores(func, registros)
	rd, resultado = exmen_estagio(func, registros)
	rd, resultado = exmen_wb_registradores(rd, resultado)
	wb_estagio(rd, resultado)
	utils.imprimir_registradores(proc)

