
con = 0
# Variavel só pro computador saber que sera a primeira jogada
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
ng = []
# Uma lista pra colocar todos os numeros das colunas
cm = int(input("Quantas colunas(MAX: 5): "))
# Pra saber quantas colunas o usuario quer


# Loop que vai pegar os numeros:
for ns in range(cm):
    n = input("Qual vai ser o numero de palitos da {}ª coluna?(MAX: 31): ".format(ns + 1))
    ng.append(int(n))
    # Coloca os numeros digitados na lista geral

ng.sort()
# Coloca a lista geral em ordem crescente, pra ficar mais bonito e organizado

for cs in range(cm):
    if cs + 1 == 1:
        n1 = int(ng[0])
    if cs + 1 == 2:
        n2 = int(ng[1])
    if cs + 1 == 3:
        n3 = int(ng[2])
    if cs + 1 == 4:
        n4 = int(ng[3])
    if cs + 1 == 5:
        n5 = int(ng[4])
# Coloca os valores nas variaveis

# Função que coloca só as colunas que o usuario escolheu na lista, pro codigo ficar mais bonito:
def nums(cm, n1, n2, n3, n4, n5):
    ng = []
    for s in range(cm):
        if s + 1 == 1:
            ng += [n1]
        if s + 1 == 2:
            ng += [n2]
        if s + 1 == 3:
            ng += [n3]
        if s + 1 == 4:
            ng += [n4]
        if s + 1 == 5:
            ng += [n5]
    return ng

# Uma função para analisar o numero que satisfaz a coluna para que ela seja segura:
def analise(lisx):
    t1 = lisx[0]
    t2 = lisx[1]
    t3 = lisx[2]
    t4 = lisx[3]
    t5 = lisx[4]
    # As variaveis que vão testar se o 1ª numero vai ser modificado
    if k1 != 2:
        if lisx[0] == 1:
            t1 = 0
        if lisx[0] == 0:
            t1 = 1
    if k2 != 2:
        if lisx[1] == 1:
            t2 = 0
        if lisx[1] == 0:
            t2 = 1
    if k3 != 2:
        if lisx[2] == 1:
            t3 = 0
        if lisx[2] == 0:
            t3 = 1
    if k4 != 2:
        if lisx[3] == 1:
            t4 = 0
        if lisx[3] == 0:
            t4 = 1
    if k5 != 2:
        if lisx[4] == 1:
            t5 = 0
        if lisx[4] == 0:
            t5 = 1
    # Caso a chave for impar ele troca o algarismo pelo oposto(se for 1 muda pra 0 e ao contrario), isso faz com que a chave vire par
    nax = t1 * 16 + t2 * 8 + t3 * 4 + t4 * 2 + t5
    # Trasforma o numero de decimal para binario
    return nax

# Um loop que para só quando todas as colunas estiverem zeradas
while sum(ng) != 0:
    con += 1
    # Pula a jogada do usuario caso for a primeira rodada:
    if con != 1:
        c = input("Qual coluna?")
        b = int(input("Quantos palitos?"))
    # Pergunta qual coluna o usuario vai jogar e quantos palitos ira retirar da mesma
        if c == "1":
            n1 = n1 - b
        if c == "2":
            n2 = n2 - b
        if c == "3":
            n3 = n3 - b
        if c == "4":
            n4 = n4 - b
        if c == "5":
            n5 = n5 - b
        # Atualiza o valor da coluna

        # SETOR DO PLAYER
        ng = nums(cm, n1, n2, n3, n4, n5)

        print("PLAYER JOGOU:")
        print(n1 * '|', n2 * '|', n3 * '|', n4 * "|", n5 * "|")
        for d in ng:
            print(d, end=" ")
        print("")
        # Mostra a jogada do usuario

    nb1 = '%05d' % int(bin(n1)[2:])
    nb2 = '%05d' % int(bin(n2)[2:])
    nb3 = '%05d' % int(bin(n3)[2:])
    nb4 = '%05d' % int(bin(n4)[2:])
    nb5 = '%05d' % int(bin(n5)[2:])
    # Transforma os numeros em binario

    lis1 = [int(nb1[0]), int(nb1[1]), int(nb1[2]), int(nb1[3]), int(nb1[4])]
    lis2 = [int(nb2[0]), int(nb2[1]), int(nb2[2]), int(nb2[3]), int(nb2[4])]
    lis3 = [int(nb3[0]), int(nb3[1]), int(nb3[2]), int(nb3[3]), int(nb3[4])]
    lis4 = [int(nb4[0]), int(nb4[1]), int(nb4[2]), int(nb4[3]), int(nb4[4])]
    lis5 = [int(nb5[0]), int(nb5[1]), int(nb5[2]), int(nb5[3]), int(nb5[4])]
    # Faz uma lista de cada numero separando os algarismo
    # Pra poder manipular mais facilmente

    # Faz a mesma coisa que o de cima
    # for c in nb1:
    #     lis1 += [int(c)]

    # Verifica as chaves:
    if (lis1[0] + lis2[0] + lis3[0] + lis4[0] + lis5[0]) % 2 == 0:
        k1 = 2
    else:
        k1 = 0
    if (lis1[1] + lis2[1] + lis3[1] + lis4[1] + lis5[1]) % 2 == 0:
        k2 = 2
    else:
        k2 = 0
    if (lis1[2] + lis2[2] + lis3[2] + lis4[2] + lis5[2]) % 2 == 0:
        k3 = 2
    else:
        k3 = 0
    if (lis1[3] + lis2[3] + lis3[3] + lis4[3] + lis5[3]) % 2 == 0:
        k4 = 2
    else:
        k4 = 0
    if (lis1[4] + lis2[4] + lis3[4] + lis4[4] + lis5[4]) % 2 == 0:
        k5 = 2
    else:
        k5 = 0
    # O else ta ali pra ser mais otimizado, pra usar esse bloco em todas as rodadas(se não, ia ser necessario zerar todos as chaves toda rodada)

    if k1 + k2 + k3 + k4 + k5 == 10 and con == 1:
        print("A sequencia digitada, ja começa segura, logo a maquina não consegue ganhar")
        break
    # Caso o jogo que o usuario pedir ja esteja em uma sequencia par, não tem como a maquina ganhar


    # SETOR DA COLUNA 1
    na1 = analise(lis1)
    if na1 < n1:
        n1 = na1
        ng = nums(cm, n1, n2, n3, n4, n5)
        print("MAQUINA JOGOU:")
        print(na1 * '|', n2 * '|', n3 * '|', n4 * "|", n5 * "|")
        for d in ng:
            print(d, end=" ")
        print("")
        continue
    # Verifica se o numero pode ser modificado, é necessario porque um numero não pode mudar para maior que ele

    # SETOR DA COLUNA 2
    na2 = analise(lis2)
    if na2 < n2:
        n2 = na2
        ng = nums(cm, n1, n2, n3, n4, n5)
        print("MAQUINA JOGOU:")
        print(n1 * '|', na2 * '|', n3 * '|', n4 * "|", n5 * "|")
        for d in ng:
            print(d, end=" ")
        print("")
        continue

    # SETOR DA COLUNA 3
    na3 = analise(lis3)
    if na3 < n3:
        n3 = na3
        ng = nums(cm, n1, n2, n3, n4, n5)
        print("MAQUINA JOGOU:")
        print(n1 * '|', n2 * '|', na3 * '|', n4 * "|", n5 * "|")
        for d in ng:
            print(d, end=" ")
        print("")
        continue

    # SETOR DA COLUNA 4
    na4 = analise(lis4)
    if na4 < n4:
        n4 = na4
        ng = nums(cm, n1, n2, n3, n4, n5)
        print("MAQUINA JOGOU:")
        print(n1 * '|', n2 * '|', n3 * '|', na4 * "|", n5 * "|")
        for d in ng:
            print(d, end=" ")
        print("")
        continue

    # SETOR DA COLUNA 5
    na5 = analise(lis5)
    if na5 < n5:
        n5 = na5
        ng = nums(cm, n1, n2, n3, n4, n5)
        print("MAQUINA JOGOU:")
        print(n1 * '|', n2 * '|', n3 * '|', n4 * "|", na5 * "|")
        for d in ng:
            print(d, end=" ")
        print("")
        continue
