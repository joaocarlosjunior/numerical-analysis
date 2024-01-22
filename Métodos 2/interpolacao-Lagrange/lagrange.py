from sympy import Symbol, simplify, expand


def polinomioLagrange(x,y):
    X = Symbol('x')
    coeficientes = []
    for i in range(len(x)):
        L = 1
        for j in range(len(x)):
            if i != j:
                L *= (X - x[j]) / (x[i] - x[j])
        coeficientes.append(L)

    polinoInterpo = 0
    for i in range(len(coeficientes)):
        polinoInterpo += y[i]*coeficientes[i]

    p = simplify(polinoInterpo)
    p = expand(p)
    return p


if __name__ == "__main__":
    # Aquivos de entrada e saida.
    entrada = open('entrada.txt', 'r')
    saida = open('saida.txt', 'w')
    # Pego valores do arquivo de entrada,substituo a quebra de
    # linha por vazio e separo os valores por espaço em uma lista.
    x = [float(i) for i in entrada.readline().replace('\n', '').split(' ')]
    y = [float(i) for i in entrada.readline().replace('\n', '').split(' ')]
    saida.write(f'P(x): {polinomioLagrange(x,y)}')
    #Fechando os arquivos
    entrada.close()
    saida.close()
