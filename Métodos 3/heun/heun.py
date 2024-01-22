def f(funcao, x, y):
    return eval(funcao)


# Método Heun.
def heun(funcao, y, I, h):
    x, yProximo = 0, 0
    while x < I:
        f1 = f(funcao, x, y)
        f2 = f(funcao, x + h, y + (f1 * h))
        yProximo = y + (h * (f1 + f2) / 2)
        x += h
        y = yProximo

    return y


def fS(funcao, x, y1, y2):
    return eval(funcao)


# Método de Heun para Sistemas de equações diferenciais.
def heunSistema(funcao, y1, y2, I, h):
    x, y1Proximo, y2Proximo = 0, 0, 0
    while x < I:
        f1 = fS(funcao[0], x, y1, y2)
        f2 = fS(funcao[0], x + h, y1 + (f1 * h), y2 + (f1 * h))
        y1Proximo = y1 + (h * (f1 + f2) / 2)

        f1 = fS(funcao[1], x, y1Proximo, y2)
        f2 = fS(funcao[1], x + h, y1Proximo + (f1 * h), y2 + (f1 * h))
        y2Proximo = y2 + (h * (f1 + f2) / 2)

        x += h
        y1 = y1Proximo
        y2 = y2Proximo

    return y1,y2


if __name__ == "__main__":
    entrada = open("entrada.txt", "r")
    saida = open("saida.txt", "w")
    while True:
        # Funcao
        funcao = entrada.readline()
        if "S" in funcao:
            # Função que será utilizada.
            funcao = funcao.replace('S', '').replace('\n', '').split('|')
            # Y1.
            y1 = float(entrada.readline())
            # Y2.
            y2 = float(entrada.readline())
            # Passo.
            h = float(entrada.readline())
            # Intervalo.
            I = int(entrada.readline())
            y1Final, y2Final = heunSistema(funcao, y1, y2, I, h)
            saida.write(f"Funções: {funcao[0]} | {funcao[1]}\n")
            saida.write(f"Y1: {y1Final} \nY2: {y2Final}\n\n")
        else:
            # Intervalo
            I = int(entrada.readline())
            # Valor h
            h = float(entrada.readline())
            # Valor inicial de y
            y = float(entrada.readline())
            yFinal = heun(funcao, y, I, h)
            saida.write(f"Função: {funcao}")
            saida.write(f"Y({I}) = {yFinal}\n\n")

        if entrada.readline() == '': break
    entrada.close()
    saida.close()