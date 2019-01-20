

# -- Hacer la inicializacion para plotly en linea
# -- https://plot.ly/python/getting-started/#initialization-for-online-plotting

from Notas_Herramientas.Precios_Oanda import Precios
import plotly.graph_objs as go
import plotly.plotly as py
import plotly.offline as offline

# -- Convertir las fechas a strings
Precios['TimeStamp'] = Precios['TimeStamp'].dt.strftime('%d/%m/%y %H:%M')

# -- Lista de fechas desde n1 hasta ntotal de npaso tamaño de paso
lista = []
for i in range(0, len(Precios['TimeStamp']), 3):
    lista.append(Precios['TimeStamp'][i])

# -- ---------------------------------------------------------------- Serie de tiempo -- Linea -- #
# -- ---------------------------------------------------------------- ------------------------ -- #

# -- capa de trazo 1
Trazo1 = go.Scatter(x=Precios['TimeStamp'], y=Precios['Close'])

# -- capa de layout de formato
layout = dict(xaxis=dict(autorange=True, showgrid=True, zeroline=True, showline=True,
                         ticks='inside', tickmode='array', tickvals=lista, ticktext=lista),
              yaxis=dict(autorange=True, showgrid=True, zeroline=True, showline=True,
                         ticks='inside', showticklabels=True))

# -- capa de trazos
data = [Trazo1]

# -- diccionario con toda la info
fig = dict(data=data, layout=layout)

# -- ----------------------------------------------------------- Serie de tiempo -- Velas OHLC -- #
# -- ----------------------------------------------------------- ----------------------------- -- #

# -- capa de trazo 1
Trazo1 = go.Candlestick(x=Precios['TimeStamp'], open=Precios['Open'], high=Precios['High'],
                        low=Precios['Low'], close=Precios['Close'])

# -- capa de layout de formato
layout = dict(xaxis=dict(autorange=True, showgrid=True, zeroline=True, showline=True,
                         ticks='inside', tickmode='array', tickvals=lista, ticktext=lista),
              yaxis=dict(autorange=True, showgrid=True, zeroline=True, showline=True,
                         ticks='inside', showticklabels=True))

# -- capa de trazos
data = [Trazo1]

# -- diccionario con toda la info
figg = dict(data=data, layout=layout)

# -- plot offline desde editor
offline.plot(figg, filename='simple_candlestick')

# -- plot online desde jupyter
# py.iplot(fig)

# -- plot offline desde jupyter
offline.plot(fig)

