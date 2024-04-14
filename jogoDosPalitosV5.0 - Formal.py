from random import randint

# ====================== VARIAVEIS ======================
Barreira = 0
# Variavel pro sistema de começo
Numero_1 = 0
Numero_2 = 0
Numero_3 = 0
Numero_4 = 0
Numero_5 = 0
# Variaveis com os numeros que seram usados ou não
Lista_Geral = []
# Uma lista pra colocar todos os numeros das colunas

# ====================== PREPARAÇÃO I ======================
Quantidade_de_Colunas = int(input("Quantas colunas(MAX: 5): "))
# Pra saber quantas colunas o usuario quer

# Loop que vai recolher os numeros:
for ns in range(Quantidade_de_Colunas):
    Palitos = input("Qual vai ser o numero de palitos da {}ª coluna?(MAX: 31): ".format(ns + 1))
    Lista_Geral.append(int(Palitos))
    # Coloca os numeros digitados na lista geral

Lista_Geral.sort()
# Coloca a lista geral em ordem crescente, para ficar mais bonito e organizado

for cs in range(Quantidade_de_Colunas):
    if cs + 1 == 1:
        Numero_1 = int(Lista_Geral[0])
    if cs + 1 == 2:
        Numero_2 = int(Lista_Geral[1])
    if cs + 1 == 3:
        Numero_3 = int(Lista_Geral[2])
    if cs + 1 == 4:
        Numero_4 = int(Lista_Geral[3])
    if cs + 1 == 5:
        Numero_5 = int(Lista_Geral[4])
# Coloca os valores nas variaveis/colunas

# Função que coloca só as colunas que o usuario escolheu na lista, pro codigo ficar mais bonito:
def Numeros(Quantidade_de_Colunas, Numero_1, Numero_2, Numero_3, Numero_4, Numero_5):
    Lista_Geral = []
    for s in range(Quantidade_de_Colunas):
        if s + 1 == 1:
            Lista_Geral += [Numero_1]
        if s + 1 == 2:
            Lista_Geral += [Numero_2]
        if s + 1 == 3:
            Lista_Geral += [Numero_3]
        if s + 1 == 4:
            Lista_Geral += [Numero_4]
        if s + 1 == 5:
            Lista_Geral += [Numero_5]
    return Lista_Geral


# ====================== PREPARAÇÃO II ======================
print("Inicio do Jogo:")
print(Numero_1 * '|', Numero_2 * '|', Numero_3 * '|', Numero_4 * "|", Numero_5 * "|")
for d in Lista_Geral:
    print(d, end=" ")
print("")
print("=-=-=-=-=-=-=-=-=-=-=")

print("Cara ou Coroa para ver quem começa")
escolha = str(input('Voce escolhe Cara ou Coroa?: '))
resultado = randint(0, 1)
if escolha == "Cara" or escolha == "cara":
    escolha_da_maquina = "Coroa"
else:
    escolha_da_maquina = "Cara"
print("Você escolheu {}, então escolho {}".format(escolha, escolha_da_maquina))
if resultado == 0:
    if "Cara" in escolha_da_maquina:
        print("Deu cara, eu começo!")
    else:
        print("Deu cara, voce começa!")
        Barreira = 1
else:
    if "Coroa" in escolha_da_maquina:
        print("Deu coroa, eu começo!")
    else:
        print("Deu coroa, voce começa!")
        Barreira = 1


# ====================== O CEREBRO ======================
# Uma função para analisar o numero que satisfaz a coluna para que ela seja segura:
def analise(Lista_x):
    Testador_1 = Lista_x[0]
    Testador_2 = Lista_x[1]
    Testador_3 = Lista_x[2]
    Testador_4 = Lista_x[3]
    Testador_5 = Lista_x[4]
    # As variaveis que vão testar se o 1ª numero vai ser modificado
    # Cada coluna tem sua devida variavel
    if Chave_1 != 2:
        if Lista_x[0] == 1:
            Testador_1 = 0
        if Lista_x[0] == 0:
            Testador_1 = 1
    if Chave_2 != 2:
        if Lista_x[1] == 1:
            Testador_2 = 0
        if Lista_x[1] == 0:
            Testador_2 = 1
    if Chave_3 != 2:
        if Lista_x[2] == 1:
            Testador_3 = 0
        if Lista_x[2] == 0:
            Testador_3 = 1
    if Chave_4 != 2:
        if Lista_x[3] == 1:
            Testador_4 = 0
        if Lista_x[3] == 0:
            Testador_4 = 1
    if Chave_5 != 2:
        if Lista_x[4] == 1:
            Testador_5 = 0
        if Lista_x[4] == 0:
            Testador_5 = 1
    # Caso a chave for impar ele troca o algarismo pelo oposto(se for 1 muda pra 0 e ao contrario), isso faz com que a chave vire par
    Resposta_x = Testador_1 * 16 + Testador_2 * 8 + Testador_3 * 4 + Testador_4 * 2 + Testador_5
    # Trasforma o numero de decimal para binario
    return Resposta_x


# ====================== O CORPO ======================
# Um loop que para só quando todas as colunas estiverem zeradas
while sum(Lista_Geral) != 0:
    Barreira += 1
    if Barreira != 1:
        Coluna = input("Qual coluna?: ")
        Palitos_Cortados = int(input("Quer retirar quantos palitos?: "))
    # Pergunta qual coluna o usuario vai jogar e quantos palitos ira retirar da mesma
        if Coluna == "1":
            Numero_1 = Numero_1 - Palitos_Cortados
        if Coluna == "2":
            Numero_2 = Numero_2 - Palitos_Cortados
        if Coluna == "3":
            Numero_3 = Numero_3 - Palitos_Cortados
        if Coluna == "4":
            Numero_4 = Numero_4 - Palitos_Cortados
        if Coluna == "5":
            Numero_5 = Numero_5 - Palitos_Cortados
        # Atualiza o valor da coluna

        # SETOR DO PLAYER
        Lista_Geral = Numeros(Quantidade_de_Colunas, Numero_1, Numero_2, Numero_3, Numero_4, Numero_5)

        print("PLAYER JOGOU:")
        print(Numero_1 * '|', Numero_2 * '|', Numero_3 * '|', Numero_4 * "|", Numero_5 * "|")
        for d in Lista_Geral:
            print(d, end=" ")
        print("")
        # Mostra a jogada do usuario

    Numero_Binario_1 = '%05d' % int(bin(Numero_1)[2:])
    Numero_Binario_2 = '%05d' % int(bin(Numero_2)[2:])
    Numero_Binario_3 = '%05d' % int(bin(Numero_3)[2:])
    Numero_Binario_4 = '%05d' % int(bin(Numero_4)[2:])
    Numero_Binario_5 = '%05d' % int(bin(Numero_5)[2:])
    # Transforma os numeros em binario
    # Exemplo 00010

    Lista_1 = [int(Numero_Binario_1[0]), int(Numero_Binario_1[1]), int(Numero_Binario_1[2]), int(Numero_Binario_1[3]), int(Numero_Binario_1[4])]
    Lista_2 = [int(Numero_Binario_2[0]), int(Numero_Binario_2[1]), int(Numero_Binario_2[2]), int(Numero_Binario_2[3]), int(Numero_Binario_2[4])]
    Lista_3 = [int(Numero_Binario_3[0]), int(Numero_Binario_3[1]), int(Numero_Binario_3[2]), int(Numero_Binario_3[3]), int(Numero_Binario_3[4])]
    Lista_4 = [int(Numero_Binario_4[0]), int(Numero_Binario_4[1]), int(Numero_Binario_4[2]), int(Numero_Binario_4[3]), int(Numero_Binario_4[4])]
    Lista_5 = [int(Numero_Binario_5[0]), int(Numero_Binario_5[1]), int(Numero_Binario_5[2]), int(Numero_Binario_5[3]), int(Numero_Binario_5[4])]
    # Faz uma lista de cada numero separando os algarismo
    # Pra poder manipular mais facilmente
    # Exemplo [0, 0, 0, 1, 0]
    # Verifica as chaves:
    if (Lista_1[0] + Lista_2[0] + Lista_3[0] + Lista_4[0] + Lista_5[0]) % 2 == 0:
        Chave_1 = 2
    else:
        Chave_1 = 0
    if (Lista_1[1] + Lista_2[1] + Lista_3[1] + Lista_4[1] + Lista_5[1]) % 2 == 0:
        Chave_2 = 2
    else:
        Chave_2 = 0
    if (Lista_1[2] + Lista_2[2] + Lista_3[2] + Lista_4[2] + Lista_5[2]) % 2 == 0:
        Chave_3 = 2
    else:
        Chave_3 = 0
    if (Lista_1[3] + Lista_2[3] + Lista_3[3] + Lista_4[3] + Lista_5[3]) % 2 == 0:
        Chave_4 = 2
    else:
        Chave_4 = 0
    if (Lista_1[4] + Lista_2[4] + Lista_3[4] + Lista_4[4] + Lista_5[4]) % 2 == 0:
        Chave_5 = 2
    else:
        Chave_5 = 0
    # O else ta ali pra ser mais otimizado, pra usar esse bloco em todas as rodadas(se não, ia ser necessario zerar todos as chaves toda rodada)

    # SETOR DA COLUNA 1
    Resposta_1 = analise(Lista_1)
    if Resposta_1 < Numero_1:
        Numero_1 = Resposta_1
        Lista_Geral = Numeros(Quantidade_de_Colunas, Numero_1, Numero_2, Numero_3, Numero_4, Numero_5)
        print("MAQUINA JOGOU:")
        print(Resposta_1 * '|', Numero_2 * '|', Numero_3 * '|', Numero_4 * "|", Numero_5 * "|")
        for d in Lista_Geral:
            print(d, end=" ")
        print("")
        continue
    # Verifica se o numero pode ser modificado, é necessario porque um numero não pode mudar para maior que ele

    # SETOR DA COLUNA 2
    Resposta_2 = analise(Lista_2)
    if Resposta_2 < Numero_2:
        Numero_2 = Resposta_2
        Lista_Geral = Numeros(Quantidade_de_Colunas, Numero_1, Numero_2, Numero_3, Numero_4, Numero_5)
        print("MAQUINA JOGOU:")
        print(Numero_1 * '|', Resposta_2 * '|', Numero_3 * '|', Numero_4 * "|", Numero_5 * "|")
        for d in Lista_Geral:
            print(d, end=" ")
        print("")
        continue

    # SETOR DA COLUNA 3
    Resposta_3 = analise(Lista_3)
    if Resposta_3 < Numero_3:
        Numero_3 = Resposta_3
        Lista_Geral = Numeros(Quantidade_de_Colunas, Numero_1, Numero_2, Numero_3, Numero_4, Numero_5)
        print("MAQUINA JOGOU:")
        print(Numero_1 * '|', Numero_2 * '|', Resposta_3 * '|', Numero_4 * "|", Numero_5 * "|")
        for d in Lista_Geral:
            print(d, end=" ")
        print("")
        continue

    # SETOR DA COLUNA 4
    Resposta_4 = analise(Lista_4)
    if Resposta_4 < Numero_4:
        Numero_4 = Resposta_4
        Lista_Geral = Numeros(Quantidade_de_Colunas, Numero_1, Numero_2, Numero_3, Numero_4, Numero_5)
        print("MAQUINA JOGOU:")
        print(Numero_1 * '|', Numero_2 * '|', Numero_3 * '|', Resposta_4 * "|", Numero_5 * "|")
        for d in Lista_Geral:
            print(d, end=" ")
        print("")
        continue

    # SETOR DA COLUNA 5
    Resposta_5 = analise(Lista_5)
    if Resposta_5 < Numero_5:
        Numero_5 = Resposta_5
        Lista_Geral = Numeros(Quantidade_de_Colunas, Numero_1, Numero_2, Numero_3, Numero_4, Numero_5)
        print("MAQUINA JOGOU:")
        print(Numero_1 * '|', Numero_2 * '|', Numero_3 * '|', Numero_4 * "|", Resposta_5 * "|")
        for d in Lista_Geral:
            print(d, end=" ")
        print("")
        continue
