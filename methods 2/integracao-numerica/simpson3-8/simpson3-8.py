from math import e, pi, sqrt


def f(fun, x):
    return eval(fun)


if __name__ == '__main__':
    entrada = open("entrada.txt", "r")
    saida = open("saida.txt", "w")

    while True:
        funcao = entrada.readline()
        x = [float(i) for i in entrada.readline().replace('\n', '').split(' ')]
        n = int(entrada.readline().replace('\n', ''))

        h = (x[-1] - x[0])
        somatorio = 0
        p = [x[0] + (h / n)]

        for i in range(1, n - 1): p.append(p[i - 1] + (h / n))

        for i in p:
            somatorio += 3 * f(funcao, i)

        I = h * ((f(funcao, x[0]) + somatorio + f(funcao, x[-1])) / 8)

        saida.write(f"Função: {funcao}")
        saida.write(f"I: {I}\n\n")
        if entrada.readline() == '': break
    entrada.close()
    saida.close()
