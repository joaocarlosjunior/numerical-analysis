from math import e


def f2(funcao, x, y, z):
    return eval(funcao)


def shooting(funcao, chute, h, valor, yInicial, pontos):
    z, y, yt = [], [], []
    for j in range(3):
        x = 0
        y = [yInicial]
        if j != 2:
            z = [chute[j]]
            for i in range(pontos):
                y.append(y[i] + h * z[i])
                z.append(z[i] + h * f2(funcao, x, y[i], z[i]))
                x += h

            yt.append(y[-1])

            if y[-1] == valor: break
        else:
            z = [chute[0] + ((chute[1] - chute[0]) / (yt[1] - yt[0])) * (valor - yt[0])]
            for i in range(pontos):
                y.append(y[i] + h * z[i])
                z.append(z[i] + h * f2(funcao, x, y[i], z[i]))
                x += h
    return z[0], y[-1]


if __name__ == "__main__":
    entrada = open("entrada.txt", "r")
    saida = open("saida.txt", "w")
    while True:
        # Função.
        funcao = entrada.readline()
        # Os valores de chute.
        chute = [float(i) for i in entrada.readline().replace('\n', '').split(' ')]
        # Valor de h(passo).
        h = float(entrada.readline())
        # Valor desejado a ser encontrado.
        valor = float(entrada.readline())
        # O valor de y inicial.
        yInicial = float(entrada.readline())
        # Quantidade de pontos internos.
        pontos = int(entrada.readline())

        z0, yFinal = shooting(funcao, chute, h, valor, yInicial, pontos)

        saida.write(f"Função: {funcao}")
        saida.write(f"Z(0) = {z0}\nY = {yFinal}\n")
        if entrada.readline() == "": break

    entrada.close()
    saida.close()
