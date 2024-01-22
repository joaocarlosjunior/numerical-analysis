from math import e, pi, sqrt


def f(f, x):
    return eval(f)


def richards(x0, func):
    # Integracao entre dois pontos consecutivos utilizando regra do trapezio.
    I1 = trapezioSimples(x0, func)
    # Integracao com intervalo 2 dos pontos.
    I2 = trapezioMultiplo(x0[::2], func)
    # Integracao com n sub-intervalos.
    I3 = trapezioMultiplo(x0, func)

    I4 = 4 / 3 * I2 - 1 / 3 * I1
    I5 = 4 / 3 * I3 - 1 / 3 * I2
    I = 16 / 15 * I5 - 1 / 15 * I4

    return I


def trapezioSimples(x0, fun):
    h = x0[-1] - x0[0]
    I = h * ((f(fun, x0[0]) + f(fun, x0[-1])) / 2)
    return I


def trapezioMultiplo(x0, fun):
    n = len(x0)
    somatorio = sum(f(fun, x0[i]) for i in range(1, n - 1))
    h = x0[-1] - x0[0]
    I = h * ((f(fun, x0[0]) + 2 * somatorio + f(fun, x0[-1])) / (2 * (n - 1)))
    return I


if __name__ == "__main__":
    entrada = open('entrada.txt', 'r')
    saida = open('saida.txt', 'w')
    while True:
        funcao = entrada.readline().replace('\n', '')
        x = [float(i) for i in entrada.readline().replace('\n', '').split(' ')]
        n = int(entrada.readline().replace('\n', ''))
        h = (x[1] - x[0]) / n

        p = [x[0]]
        for i in range(1, n + 1):
            p.append(p[i - 1] + h)
        I = richards(p, funcao)
        saida.write(f"Função: {funcao}\n")
        saida.write(f"I: {I}\n\n")
        if entrada.readline() == '':
            break
    entrada.close()
    saida.close()
