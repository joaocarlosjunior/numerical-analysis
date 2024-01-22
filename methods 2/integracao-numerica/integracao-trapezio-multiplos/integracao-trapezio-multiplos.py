from math import e, pi, sqrt, cos


def f(funcao, x):
    return eval(funcao)


def trapezioMultiplo(x, func):
    n = len(x)
    somatorio = sum(f(func, x[i]) for i in range(1, n - 1))
    h = x[-1] - x[0]
    I = h * ((f(func, x[0]) + 2 * somatorio + f(func, x[-1]))/(2*(n-1)))
    return I


if __name__ == '__main__':
    entrada = open("entrada.txt", "r")
    saida = open("saida.txt", "w")

    while True:
        funcao = entrada.readline()
        x = [float(i) for i in entrada.readline().replace('\n', '').split(' ')]
        n = int(entrada.readline().replace('\n', ''))
        h = (x[-1] - x[0]) / n
        pontos = [x[0]]
        for i in range(1, n + 1):
            pontos.append(pontos[i - 1] + h)
        saida.write(f"Função: {funcao}")
        saida.write(f"I: {trapezioMultiplo(pontos, funcao)}\n\n")
        if entrada.readline() == '': break
    entrada.close()
    saida.close()
