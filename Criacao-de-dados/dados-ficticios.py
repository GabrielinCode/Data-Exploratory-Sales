#!/usr/bin/env python
# coding: utf-8

# # Criação de dados para a análise

# In[2]:


import pandas as pd
import random


# In[3]:


# Criação do conjunto de dados fictício
data = {
    'Data': pd.date_range(start='2023-01-01', end='2023-12-31'),
    'Produto': random.choices(['Produto A', 'Produto B', 'Produto C'], k=365),
    'Região': random.choices(['Região 1', 'Região 2', 'Região 3', 'Região 4'], k=365),
    'Valor': [random.uniform(100, 1000) for _ in range(365)]
}


# In[6]:


data


# In[9]:


#transformando o conjunto de dados em uma dataframe

df = pd.DataFrame(data)


# In[7]:


df


# In[10]:


# Salva o conjunto de dados em um arquivo CSV
df.to_csv('dados_vendas.csv', index=False)

