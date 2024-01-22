from math import *


# Funcão que recebe a funcao a ser calculada e o valor de substituicão de x.
def fun(funcao, x):
    return eval(funcao)


# Metodo de  secante
def secante_(funcao, a, b, e):
    # Produto de f(a) com f(b) for menor que 0 se tem uma raiz no intervalo
    # [a, b] podendo assim encontrar esse valor.
    if fun(funcao, a) * fun(funcao, b) < 0:
        i = 1
        # Ponto intermediário do intervalo [a, b]
        c = b - (fun(funcao, b) * (b - a)) / (fun(funcao, b) - fun(funcao, a))
        # Enquanto o resultado da função for maior que a precisão.
        while abs(fun(funcao, c)) > e:
            #Troca dos valores para a próxima iteração.
            a,b = b, c
            # Calcula novamente o ponto intermediário do intervalo [a, b].
            c = b - (fun(funcao, b) * (b - a)) / (fun(funcao, b) - fun(funcao, a))
            i = i + 1

        fileOutput.write(f"Função: {str(funcao)}")
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
        secante_(funcao, a, b, epsilon)

        if fileInput.readline() != "": continue
        break

    # Fechando os arquivos.
    fileInput.close()
    fileOutput.close()
