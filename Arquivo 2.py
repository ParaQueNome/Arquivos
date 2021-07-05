n = int(input('Informe a quantidade de eleitores:'"\n"))
arq = open('votos.txt', 'w')

for i in range(n):
    numero_candidato = str(input('Informe o código do candidato para cada eleitor:''\n'))
    arq.write(numero_candidato)
    arq.write("\n")
arq.close()

#Programa:




votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0
votos_candidato4 = 0
votos_candidato5 = 0
votos_nulos = 0
eleitores = []
arq = open('votos.txt', 'r')
linha = arq.readline()
while linha:
    dados_votos = linha.split()
    if dados_votos[0] == '100':
        votos_candidato1 = votos_candidato1 + 1
    elif dados_votos[0] == '200':
        votos_candidato2 +=1
    elif dados_votos[0] == '300':
        votos_candidato3 +=1
    elif dados_votos[0] == '400':
        votos_candidato4 +=1
    elif dados_votos[0] == '500':
        votos_candidato5 +=1
    else:
        votos_nulos +=1
    linha = arq.readline()
eleitores.append(votos_candidato1)
eleitores.append(votos_candidato2)
eleitores.append(votos_candidato3)
eleitores.append(votos_candidato4)
eleitores.append(votos_candidato5)

print(eleitores)
num_votos = votos_candidato1
menor_votos = votos_candidato1

for i in eleitores:
    if num_votos < i:
        num_votos = i
        if num_votos == eleitores[0]:
            print('O candidato "1" tem o maior número de votos com', num_votos,'votos')
        elif num_votos == eleitores[1]:
            print('O candidato "2" tem o maior número de votos com', num_votos, 'votos')
        elif num_votos == eleitores[2]:
            print('O candidato "3" tem o maior número de votos com', num_votos, 'votos')
        elif num_votos == eleitores[3]:
            print('O candidato "4" tem o maior número de votos com', num_votos, 'votos')
        elif num_votos == eleitores[4]:
            print('O candidato "5" tem o maior número de votos com', num_votos, 'votos')

    for menor in eleitores:
        if menor_votos >= menor:
            menor_votos = menor
            if menor_votos == eleitores[0]:
                print('0 candidato "1" tem o menor número de votos com', menor_votos, 'votos')
            if menor_votos == eleitores[1]:
                print('0 candidato "2" tem o menor número de votos com', menor_votos, 'votos')
            if menor_votos == eleitores[2]:
                print('0 candidato "3" tem o menor número de votos com', menor_votos, 'votos')
            if menor_votos == eleitores[3]:
                print('0 candidato "4" tem o menor número de votos com', menor_votos, 'votos')
            if menor_votos == eleitores[4]:
                print('0 candidato "5" tem o menor número de votos com', menor_votos, 'votos')


print('A quantidade de votos nulos é:', votos_nulos, 'votos')













