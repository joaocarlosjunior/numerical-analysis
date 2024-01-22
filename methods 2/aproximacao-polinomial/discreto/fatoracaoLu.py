# Função subistituição sucessiva para resolver o sistema trianguluar
# inferior Ax=b.
def substituicaoSucessiva(A, b):
    # n é a ordem da matriz A.
    n = len(A)
    # Inicializa o vetor x com tamanho n elementos iguais a 0.
    x = n * [0]
    # Laço variar do primeiro até o último elemento.
    for i in range(0, n):
        # Variavel para calcular o somatorio.
        soma = 0
        # Fazendo loop para calcular o somatorio.
        for j in range(0, i):
            soma = soma + A[i][j] * x[j]
        x[i] = (b[i] - soma) / A[i][i]
    return x


# Função subistituição retroativa para resolver o sistema trianguluar
# superior Ax=b.
def substituicaoRetroativa(A, b):
    # n é a ordem da matriz A.
    n = len(A)
    # Inicializa o vetor x com tamanho n elementos iguais a 0.
    x = n * [0]
    # Laço variar do último até o primeiro elemento.
    for i in range(n-1, -1, -1):
        soma = 0
        # Laço para o calculo do somatorio.
        for j in range(i+1, n):
            soma = soma + A[i][j] * x[j]
        x[i] = (b[i] - soma) / A[i][i]

    # retorna o vetor solução
    return x


# Cria uma matriz identidade de ordem n
def identidade(n):
    # Cria um vetor m
    m = []
    for i in range(0, n):
        # Uma linha com lista com n 0's
        linha = [0] * n
        # Na posição i da linha insiro o 1
        linha[i] = 1
        # Adiciono no vetor m
        m.append(linha)
    # retorna o vetor m
    return m


# Decompõe a matriz A no produto de duas matrizes(L e U).
# L triangular interior e U triangular superior.
def lu(A):
    # n é a ordem da matriz A
    n = len(A)
    # Inicializa o vetor L com a vetor identidade.
    L = identidade(n)
    # Para cada etapa k
    for k in range(0, n - 1):
        # Para cada linha i
        for i in range(k + 1, n):
            # Calcula o fator m
            m = - A[i][k] / A[k][k]
            # Copiando o valor de m para a matriz L.
            L[i][k] = -m
            # Atualiza a linha i da matriz, percorrendo todas as colunas j
            for j in range(k + 1, n):
                A[i][j] = (m * A[k][j]) + A[i][j]
            # zera o elemento Aik
            A[i][k] = 0
    return L, A


# Função para fazer o pivoteamento da matriz. Verifica se o pivo da coluna é
# diferente de 0 e se é o maior número da sua coluna.
def pivo(A, B):
    n = len(A)
    for i in range(n):
        for j in range(i+1, n):
            if abs(A[i][i]) < abs(A[j][i]):
                aux = A[i]
                A[i] = A[j]
                A[j] = aux
                aux1 = B[i]
                B[i] = B[j]
                B[j] = aux1


# Método para resolver o sistema LUx=b, resolvendo os dois sistemas triangulares sendo
# L matriz triangular inferior e U matriz triangular superior e b é o vetor.
def lux(L,U,b):

    y = substituicaoSucessiva(L, b)
    x = substituicaoRetroativa(U, y)

    return x


def fatorLu(A,B):
    L,U = lu(A)
    return lux(L,U,B)
