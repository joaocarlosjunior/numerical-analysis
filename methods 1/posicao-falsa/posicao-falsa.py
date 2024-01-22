# Biblioteca necessaria
from numpy import *


# Funcão que recebe a funcao a ser calculada e o valor de substituicão de x.
def fun(funcao, x):
    return eval(funcao)


# Metodo posicão falsa
def posicaoFalsa(funcao, a, b, e):
    # Produto de f(a) com f(b) for menor que 0 se tem uma raiz no intervalo
    # [a, b] podendo assim encontrar esse valor.
    if fun(funcao, a) * fun(funcao, b) < 0:
        i = 1
        # Calcula o ponto intermediário do intervalo [a, b]
        c = ((a * fun(funcao, b)) - (b * fun(funcao, a))) / (fun(funcao, b) - fun(funcao, a))
        # Enquanto o resultado da função for maior que a precisão
        while abs(fun(funcao, c)) > e:
            # Se o valor do produto de f(a) por f(b) for menor que 0
            # b recebe o valor de c, se não a recebe valor de c.
            if fun(funcao, a) * fun(funcao, c) < 0: b = c
            else: a = c
            # Calcula o ponto intermediário do intervalo [a, b].
            c = ((a * fun(funcao, b)) - (b * fun(funcao, a))) / (fun(funcao, b) - fun(funcao, a))
            # Contando as iterações
            i = i + 1

        fileOutput.write(f"Função: {str(funcao)}")
        fileOutput.write(f"Tolerância: {str(b - a)}\n")
        fileOutput.write(f"Número de iterações: {i}\n")
        fileOutput.write(f"Valor de c: {float(c)}\n")
        fileOutput.write(f"f(c): {fun(funcao, c)}\n\n")

    else: print("Não a raiz nesse intervalo!\n")


if __name__ == "__main__":
    fileInput = open("input.txt", "r")
    fileOutput = open("output.txt", "w")

    while True:
        # Função do arquivo
        funcao = fileInput.readline()
        # Extremo a
        a = float(fileInput.readline())
        # Extremo b
        b = float(fileInput.readline())
        # Erro toleravel
        epsilon = float(fileInput.readline())
        # Executando o método.
        posicaoFalsa(funcao, a, b, epsilon)

        if fileInput.readline() != "": continue
        break

    # Fechando os arquivos.
    fileInput.close()
    fileOutput.close()
