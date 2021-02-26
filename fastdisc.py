import sys
import os
import time
import argparse
import matplotlib.pyplot
import statistics



def main():

    tamanho = args.tamanho

    tempos = []
    tamanhos = []

    Word_file = '.\\entrada.txt'
    words = open(Word_file).read()

    data = ""

    for i in range(0,tamanho):
        for j in range(0,10):
            data += words
        output_file = open("temp.txt", "w")

        #inicio do algoritimo
        inicio = time.time()

        output_file.writelines(data)
        output_file.close()

        fim = time.time()

        tempos.append(round(fim - inicio, 2))
        tamanhos.append( 10*(i+1))
        os.remove("temp.txt")

    matplotlib.pyplot.plot(tamanhos, tempos, 'o--')
    matplotlib.pyplot.grid(True)
    matplotlib.pyplot.title("Benchmark")

    matplotlib.pyplot.xlabel('Tamanhos - (MB)')
    matplotlib.pyplot.xticks(tamanhos)

    matplotlib.pyplot.ylabel('Tempos - (segundos)')
    matplotlib.pyplot.yticks(tempos)

    matplotlib.pyplot.show()

    return [tempos, tamanhos]

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Tamanho do arquivo')
    parser.add_argument('--tamanho','-tm', type= int, default= 2,
        help= "Tamanho do teste")
    parser.add_argument('--repeticao','-rp', type= int, default= 1,
        help= "Quantas vezes o teste vai rodar")

    args = parser.parse_args()


    resultadoFinal = []

    output_file = open("tabela.csv", "w")
    linha = 'Tamanhos' ';' + 'Tempos' + '\n'
    output_file.writelines(linha)
    linha = ''

    tamanho = args.tamanho
    repeticao = args.repeticao

    for i in range(0,repeticao):
        resultado =  main()
        linha = str(i+1)+"º;\n"
        output_file.writelines(linha)
        for j in range(0,tamanho):
            linha = str(resultado[1][j]) + 'MB;' + str(resultado[0][j]) + 's\n'
            output_file.writelines(linha)
            linha = ''
            resultadoFinal.append(round(resultado[1][j]/resultado[0][j],2)) # MB/s

    # .mean() - Média  .median() - Mediana
    linha = ';\n;\n'
    output_file.writelines(linha)
    linha = 'Média;Mediana;Moda;Variância;Desvio Padrão\n'
    output_file.writelines(linha)

    linha = str(round(statistics.mean(resultadoFinal),4)) + ';' \
          + str(round(statistics.median(resultadoFinal),4)) + ';' \
          + str(round(statistics.mode(resultadoFinal),4)) + ';' \
          + str(round(statistics.variance(resultadoFinal),4)) + ';' \
          + str(round(statistics.stdev(resultadoFinal),4)) + '\n'

    output_file.writelines(linha)

    output_file.close()
