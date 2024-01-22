from sympy import simplify, expand, Symbol


def interpolacaoNewton(x, y):
    tabela = []
    tabela.append(y)
    pontos = x
    passo = 1
    for i in range(len(x) - 1):
        ordem = []
        for j in range(len(tabela[i]) - 1):
            difDividida = (tabela[i][j + 1] - tabela[i][j]) / (pontos[j + passo] - pontos[j])
            ordem.append(difDividida)
        tabela.append(ordem)
        passo = passo + 1
    aprox = 0
    grau = 0
    X = Symbol('x')
    for i in range(len(tabela)):
        fator = tabela[i][0]
        for j in range(grau):
            fator = fator * (X - pontos[j])
        grau= grau +1
        aprox = aprox + fator
    p = simplify(aprox)
    p = expand(p)
    return p

if __name__ == "__main__":
    # Aquivos de entrada e saida.
    entrada = open('entrada.txt', 'r')
    saida = open('saida.txt', 'w')
    while True:
        # Pego valores do arquivo de entrada,substituo a quebra de
        # linha por vazio e separo os valores por espaço em uma lista.
        x = [float(i) for i in entrada.readline().replace('\n', '').split(' ')]
        y = [float(i) for i in entrada.readline().replace('\n', '').split(' ')]

        saida.write(f'P(x) = {interpolacaoNewton(x, y)}\n\n')
        if entrada.readline() == '': break

    entrada.close()
    saida.close()
