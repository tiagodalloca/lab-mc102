# thomas (Desnord)

# objetivo: auxiliar o gerenciamento de um estacionamento

# entrada: capacidade do estacionamento, sequencia de valores
# que representam o tamanho do veiculo

# saida: resposta dada a cada veiculo que tenta entrar
# ou sair do estacionamento

c = int(input()); # pega a capacidade do estacionamento
x = -1;
while(x != 0): # enquanto nao finaliza a leitura da sequencia
 x = int(input()); # lê um valor da sequencia
 if(x > 0): # se o veiculo esta tentando entrar
   if((c-x) >= 0): # se o veiculo cabe no estacionamento
    c = c - x; # deixa ele entrar, subtraindo o tamanho na capacidade
    print("Seja bem-vindo! Capacidade restante: %d" %c);
   else: # caso o estacionamento estiver lotado
    print("Veiculo muito grande! Capacidade restante: %d" %c);
 elif(x < 0): # se um veiculo esta saindo do estacionamento
  c = c + abs(x); # aumenta a capacidade de acordo com
                  # o tamanho do veiculo que saiu
  print("Volte sempre! Capacidade restante: %d" %c);
