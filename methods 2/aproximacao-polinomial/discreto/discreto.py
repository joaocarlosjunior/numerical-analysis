from fatoracaoLu import fatorLu
from sympy import Symbol


def calculoMatriz(m, y):
    # Crio lista temporária.
    temp = []
    for i in range(len(m)):
        temp.append(sum([y[j] * m[i][j] for j in range(len(y))]))

    return temp


def produto(m, x, y):
    # Cria lista auxiliar.
    aux = []
    for i in range(len(m[0])):
        aux.append(m[x][i] * m[y][i])
    return sum(aux)


def resolveMatriz(m):
    temp = []
    for i in range(len(m)):
        temp.append([produto(m, j, i) for j in range(len(m))])
    return temp


if __name__ == "__main__":
    # Aquivos de entrada e saida.
    entrada = open('entrada.txt', 'r')
    saida = open('saida.txt', 'w')
    # Pego valores do arquivo de entrada,substituo a quebra de
    # linha por vazio e separo os valores por espaço em uma lista.
    x = entrada.readline().replace('\n', '').split(' ')
    y = entrada.readline().replace('\n', '').split(' ')
    grauM = int(entrada.readline())
    # Crio lista x e y forçando os elementos do arquivo serem do tipo float.
    x = [float(i) for i in x]
    y = [float(i) for i in y]

    matriz = [[i**j for i in x] for j in range(grauM + 1)]

    v = calculoMatriz(matriz, y)
    a = fatorLu(resolveMatriz(matriz), v)
    x = Symbol('x')
    s = 0
    for i in range(grauM + 1):
        s += a[i]*x**i
    saida.write(f"P(x) = {s}")
    # Fecho os aquivos.
    entrada.close()
    saida.close()
