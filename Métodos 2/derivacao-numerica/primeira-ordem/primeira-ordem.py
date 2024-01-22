from numpy import e,log,sin


def f(funcao, x):
    return eval(funcao)


if __name__ == "__main__":
    # Aquivos de entrada e saida.
    entrada = open('entrada.txt', 'r')
    saida = open('saida.txt', 'w')

    while True:
        # Faz a leitura da função, x e h do arquivo texto.
        funcao = entrada.readline()
        x = float(entrada.readline())
        h = float(entrada.readline())

        progressiva = (f(funcao, x + h) - f(funcao, x)) / h
        retardada = (f(funcao, x) - f(funcao, x - h)) / h
        centrada = (f(funcao, x + h) - f(funcao, x - h)) / (2 * h)

        saida.write(f"Funcao: {funcao}")
        saida.write(f"Progressiva: {progressiva}\n")
        saida.write(f"Retardada: {retardada}\n")
        saida.write(f"Centrada: {centrada}\n\n")

        if entrada.readline() == "":
            break
    entrada.close()
    saida.close()
