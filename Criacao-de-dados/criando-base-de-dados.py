#!/usr/bin/env python
# coding: utf-8

# # relatório de Análise I

# ## Importando a base de dados

# In[12]:


import pandas as pd


# In[13]:


pd.read_csv('dados/aluguel.csv',sep = ';')


# In[14]:


dados = pd.read_csv('dados/aluguel.csv', sep = ';')


# In[15]:


dados


# In[16]:


type(dados)


# In[17]:


dados.info()


# In[18]:


dados.head()


# ## informações gerais sobre a base de dados

# In[19]:


dados.dtypes


# In[23]:


tipos_de_dados = pd.DataFrame(dados.dtypes, columns = ['tipos de dados'])


# In[25]:


tipos_de_dados.columns.name = 'variaveis'


# In[26]:


tipos_de_dados


# In[27]:


dados.shape


# In[28]:


dados.shape[0]


# In[29]:


print('A base de dados apresenta {} registros (imoveis) e {} variaveis'.format(dados.shape[0], dados.shape[1]))


# In[ ]:




