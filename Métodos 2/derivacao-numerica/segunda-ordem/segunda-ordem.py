from numpy import e,log,sin


def f(x,funcao):
    return eval(funcao)


if __name__ == "__main__":
    # Aquivos de entrada e saida.
    entrada = open('entrada.txt', 'r')
    saida = open('saida.txt', 'w')

    while True:
        # Faz a leitura da função,x e h do arquivo texto.
        funcao = entrada.readline()
        x = float(entrada.readline())
        h = float(entrada.readline())

        regressiva = (f(x, funcao) - 2 * f(x - h, funcao) + f(x - 2 * h, funcao)) / h**2
        centrada = (f(x + h, funcao) - 2 * f(x, funcao) + f(x - h, funcao)) / h**2
        avancada = (f(x + 2 * h, funcao) - 2 * f(x + h, funcao) + f(x, funcao)) / h**2

        saida.write(f"Funcao: {funcao}")
        saida.write(f"Regressiva: {regressiva}\n")
        saida.write(f"Centrada: {centrada}\n")
        saida.write(f"Avançada: {avancada}\n\n")

        if entrada.readline() == "": break
    entrada.close()
    saida.close()
