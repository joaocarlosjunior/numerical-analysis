def f(funcao, x, y):
    return eval(funcao)


# Método de Runge-Kutta de 3ª ordem.
def runge3Ordem(funcao, y, I, h):
    yProximo, x = 0, 0

    while x < I:
        k1 = f(funcao, x, y)
        k2 = f(funcao, x + (1 / 2 * h), y + (1 / 2 * k1) * h)
        k3 = f(funcao, x + h, y - (k1 * h) + (2 * k2) * h)
        yProximo = y + 1 / 6 * (k1 + 4 * k2 + k3) * h
        x += h
        y = yProximo
    return y


def fS(funcao, x, y1, y2):
    return eval(funcao)


# Método de Runge-Kutta de 3ª Ordem para Sistemas de equações diferenciais.
def runge3OrdemSistema(funcao, y1, y2, I, h):
    y1Proximo, y2Proximo, x = 0, 0, 0
    while x < I:
        k1 = fS(funcao[0], x, y1, y2)
        k2 = fS(funcao[0], x + (1 / 2 * h), y1 + (1 / 2 * k1) * h,y2 + (1 / 2 * k1) * h)
        k3 = fS(funcao[0], x + h, y1 - (k1 * h) + (2 * k2) * h, y2 - (k1 * h) + (2 * k2) * h)
        y1Proximo = y1 + 1 / 6 * (k1 + 4 * k2 + k3) * h

        k1 = fS(funcao[1], x, y1, y2)
        k2 = fS(funcao[1], x + (1 / 2 * h), y1 + (1 / 2 * k1) * h, y2 + (1 / 2 * k1) * h)
        k3 = fS(funcao[1], x + h, y1 - (k1 * h) + (2 * k2) * h, y2 - (k1 * h) + (2 * k2) * h)
        y2Proximo = y2 + 1 / 6 * (k1 + 4 * k2 + k3) * h

        y1 = y1Proximo
        y2 = y2Proximo
        x += h

    return y1, y2


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
            y1Final, y2Final = runge3OrdemSistema(funcao, y1, y2, I, h)
            saida.write(f"Funções: {funcao[0]} | {funcao[1]}\n")
            saida.write(f"Y1: {y1Final} \nY2: {y2Final}\n\n")
        else:
            # Intervalo
            I = int(entrada.readline())
            # Valor h
            h = float(entrada.readline())
            # Valor inicial de y
            y = float(entrada.readline())
            yFinal = runge3Ordem(funcao, y, I, h)
            saida.write(f"Função: {funcao}")
            saida.write(f"Y({I}) = {yFinal}\n\n")

        if entrada.readline() == '': break
    entrada.close()
    saida.close()
