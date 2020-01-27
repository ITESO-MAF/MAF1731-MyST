
# -- ------------------------------------------------------------------------------------ -- #
# -- Proyecto: Describir brevemente el proyecto en general                                -- #
# -- Codigo: RepasoPython.py - describir brevemente el codigo                             -- #
# -- Repositorio: https://github.com/                                                     -- #
# -- Autor: Nombre de autor                                                               -- #
# -- ------------------------------------------------------------------------------------ -- #

import plotly.graph_objects as go
import plotly.io as pio                           # renderizador para visualizar imagenes
pio.renderers.default = "browser"                 # render de imagenes para correr en script


# -- --------------------------------------------------------- GRÁFICA: velas OHLC Simple -- #
# -- ------------------------------------------------------------------------------------ -- #
# -- --- Velas tipo candlestick utilizando precios tipo OHLC

def g_velas(p0_de):
    """
    Parameters
    ----------
    p0_de : pd.DataFrame : Precios OHLC como datos de entrada

    Returns
    -------
    fig : plotly figure : Grafica final

    Debugging
    ---------
    datos_dd = pd.DataFrame({'timestamp': [], 'open': [], 'high': [], 'low': [], 'close': []},
                              index=[])

    """

    p0_de.columns = [list(p0_de.columns)[i].lower() for i in range(0, len(p0_de.columns))]

    fig = go.Figure(data=[go.Candlestick(x=p0_de['timestamp'],
                                         open=p0_de['open'], high=p0_de['high'],
                                         low=p0_de['low'], close=p0_de['close'])])

    fig.update_layout(margin=go.layout.Margin(l=50, r=50, b=20, t=50, pad=0),
                      title=dict(x=0.5, y=1, text='Precios Historicos OHLC'),
                      xaxis=dict(title_text='Hora del dia', rangeslider=dict(visible=False)),
                      yaxis=dict(title_text='Precio del EurUsd'))

    fig.layout.autosize = False
    fig.layout.width = 840
    fig.layout.height = 520

    return fig


# -- ----------------------------------------------------------- GRÁFICA: Boxplot de PIPS -- #
# -- ------------------------------------------------------------------------------------ -- #
# -- --- Utilizando diferencias de precios expresadas en PIPS

def g_boxplot_varios(p0_data, p1_norm):
    """
    Parameters
    ----------
    p0_data : pd.DataFrame : Datos de entrada en formato OHLC
    p1_norm : bool : Para normalizar o no los datos de entrada

    Returns
    -------

    Debugging
    ---------

    """
    x_data = list(p0_data.columns)

    if p1_norm:
        y_data = [p0_data.iloc[:, i]/max(p0_data.iloc[:, i])
                  for i in range(0, len(list(p0_data.columns)))]
    else:
        y_data = [p0_data.iloc[:, i] for i in range(0, len(list(p0_data.columns)))]

    fig = go.Figure()

    for xd, yd in zip(x_data, y_data):
        q1 = yd.quantile(0.25)
        q3 = yd.quantile(0.75)
        iqr = q3 - q1
        out_yd = list(yd[(yd < (q1 - 1.5 * iqr)) | (yd > (q3 + 1.5 * iqr))].index)

        fig.add_trace(go.Box(y=yd, name=xd, boxpoints='all', jitter=0.5, whiskerwidth=0.5,
                             marker_size=7, line_width=1, boxmean=True,
                             selectedpoints=out_yd))

    fig.update_layout(title='Visualizacion de todas las variables',
                      yaxis=dict(autorange=True, showgrid=True, dtick=5,
                                 gridcolor='rgb(255, 255, 255)', gridwidth=1),
                      margin=dict(l=40, r=30, b=80, t=100),
                      showlegend=False)

    fig.update_yaxes(hoverformat='.2f')

    # Mostrar figura
    # fig.show()

    return fig
