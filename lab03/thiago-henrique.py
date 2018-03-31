'''Objetivo criar um programa a fim de calcular a média da prova, média geral e a nota final,
da disciplina MC102'''

#Valores de entrada
P1 = float(input())
P2 = float(input())
Ml = float(input())

#Média das provas
Mp = float((2*P1 + 3*P2)/5)

#Regras do cálculo
if Mp<  5 or Ml < 5:
	if Mp < 4.9:
		M = Mp
	else:
		M = 4.9
else:
	M = float((3*Mp + 2*Ml)/5)

if M < 5 and M >= 2.5:
	E = float(input())
	F = float((M + E)/2)
else:
	F =float(M)
	
#Resultados
print ("%.1f" %Mp)
print ("%.1f" %M)
print ("%.1f" %F)




