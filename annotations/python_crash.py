# %%
seq2 = [1, 2, 3, 4, 5]
# %%
for num in seq:
    print('hello')
# %%

i = 1
while i <= 5:
    print('i is {}'.format(i))
    i += 1

# %%

list(range(0, 5))
list(range(10))
list(range(-1))

# %%

a = []
x = range(1, 20)
for num in x:
    a.append(num**2)

a
# %%
# list as created
type([num**2 for num in x])
# %%

# functions
""" 
uma função para criar a tabuada do numero passado do 0 até o 10 
"""
def my_func(number: int):
    for i in range(0, 11):
        print(f'{number} x {i} = {number * i}')


# %%
"""
docstrings servers para documentação 
"""
my_func(5)
# %%
seq = [1,2,3,4,5,6,7]
# %%
type(map(seq,seq2))
# %%
i =  lambda number: number ** 3
# %%
i(80)
# %%
# iterando elementos com lambda e map
# map serve para iterar elementos, ele passou a expressão lambda em cada item da lista
salve = list(map(lambda num: num**3,seq))
salve
# %%
pares = list(filter(lambda num: num%2 == 0, salve))
pares
# %%
# metodos
# upper transforma todos os elementos da string em maiusculo 
s = 'my names is eduardo'
s.upper()
# %%
# lower transforma todos os elementos da string em minusculo
i = 'HOMEM DE FERRO MORRER FOI A PIOR DECISÃO DA MARVEL'
i.lower()
# %%
# split divide as strings de acordo com uma string passada, 1 é o numero de cortes que é pra ele fazer
o = 'a s #sf fdsd#  dd#ddd f !Salve #favela venceu!!' 
o.split('#',1)
# %%
d = {'k1':1,'k2':2}

# %%
# retorna as chaves do dicionario
print(d.keys())
# retorna as chaves com seus itens
print(d.items())
# retorn os valores contidos dentro de cada chave no dicionario
print(d.values())
# %%
list = [1,2,3,4,5,6,7]

# %%
# remove o elemento da posição passada 
list.pop(4)
list
# %%
# append coloca o item no ultimo lugar da lista
list.append(90)
list

# %%
p = [(1,2),(3,4),(5,6)]
# %%
print(type(p))
for (a,b) in p:
    print(b)
    print(a)