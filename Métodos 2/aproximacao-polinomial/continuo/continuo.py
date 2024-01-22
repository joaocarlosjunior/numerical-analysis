from sympy import Symbol, sympify, integrate


# Forma o sistema de acordo com o grau m e faz a resolução com o intervalo [a,b].
def sistema(grauM, a, b, funcao):
    x = Symbol('x')
    for coluna in range(grauM + 1):
        linha_L = [0.0] * (grauM + 1)
        for linha in range(grauM + 1):
            linha_L[linha] = integrate(((x ** linha) * (x ** coluna)), (x, a, b))
        matriz2[coluna] = integrate((sympify(funcao) * (x ** coluna)), (x, a, b))
        matriz1.append(linha_L)


def eliminacaoGauss(A, b):
    # n é a ordem da matriz A
    n = len(A)
    # Para cada etapa k
    for k in range(0, n-1):
        # Para cada linha i
        for i in range(k+1, n):
            #Calcula o fator m
            m = -A[i][k]/A[k][k]
            # Atualiza a linha i da matriz, percorrendo todas as colunas j
            for j in range(k+1, n):
                A[i][j] = (m * A[k][j]) + A[i][j]
            # Atualiza o vetor b na linha i
            b[i] = m * b[k] + b[i]


def solucao(grauM, matriz1, matriz2, funcao):
    sistema(grauM, a, b, funcao)
    eliminacaoGauss(matriz1, matriz2)
    X = [0.0] * (grauM + 1)
    X[grauM] = matriz2[grauM] / matriz1[grauM][grauM]
    for i in range(grauM, -1, -1):
        s = 0.0
        for j in range(i + 1, grauM + 1):
            s = s + (matriz1[i][j] * X[j])
            X[i] = (matriz2[i] - s) / matriz1[i][i]

    return X


if __name__ == "__main__":
    # Aquivos de entrada e saida.
    entrada = open('entrada.txt','r')
    saida = open('saida.txt','w')

    funcao = entrada.readline()
    a = int(entrada.readline())
    b = int(entrada.readline())
    grauM = int(entrada.readline())
    matriz1 = []
    matriz2 = [0.0]*(grauM+1)
    s = solucao(grauM, matriz1, matriz2, funcao)
    x = Symbol('x')
    soma = 0
    for i in range(grauM + 1):
        soma = soma + s[i] * x ** i
    saida.write(f"P(x) = {soma}")
