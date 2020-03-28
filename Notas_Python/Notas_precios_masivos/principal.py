
# .. ................................................................................... .. #
# .. Proyecto: Descarg de Precios Masivos                                                .. #
# .. Archivo: principal.py - script con ejemplos de como utilizar la funcion             .. #
# .. Desarrolla: Francisco ME                                                            .. #
# .. Licencia: Open Source                                                               .. #
# .. Repositorio: https://github.com/                                                    .. #
# .. ................................................................................... .. #

import pandas as pd
import funciones as fn
import datos as dt

oa_in = "USD_MXN"  # Instrumento
oa_gn = "M1"       # Granularidad de velas (M1: Minuto, M5: 5 Minutos, M15: 15 Minutos)
fini = pd.to_datetime("2019-01-01 00:00:00").tz_localize('GMT')  # Fecha inicial
ffin = pd.to_datetime("2020-01-03 00:00:00").tz_localize('GMT')  # Fecha final

precios = fn.f_precios_masivos(p0_fini=fini, p1_ffin=ffin, p2_gran=oa_gn,
                               p3_inst=oa_in, p4_oatk=dt.oa_token, p5_ginc=4900)
