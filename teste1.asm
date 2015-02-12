; Nome deste programa: TESTE1.ASM
.module m0
.pseg
.global _soma; exporting
; ---- PROLOGUE for _soma ----
; framesize=5, argbuildsize=0
; aqui devem ser colocadas instruções para inicialização
loadlit r4,5
;create new stack frame
sub sp,sp,r4
loadlit r4,0
;save the old frame pointer
add r4,r4,sp
store r4,fp
or fp,sp,sp
; and create new one
loadlit r4,0
add fp,fp,r4
; with proper offset.
loadlit r4,1
add r4,r4,fp
store r4,ra
; save the return address
loadlit r4,2
add r4,r4,fp
store r4,r1
; save regs
; ---- END PROLOGUE ----
loadlit r4,5
add r4,fp,r4
load r0,r4
; INDIR (reg1) via r4
loadlit r4,7
add r4,fp,r4
load r1,r4
; INDIR (reg2) via r4
add r0,r0,r1
L1:
; ---- EPILOGUE ----
loadlit r4,2
add r4,r4,fp
load r1,r4
; restore regs

inca r4,fp
load ra,r4
; restore return addr
load fp,fp
; restore old fp
loadlit r4,5
; discard old stack frame
add sp,sp,r4
jr ra
; and return
; ---- END EPILOGUE ----
.dseg 1
L3:
; resultado
.const 8
.dseg 3
L4:
; teste
.blk
1
; reserve an 1-word block
.pseg
.global _main; exporting
; ---- PROLOGUE for _main ----
; framesize=13, argbuildsize=4
loadlit r4,13
;create new stack frame
sub sp,sp,r4
loadlit r4,8
;save the old frame pointer
add r4,r4,sp
store r4,fp
or fp,sp,sp
; and create new one
loadlit r4,8
add fp,fp,r4
; with proper offset.
loadlit r4,1
add r4,r4,fp
store r4,ra
; save the return address
loadlit r4,2
add r4,r4,fp
store r4,r1
; save regs
; ---- END PROLOGUE ----
loadlit r1,500
loadlit r4,-2
add r4,r4,fp
store r4,r1
; ASGNP (a) via r4
lcl r1, LOWBYTE 10000
lch r1, HIGHBYTE 10000
loadlit r4,-4
add r4,r4,fp
store r4,r1
; ASGNP (b) via r4
loadlit r4,-2
add r4,fp,r4
load r0,r4
; INDIR (a) via r4
loadlit r4, 0
add r4,r4,sp
store r4,r0
loadlit r4,-4
add r4,fp,r4
load r0,r4
; INDIR (b) via r4
loadlit r4, 2
add r4,r4,sp
store r4,r0
lcl r0,LOWBYTE _soma
lch r0,HIGHBYTE _soma
jal r0 ; _soma
lcl r1,LOWBYTE L3
lch r1,HIGHBYTE L3
store r1,r0
L2:
; ---- EPILOGUE ----
loadlit r4,2
add r4,r4,fp
load r1,r4
; restore regs
inca r4,fp
load ra,r4
; restore return addr
load fp,fp
; restore old fp
loadlit r4,13
; discard old stack frame
add sp,sp,r4
HALT:
j HALT
; ---- END EPILOGUE ----
.end
