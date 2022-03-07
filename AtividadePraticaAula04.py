#ETE PORTO DIGITAL
#PROFESSOR: CLOVES ROCHA
#ALUNO: MARCOS ALURELIO LOPES DE ARAUJO
#ATIVIADE PRÁTICA - AULA 04 - VII/III/XXII

#EXECUTAR COMANDOS DE CONTROLE/DESCISÃO DE UM AEROMODELO(ACELERAR, DECOLAR, PLANAR, PILOTO AUTOMÁTICO, POUSAR E DESLIGAR).

print("Teclas de comando:\n1: acelerar.\n2: decolar.\n3: planar.\n4: piloto automatico.\n5: pousar.")

ligado = True

while (ligado):
  escolher = int(input("Digite um número para executar uma ação no aeromoodelo: "))

  if (escolher == 1):
    print("Acererando")
  elif escolher == 2:
    print("decolando")
  elif escolher == 3:
    print("planando")
  elif escolher == 4:
    print("piloto automático")
  elif escolher == 5:
    print("pousando")
  elif escolher == 0:
    print("desligando o sistema")