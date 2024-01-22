def f(funcao, x, y):
    return eval(funcao)


# Método de Euler.
def eulerModificado(fun, y, I, h):
    x = 0
    yPrevisao, xProximo = 0,0
    while x < I:
        yPrevisao = y + h*f(fun,x,y)
        xProximo = x + h
        y += (h/2)*(f(fun,x,y) + f(fun,xProximo,yPrevisao))
        x += h
    return y


def fS(funcao, x, y1, y2):
    return eval(funcao)


# Método de Euler para Sistemas de equações diferenciais.
def eulerModificadoSistema(fun, y1, y2, I, h):
    x = 0
    y1Previsao, y2Previsao, xProximo = 0,0,0
    while x < I:
        y1Previsao = y1 + h * fS(fun[0], x, y1, y2)
        y2Previsao = y2 + h * fS(fun[1], x, y1, y2)
        xProximo = x + h
        y1 += (h/2)*(fS(fun[0], x, y1, y2) + fS(fun[0], xProximo, y1Previsao, y2Previsao))
        y2 += (h/2)*(fS(fun[1], x, y1, y2) + fS(fun[1], xProximo, y1Previsao, y2Previsao))
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
            y1Final, y2Final = eulerModificadoSistema(funcao, y1, y2, I, h)
            saida.write(f"Funções: {funcao[0]} | {funcao[1]}\n")
            saida.write(f"Y1: {y1Final} \nY2: {y2Final}\n\n")
        else:
            # Intervalo
            I = int(entrada.readline())
            # Valor h
            h = float(entrada.readline())
            # Valor inicial de y
            y = float(entrada.readline())
            yFinal = eulerModificado(funcao, y, I, h)
            saida.write(f"Função: {funcao}")
            saida.write(f"Y({I}) = {yFinal}\n\n")

        if entrada.readline() == '':break
    entrada.close()
    saida.close()
