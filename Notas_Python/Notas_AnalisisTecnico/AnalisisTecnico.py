
# -- ------------------------------------------------------------- Importar modulos a utilizar -- #
# -- ------------------------------------------------------------- --------------------------- -- #

import ta as ta
import pandas as pd
from oandapyV20 import API
import oandapyV20.endpoints.instruments as instruments
import plotly.graph_objs as go
import plotly as py
from Notas_AnalisisTecnico.AnalisisBase import *

# -- ------------------------------------------------------------------- Parametros para OANDA -- #
# -- ------------------------------------------------------------------- --------------------- -- #

pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 200)
pd.set_option('display.width', 1000)

# -- ---------------------------------------------------------------------------- Cargar datos -- #
# -- ---------------------------------------------------------------- ------------------------ -- #

# -- Precios


# -- ---------------------------------------------------------------- Agregar analisis tecnico -- #
# -- ---------------------------------------------------------------- ------------------------ -- #


# -- ---------------------------------------------------------------- Agregar analisis tecnico -- #
# -- ---------------------------------------------------------------- ------------------------ -- #

pd_hist['ema_Close'] = ta.ema(series=pd_hist['Close'], periods=20)

# -- ------------------------------------------------------------------- --------------------- -- #
# -- ------------------------------------------------------------------- --------------------- -- #

trace0 = go.Scatter(x=pd_hist['TimeStamp'], y=pd_hist['ema_Close'],
                    mode='lines', name='lines0')

trace1 = go.Scatter(x=pd_hist['TimeStamp'], y=pd_hist['Close'],
                    mode='lines', name='lines1')

data = [trace0, trace1]

py.offline.plot(data, filename='Grafica_1.html')
