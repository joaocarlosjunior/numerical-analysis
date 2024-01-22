from math import e, pi, sqrt


def f(fun,x):
    return eval(fun)


if __name__ == "__main__":
    entrada = open("entrada.txt","r")
    saida = open("saida.txt","w")

    while True:
        funcao = entrada.readline()
        a = float(entrada.readline())
        b = float(entrada.readline())

        h = b - a
        i = h/2*(f(funcao,a) + f(funcao,b))
        saida.write(f"Função: {funcao}")
        saida.write(f"I: {i}\n\n")

        if entrada.readline() == '': break

    entrada.close()
    saida.close()
