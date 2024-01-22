def regressaoLinear(n,x,y):
    somatorioX = somatorioXY = somatorioY = quadradoX = 0.0
    # Laço para calcular os somatorios que serão utilizados para
    # calcular a regressão linear.
    for i in range(n):
        somatorioXY += x[i]*y[i]
        somatorioX += x[i]
        somatorioY += y[i]
        quadradoX += (x[i]**2)
    # Calculando a regressão por mínimos quadrados.
    a = ((n*somatorioXY) - (somatorioX*somatorioY))/((n*quadradoX) - (somatorioX**2))
    b = ((somatorioY * quadradoX) - (somatorioX * somatorioXY))/((n*quadradoX) - (somatorioX**2))
    # Retorna os valores de a e b.
    return a,b


if __name__ == "__main__":
    # Aquivos de entrada e saida.
    entrada = open('entrada.txt','r')
    saida = open('saida.txt','w')
    while True:
        # Pego valores do arquivo de entrada,substituo a quebra de
        # linha por vazio e separo os valores por espaço em uma lista.
        x = entrada.readline().replace('\n','').split(' ')
        y = entrada.readline().replace('\n','').split(' ')
        # Crio lista x e y forçando os elementos do arquivo serem do tipo float.
        x = [float(i) for i in x]
        y = [float(i) for i in y]
        # Chamo método passando quantidade número de pontos,
        # as listas x e y.
        a,b = regressaoLinear(len(x),x,y)
        # Gravo o resultado no arquivo de saida.
        saida.write(f'Pontos(x): {x}\n')
        saida.write(f'Pontos(y): {y}\n')
        saida.write(f'a = {a}\n')
        saida.write(f'b = {b}\n\n')
        if entrada.readline() == '':
            break
    # Fecho os aquivos.
    entrada.close()
    saida.close()