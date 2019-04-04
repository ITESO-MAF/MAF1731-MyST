
# -- ------------------------------------------------------------- Importar modulos a utilizar -- #
# -- ------------------------------------------------------------- --------------------------- -- #

import ta as ta
import pandas as pd
from oandapyV20 import API
import oandapyV20.endpoints.instruments as instruments
import plotly.graph_objs as go
import plotly as py

# -- ------------------------------------------------------------------- Parametros para OANDA -- #
# -- ------------------------------------------------------------------- --------------------- -- #

pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 200)
pd.set_option('display.width', 1000)

# -- ------------------------------------------------------------------- Parametros para OANDA -- #
# -- ------------------------------------------------------------------- --------------------- -- #

A1_OA_Da = 17                     # Day Align
A1_OA_Ta = "America/Mexico_City"  # Time Align

A1_OA_Ai = "101-004-2221697-001"  # Id de cuenta
A1_OA_At = "practice"             # Tipo de cuenta

A1_OA_In = "USD_MXN"              # Instrumento
A1_OA_Gn = "H1"                   # Granularidad de velas

A1_OA_Ak = "a" + "da4a61b0d5bc0e5939365e01450b614" + "-4121f84f01ad78942c46fc3ac777baa" + "6"

F1 = "2017-01-01T00:00:00Z"
F2 = "2017-02-01T00:00:00Z"

# -- ---------------------------------------------------------------- Inicializar API de OANDA -- #
# -- ---------------------------------------------------------------- ------------------------ -- #

api = API(access_token=A1_OA_Ak)

# -- -------------------------------------------------------------- Obtener precios historicos -- #
# -- -------------------------------------------------------------- -------------------------- -- #

params = {"granularity": A1_OA_Gn, "price": "M", "dailyAlignment": A1_OA_Da,
          "alignmentTimezone": A1_OA_Ta, "from": F1, "to": F2}

A1_Req1 = instruments.InstrumentsCandles(instrument=A1_OA_In, params=params)
A1_Hist = api.request(A1_Req1)

lista = []
for i in range(len(A1_Hist['candles'])-1):
        lista.append({'TimeStamp': A1_Hist['candles'][i]['time'],
                      'Open': A1_Hist['candles'][i]['mid']['o'],
                      'High': A1_Hist['candles'][i]['mid']['h'],
                      'Low': A1_Hist['candles'][i]['mid']['l'],
                      'Close': A1_Hist['candles'][i]['mid']['c']})

pd_hist = pd.DataFrame(lista)
pd_hist = pd_hist[['TimeStamp', 'Open', 'High', 'Low', 'Close']]
pd_hist['TimeStamp'] = pd.to_datetime(pd_hist['TimeStamp'])


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
