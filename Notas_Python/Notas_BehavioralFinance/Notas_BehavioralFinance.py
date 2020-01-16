
# -- ------------------------------------------------------------------------------------------------------------- -- #
# -- script: Notas_BehavioralFinance.py
# -- funcionalidad: Exploracion de Behavioral Finance para analisis de historico de trading de un trader manual
# -- repositorio:
# -- ------------------------------------------------------------------------------------------------------------- -- #

# Importar dependencias
import pandas as pd
import Notas_BehavioralFinance.Funciones_BehavioralFinance as fn

# Opciones para visualizar data frames en consola
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

datos = fn.f_leerarchivo(p0_parametro='Notas_BehavioralFinance/archivo_tradeview_0.json')

# IDEAS
# Disposition Effect
# -- Cortar mas rapido las ganancias que las perdidas

# Loss aversion (Variacion 1)
# -- Cerrar operacion con stop loss antes que alcanzara stop loss

# Sobre confianza
# -- Hacer "demasiadas" operaciones: mas de 5 operaciones en una misma cuenta

