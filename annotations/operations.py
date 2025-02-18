#%%
import pandas as pd
import numpy as np
# %%
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df
# %%
# retorna os valores únicos da coluna col2
df['col2'].unique()
# %%
# retorna a quantidade de valores únicos da coluna col2
df['col2'].nunique()
# %%
# retorna a quantidade de vezes que cada valor aparece na coluna col2
df['col2'].value_counts()
# %%
# retorna os valores da coluna col1 que são maiores que 2
newdf = df[(df['col1']>2) & (df['col2']==444)]
newdf
# %%
def times2(x):
    return x*2
# %%
# aplica a função times2 a coluna col1
df['col1'].apply(times2)
# %%
# aplica a função lambda a coluna col3 que retorna o tamanho de cada string
df['col3'].apply(len)
# %%
# retorna a soma dos valores da coluna col1
df['col1'].sum()
# %%
# ordena os valores da coluna col2
df.sort_values(by='col2')
# %%
# retorna os valores da coluna col2 que são nulos
df.isnull()
# %%
# remove as linhas que contém valores nulos
df.dropna()
# %%
df1 = pd.DataFrame({'col1':[1,2,3,np.nan],
                   'col2':[np.nan,555,666,444],
                   'col3':['abc','def','ghi','xyz']})
df1