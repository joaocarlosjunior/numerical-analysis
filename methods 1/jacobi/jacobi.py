# Método para calcular a norma entre dois vetores v e x.
def norma(v, x):
    # n é a ordem do vetor v.
    n = len(v)
    # Número máximo do numerador.
    maxNumerador = 0
    # Número máximo do numerador.
    maxDenominador = 0
    # Loop para percorrer os componentes do vetor v e x.
    for i in range(0, n):
        # Calcula o valor absoluto da diferença.
        numerador = abs(v[i] - x[i])
        # Se o numerador for maior que o maximo numerador
        # atualiza o maximo numerador.
        if numerador > maxNumerador:
            maxNumerador = numerador
        # O valor absoluto da maior aproximação atual do v[i].
        denominador = abs(v[i])
        # Se o denominador for maior que o maximo denominador
        # atualiza o maximo denominador.
        if denominador > maxDenominador:
            maxDenominador = denominador
    return maxNumerador/maxDenominador


# Método para resolver sistema linear Ax=b
def jacobi_(A, b, e, iter):
    # n é a ordem do vetor A.
    n = len(A)
    x = [0] * n
    v = [0] * n
    # Loop para dividir cada linha da matriz A e do vetor b por A[i][i].
    for i in range(0,n):
        for j in range(0,n):
            # Só divide se o elemento for diferente da diagonal principal.
            if i != j:
                # Verifica se o elemento da diagonal principal é diferente de 0.
                if A[i][i] != 0:
                    A[i][j] = A[i][j]/A[i][i]
                else:
                    print("ERRO! Elemento da diagonal principal igual a 0.")
        # vetor b recebe o seu valor dividido pelo elemento da diagonal principal da mesma linha.
        b[i] = b[i] / A[i][i]
    # Faz a copia do vetor b em x.
    x = b[:]

    for k in range(1, iter+1):
        # Percorrer as linhas.
        for i in range(0,n):
            # Variavel para calcular o somatorio.
            soma = 0
            # Percorrer as colunas e calcular o somatorio.
            for j in range(0, n):
                if i != j:
                    # Somatorio do produto dos elementos da linha i pela coluna j
                    # pela aproximação anterior.
                    soma = soma + A[i][j] * x[j]
            # Calculando a aproximação atual.
            v[i] = b[i] - soma
            # Calcula a norma entre o vetor v e o vetor x.
            resultado = norma(v, x)
            if resultado <= e:
                return v
            # Faz a copia do vetor v em x
            x = v[:]


if __name__ == '__main__':
    fileInput = open('input.txt', 'r')
    fileOutput = open('output.txt', 'w')
    A = []
    B = []
    # Pegando o valor acima da matriz que representa o número de linhas.
    size = int(fileInput.readline())
    # Pegando o valor acima da matriz que representa a precisão.
    epsilon = float(fileInput.readline())
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
    # Resolvendo o sistema.
    fileOutput.write(str(jacobi_(A, B, epsilon, 50)) + '\n')
    # Fechando os arquivos.
    fileInput.close()
    fileOutput.close()
