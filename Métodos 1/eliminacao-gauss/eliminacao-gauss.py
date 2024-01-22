def eliminacaoGauss(A, b):
    # n é a ordem da matriz A
    n = len(A)
    # Faz o pivoteamento em na matriz A
    pivo(A, b)
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
            # zera o elemento Aik
            A[i][k] = 0
    # Chama o método para resolver o sistema triangular superior.
    x = substituicaoRetroativa(A, b)
    return x

# Função subistituição retroativa para resolver o sistema trianguluar
# superior Ax=b
def substituicaoRetroativa(A, b):
    # n é a ordem da matriz A.
    n = len(A)
    # Inicializa o vetor x com tamanho n elementos iguais a 0.
    x = n * [0.0]
    # Laço variar do último até o primeiro elemento.
    for i in range(n-1, -1, -1):
        soma = 0
        # Laço para o calculo do somatorio.
        for j in range(i+1, n):
            soma = soma + A[i][j] * x[j]
        x[i] = (b[i] - soma) / A[i][i]

    # retorna o vetor solução.
    return x


# Método para fazer o pivoteamento da matriz. Verifica se o pivo da coluna é
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


if __name__ == '__main__':
    fileInput = open('input.txt', 'r')
    fileOutput = open('output.txt', 'w')
    # Criando os vetores A e B.
    A = []
    B = []
    # Número de linhas da matriz.
    size = int(fileInput.readline())
    # Laço que faz a leitura de cada linha montando a matriz linha por linha.
    for i in range(size):
        linha = []
        # Faz a leitura da linha em questão
        valoresLinha = fileInput.readline()
        # Remove o '\n'
        valoresLinha = (valoresLinha.replace('\n', ''))
        # Divide os elementos com base no espeço entre eles.
        valoresLinha = valoresLinha.split(' ')
        # Faz a varredura do vetor A e armazena em 'linha'.
        for j in range(len(valoresLinha) - 1):
            linha.append(float(valoresLinha[j]))
        # Armazena o valor da última coluna referente ao vetor B
        B.append(float(valoresLinha[j + 1]))
        # Armazena da coluna 0 a coluna n-1, referentes ao vetor A
        A.append(linha)
    # Executando o método principal e gravando o resultado ao mesmo tempo.
    fileOutput.write(str(eliminacaoGauss(A, B)) + '\n')
    # Fechando os arquivos.
    fileInput.close()
    fileOutput.close()
