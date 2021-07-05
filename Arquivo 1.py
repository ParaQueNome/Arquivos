arq = open("pesquisa.txt", "w")
n = int(input("Digite a quantidade de entrevistados da pesquisa"))
for i in range(n):
    sexo = str(input('Informe se o sexo é "Feminino" ou "Masculino"'))
    arq.write(sexo )
    arq.write(" ")
    idade = str(input('Informe a idade da pessoa'))
    arq.write(idade)
    arq.write(" ")
    usuario = str(input('Informe se a pessoa é "fumante" ou "não_fumante"'))
    arq.write(usuario)
    arq.write(" ")
    formacao = str(input('Informe a formação da pessoa: "fundamental", "medio" ou "superior".'))
    arq.write("\n")
arq.close()


# Programa:
soma_homens = 0
soma_mulheres = 0
soma_total = 0
soma_fumantes = 0
homens_não_fumantes = 0
mulheres_fumantes = 0

arq = open("pesquisa.txt", "r")
linha = arq.readline()
while linha:
    dados_entrevistados = linha.split()
    if dados_entrevistados[2] == 'fumante':
        soma_fumantes +=1
    elif dados_entrevistados[0] == 'Masculino':
        soma_homens +=1
        if dados_entrevistados[1] < "40" and dados_entrevistados[2] == "não_fumante":
            homens_não_fumantes +=1
    elif dados_entrevistados[0] == 'Feminino':
        soma_mulheres +=1
        if dados_entrevistados[1] > '40' and dados_entrevistados[2] == 'fumante':
            mulheres_fumantes +=1


    soma_total +=1
    linha = arq.readline()

print("A porcentagem de fumantes em relação ao total de pessoas é:", (soma_fumantes/soma_total)*100, "%")
print('A porcentagem de homens não fumantes menores de 40 anos em relação ao total masculino é:', (homens_não_fumantes/soma_homens)*100, "%")
print('A porcentagem de mulheres fumantes acima de 40 anos em relação ao total feminino é:', (mulheres_fumantes/soma_mulheres)*100, "%")



