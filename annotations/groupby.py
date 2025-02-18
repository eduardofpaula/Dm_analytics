#%%
import pandas as pd

# %%
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

# %%
# cria um DataFrame a partir do dicionário
df = pd.DataFrame(data)
df
# %%
# agrupa os dados por empresa
byComp = df.groupby("Company")

# %%
# calcula a média das vendas de cada empresa
byComp.mean('Sales')
# %%
# calcula a soma das vendas de cada empresa
byComp.sum('Sales')

# %%
# calcula o desvio padrão das vendas de cada empresa
byComp['Sales'].std()

# %%
# calcula o menor valor de vendas de cada empresa
byComp.min('Sales')

# %%
# calcula o maior valor de vendas de cada empresa
byComp.max('Sales')

# %%
# calcula a contagem de vendas de cada empresa
byComp.count()
# %%