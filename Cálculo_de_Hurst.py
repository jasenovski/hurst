import numpy as np
import pandas as pd
import metodo_minimos_quadrados as mmq

def Hurst(dados):

    """
    :param dados: Este parâmetro deve estar estruturado como um array
    :return: O retorno deverá ser o coeficiente angular da reta média de dados logaritmizados (entropizados)
    """

    bd_auxiliar = dados

    qtd_dados = len(bd_auxiliar)

    dados_interno = np.zeros(qtd_dados)
    serie1 = np.zeros(qtd_dados - 1)
    serie2 = np.zeros(qtd_dados - 1)
    y = np.zeros(qtd_dados + 1)
    dados_interno[0] = bd_auxiliar[0]
    dados_interno[1] = bd_auxiliar[1]
    contador = 2
    soma = 0
    for i in range(0, qtd_dados - 1, 1):
        serie1[i] = np.log2(contador)
        media = np.mean(dados_interno[:contador])
        for j in range(1, contador + 1, 1):
            y[j] = y[j - 1] + (dados_interno[j - 1] - media)
        y_max = np.max(y[:contador])
        y_min = np.min(y[:contador])
        for j in range(0, contador, 1):
            soma = soma + np.square(dados_interno[j] - media)
        desvio_padrao = np.sqrt(soma / len(dados_interno[:contador]))
        soma = 0
        serie2[i] = np.log2((y_max - y_min) / desvio_padrao)
        contador = contador + 1
        if contador <= qtd_dados:
            for k in range(0, contador, 1):
                dados_interno[k] = bd_auxiliar[k]

    # a = 0
    # b = 0
    # c = 0
    # d = 0
    # e = 0
    # f = 0
    #
    # for i in range(0, qtd_dados - 1, 1):
    #     a = a + (2 * np.square(serie1[i]))
    #
    # for i in range(0, qtd_dados - 1, 1):
    #     b = b + (2 * serie1[i])
    #
    # for i in range(0, qtd_dados - 1, 1):
    #     c = c + (-2 * serie1[i] * serie2[i])
    #
    # c = c * (-1)
    #
    # for i in range(0, qtd_dados - 1, 1):
    #     d = d + (2 * serie1[i])
    #
    # e = 2.0 * (qtd_dados - 1)
    #
    # for i in range(0, qtd_dados - 1, 1):
    #     f = f + (2 * (-1) * serie2[i])
    # f = f * (-1)

    # matriz_um = [[a, b],
    #              [d, e]]
    #
    # matriz_dois = [c, f]

    # print("Seguem os valores para a matriz um: ", matriz_um)
    # print("Seguem os valores para a matriz dois: ", matriz_dois)

    # valor_coef_ang = (-(f * b) + (c * e)) / ((a * e) - (d * b))
    #
    # valor_coef_lin = ((f * a) - (c * d)) / ((a * e) - (d * b))

    valor_coef_ang, valor_coef_lin = mmq.mmq_reta(serie1, serie2)

    return valor_coef_ang