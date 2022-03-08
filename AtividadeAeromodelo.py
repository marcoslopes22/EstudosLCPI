#ETE - PORTO DIGITAL
#PROFESSOR: CLOVES ROCHA
#ALUNO: MARCOS AURÉLIO LOPES DE ARAUJO
#EXERCICIO PRÁTICO AULA 04 - VII III XXII

#EXECUTAR COMANDOS DE CONTROLE/DESCISÃO DE UM AEROMODELO
#(LIGAR, DESLIGAR, ACELERAR, DECOLAR, PLANAR, PILOTO AUTOMÁTICO E POUSAR).

print("--------------------------------------------------------")
print("Bem-vindo ao perfil do aeromodelo. Siga as teclas de comando:\n\nTeclas de comando:\n1. Acelerar\n2. Decolar\n3. Planar\n4. Piloto automatico\n5. Pousar\n9. Ligar\n0. Desligar")

ligado = False

while (ligado == False):

    escolher = int(input("\nPressione > 9 < para ligar: "))

    if escolher == 9:
        ligado = True
        print("Sistema ligado com sucesso...")
    elif (escolher == 1) or (escolher == 2) or (escolher == 3) or (escolher == 4) or (escolher == 5) or (escolher == 0):
        print("Sistema desligado. Por favor, pressione > 9 < para ligar.")
    else:
        print("Erro. Este comando não existe. Por favor, verifique as teclas de comando.")


    while (ligado == True):

        escolher = int(input("\nPressione uma tecla de comando para executar uma ação: "))

        if (escolher == 1):
            print("Acelerando...")
        elif escolher == 2:
            print("Decolando...")
        elif escolher == 3:
            print("Planando...")
        elif escolher == 4:
            print("Piloto automático...")
        elif escolher == 5:
            print("Pousando...")
        elif escolher == 0:
            print("\nDesligando o sistema...\nSistema desligado com sucesso.")
            ligado = False
        elif escolher == 9:
            print("Sistema ligado. Por favor, pressione uma tecla de comando para executar uma ação: ")
        else:
            print("Erro. Esse comando não existe. Por favor, verifique as teclas de comando.")
