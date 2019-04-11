# -- ----------------------------------------------------------------------------------------- -- #
# -- Codigos y funciones para trading en python ---------------------------------------------- -- #
# -- URL -- https://github.com/ITESOIF/MyST/blob/master/Notas_Python/FuncionesBase.py -------- -- #
# -- ------------------------------------------------------------- --------------------------- -- #

# -- ------------------------------------------------------------- Importar modulos a utilizar -- #
# -- ------------------------------------------------------------- --------------------------- -- #

import ta as ta
import pandas as pd
from oandapyV20 import API
import oandapyV20.endpoints.instruments as instruments
import plotly.graph_objs as go
import plotly as py
from datetime import date, datetime, timedelta
import datetime

# -- ------------------------------------------------------------------- Parametros para OANDA -- #
# -- ------------------------------------------------------------------- --------------------- -- #

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 200)
pd.set_option('display.width', 1000)

# -- ------------------------------------------------------------------- Parametros para OANDA -- #
# -- ------------------------------------------------------------------- --------------------- -- #

A1_OA_Da = 17                     # Day Align
A1_OA_Ta = "America/Mexico_City"  # Time Align

A1_OA_Ai = "101-004-2221697-001"  # Id de cuenta
A1_OA_At = "practice"             # Tipo de cuenta

A1_OA_In = "USD_MXN"              # Instrumento
A1_OA_Gn = "M5"                   # Granularidad de velas

A1_OA_Ak = '2' + '6b62ddbe404c61a1cc9da0ed8395945-52d44ef76c42b62460581783bba6c8e' + 'a'

FechaIni = "2017-03-10T00:00:00Z"
FechaFin = "2017-03-10T00:00:00Z"

# -- Vector de fechas


def date_range(start_date, end_date, increment, period):
    result = []
    nxt = start_date
    delta = relativedelta(**{period:increment})
    while nxt <= end_date:
        result.append(nxt)
        nxt += delta
    return result

start_date = date(2017, 3, 1)
end_date = date(2019, 3, 1)
fechas = date_range(start_date, end_date, 15, 'days')

F1 = fechas[0].strftime('%Y-%m-%dT%H:%M:%S')
F2 = fechas[1].strftime('%Y-%m-%dT%H:%M:%S')


# -- ---------------------------------------------------------------- Inicializar API de OANDA -- #
# -- ---------------------------------------------------------------- ------------------------ -- #

api = API(access_token=A1_OA_Ak)

# -- -------------------------------------------------------------- Obtener precios historicos -- #
# -- -------------------------------------------------------------- -------------------------- -- #


params = {"granularity": A1_OA_Gn, "price": "M", "dailyAlignment": A1_OA_Da,
          "alignmentTimezone": A1_OA_Ta, "from": F1  , "to": F2}

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

# -- -------------------------------------------------------------------- Estructuras de datos -- #
# -- ------------------------------------------------------------------- --------------------- -- #

# -- Paso 1 -- Data Frame (df1_precios) descargando todos los precios, segun fechas y granularidad
# -- -- Fecha, Apertura, Maximo, Minimo, Cierre.

# -- Paso 2 -- en Data Frame (df2_operaciones)
# -- -- Fecha, Folio (1 a n), Operacion (1 = compra, -1 = venta), Unidades (0 a n),
# -- -- Margen (0 a n), Comentario ("razon con base al indicador")
# -- -- Precio_apertura, Precio_cierre

# -- Paso 3 -- en Data Frame Cuenta (df3_cuenta)
# -- -- Fecha, Capital (Efectivo $), Flotante ($),
# -- -- Balance (Capital+Flotante), Rend_Balance_acm, Comentario ("Se abrio operacion: compra/venta",
# -- -- "Se cerro operacion: Con perdia de: / Con ganancia de: ",

# -- Paso 4 -- Generar un vector de fechas, de F1 hasta F2

par0_cap = 100000   # Capital a utilizar $100,000 Usd
par1_mar = 1000000  # Unidades por operacion maximo 1'000,000

# -- Criterios para trading
# -- para cerrar una operacion: 1) TP o SL, 2) Regla con indicador

# -- df1_precios

# -- df2_operaciones

indice = pd_hist['TimeStamp']
columnas = ['Folio', 'Operacion', 'Unidades', 'Margen', 'Comentario', 'Precio_apertura', 'Precio_cierre']
df2_operaciones = pd.DataFrame(index=indice, columns=columnas)
df2_operaciones = df2_operaciones.fillna(0)  # -- llenar todas las celdas con 0s


# -- df3_cuenta

indice = pd_hist['TimeStamp']
columnas = ['Folio', 'Operacion', 'Unidades', 'Margen', 'Comentario', 'Precio_apertura', 'Precio_cierre']
df2_operaciones = pd.DataFrame(index=indice, columns=columnas)
df2_operaciones = df2_operaciones.fillna(0)  # -- llenar todas las celdas con 0s
