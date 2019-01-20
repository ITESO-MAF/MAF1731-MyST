
# -- ------------------------------------------------------------- Importar modulos a utilizar -- #
# -- ------------------------------------------------------------- --------------------------- -- #

import pandas as pd
from oandapyV20 import API
import oandapyV20.endpoints.instruments as instruments

# -- ------------------------------------------------------------------- Parametros para OANDA -- #
# -- ------------------------------------------------------------------- --------------------- -- #

A1_OA_Da = 16                     # Day Align
A1_OA_Ta = "America/Mexico_City"  # Time Align

A1_OA_Ai = "101-004-2221697-001"  # Id de cuenta
A1_OA_At = "practice"             # Tipo de cuenta

A1_OA_In = "USD_MXN"              # Instrumento
A1_OA_Gn = "H4"                   # Granularidad de velas

A1_OA_Ak = "a" + "da4a61b0d5bc0e5939365e01450b614" + "-4121f84f01ad78942c46fc3ac777baa" + "6"

F1 = "2017-09-04T00:00:00Z"
F2 = "2017-09-21T00:00:00Z"

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

Precios = pd.DataFrame(lista)
Precios = Precios[['TimeStamp', 'Open', 'High', 'Low', 'Close']]
Precios['TimeStamp'] = pd.to_datetime(Precios['TimeStamp'])
