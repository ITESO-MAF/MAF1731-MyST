
# -- ------------------------------------------------------------------------------------------------------------- -- #
# -- script: Funciones_BehavioralFinance.py
# -- funcionalidad: Funciones para implementacion de Behavioral Finance en trading
# -- repositorio:
# -- ------------------------------------------------------------------------------------------------------------- -- #

import pandas as pd
import json


# -- ----------------------------------------------------------------------------------- Leer archivos xlsx y json -- #

def f_leerarchivo(p0_parametro):
    """
    :param p0_parametro: archivo de entrada
    :return: resultado

    para hacer pruebas
    p0_parametro = 'archivo_tradeview_0.json'
    """

    # datos = pd.read_excel('Historico.xlsx', sheet_name='Hoja1')

    # ingreso de datos de entrada: leer archivo JSON
    with open(p0_parametro, encoding='utf-8-sig') as json_file:
        datos_2 = json.load(json_file)['data']

    # Seleccionar la seccion de 'closedTransactions" que es la de interes
    df_datos = pd.DataFrame(datos_2['closedTransactions']['list'])

    # Seleccionar solo los renglones de operaciones
    df_datos = df_datos[(df_datos['type'] == 'buy') | (df_datos['type'] == 'sell') |
                        (df_datos['type'] == 's/l')
                        | (df_datos['type'] == 't/p')]

    # Resetear index para tener todos los numeros de indice completos
    df_datos = df_datos.reset_index(drop=True)

    # Eliminar columas 'info' e index
    df_datos = df_datos.drop(['info'], 1)

    # renombrar columnas
    df_datos.rename(columns={'SL': 'sl', 'TP': 'tp', 'price': 'openPrice',
                             'price2': 'closePrice', 'item': 'instrument'},
                    inplace=True)

    return df_datos
