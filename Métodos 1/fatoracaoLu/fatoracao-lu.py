# Função subistituição sucessiva para resolver o sistema trianguluar
# inferior Ax=b.
def substituicaoSucessiva(A, b):
    pivo(A, b)
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
    pivo(A,b)
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


if __name__ == '__main__':
    fileInput = open('input.txt', 'r')
    fileOutput = open('output.txt', 'w')
    A = []
    B = []
    # Pegando o valor acima da matriz que representa o número de linhas.
    size = int(fileInput.readline())
    # Laço que faz a leitura de cada linha montando a matriz linha por linha.
    for i in range(size):
        linha = []
        # Faz a leitura da linha em questão
        valores_linha = fileInput.readline()
        # Remove o '\n'
        valores_linha = (valores_linha.replace('\n', ''))
        # Divide os elementos com base no espeço entre eles.
        valores_linha = valores_linha.split(' ')
        # Faz a varredura do vetor A e armazena em 'linha'.
        for j in range(len(valores_linha) - 1):
            linha.append(float(valores_linha[j]))
        # Armazena o valor da última coluna referente ao vetor B
        B.append(float(valores_linha[j + 1]))
        # Armazena da coluna 0 a coluna n-1, referentes ao vetor A
        A.append(linha)
    # Matriz L e a Matriz U
    L, U = lu(A)
    # Resolvendo o sistema.
    fileOutput.write(str(lux(L, U, B)) + '\n')
    # Fechando os arquivos.
    fileInput.close()
    fileOutput.close()
