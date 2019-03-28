
from datos import cuentas

import pandas as pd
import oandapyV20
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.transactions as trans


# -- Crear csv con historico de balance y operaciones de x

client = oandapyV20.API(access_token=cuentas['x']['acc_tk'])
r = accounts.AccountSummary(cuentas['x']['acc_id'])
client.request(r)
datos = pd.DataFrame(r.response)
print(datos['account']['balance'])
print(datos['account']['unrealizedPL'])
print(datos['account']['openTradeCount'])