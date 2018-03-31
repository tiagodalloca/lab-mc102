'''O objetivo do problema foi calcular a capacidade atual de um estacionamento,
conhecendo o tamanho do veículo e se ele está entrando ou saindo.'''

#Valores de entrada
c = int(input())
v = int(input())

#Regras e Resultado
while v != 0:
	if v <= c and v > 0:
		c = c - v
		print ("Seja bem-vindo! Capacidade restante:", c)
		v = int(input())
	if v > c:
		print ("Veiculo muito grande! Capacidade restante:", c)
		v = int(input())
	if v < 0:
		c = c - v
		print ("Volte sempre! Capacidade restante:", c)
		v = int(input())

