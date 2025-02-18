# %%
import numpy as np
import pandas as pd

# %%
df = pd.DataFrame({'A':[1,2,np.nan],
                  'B':[5,np.nan,np.nan],
                  'C':[1,2,3]})
df
# %%
# dropa todas as linhas com valores faltantes
df.dropna()
# %%
# dropa todas as colunas com valores faltantes
df.dropna(axis=1)
# %%
# dropa todas as linhas com 2 ou mais valores faltantes
df.dropna(thresh=2)
# %%
# preenche os valores faltantes com o valor 0
df.fillna(value='Value Not Found')
# %%
# preenche os valores faltantes com a média dos valores da coluna
df['A'].fillna(value=df['A'].mean())