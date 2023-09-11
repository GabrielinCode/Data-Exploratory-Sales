

# # Análise Exploratória

# ## Tratamento dos dados

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


#importando os dados 
dados = pd.read_csv('Arquivos/dados_vendas.csv')


# In[7]:


#verificando os dados

print(dados.head())


# In[8]:


print(dados.info())


# In[9]:


#tratando dados ausentes

dados.dropna(inplace=True) #remove as linhas com valores null , o parametro "inplace" esta como true por que as alterações devem ser feitas no proprio dataframe
dados.reset_index(drop=True, inplace= True) #reseta os indices após a remoção, o parametro "drop" esta como true por que o indice atual vai ser removido após a mudança 


# In[10]:


#tratando os tipos de dados

dados['Data'] = pd.to_datetime(dados['Data']) #convertendo a coluna 'Data' de object para o tipo datetime


# In[11]:


#verificando os dados após as alterações 

print(dados.head())


# In[12]:


print(dados.info())


# ## Análise dos dados

# In[13]:


#Estatisticas basica dos dados

print(dados.describe())


# In[14]:


#visualização gráfica da destribuição dos valores de venda 

plt.figure(figsize=(8, 6))
sns.histplot(data=dados, x='Valor', bins=10)
plt.title('Distribuição dos Valores de Venda')
plt.xlabel('Valor')
plt.ylabel('Contagem')
plt.show()


# In[15]:


# analise por produtos, Agrupei todos os dados da coluna 'Produto' e somei todos os valores.

produto_vendas =dados.groupby('Produto')['Valor'].sum()
print(produto_vendas)


# In[16]:


# Visualização da relação de vendas entre os produtos

plt.figure(figsize=(8,5))
produto_vendas.plot(kind='bar')
plt.title('Vendas por Produto')
plt.xlabel('Produto')
plt.ylabel('Total de Vendas')
plt.show()


# ## Estudos Temporais 

# In[17]:


# Estudo temporal - vendas por mês 

# Converter a coluna para datetime já foi feito, então criei uma nova coluna 'Mês' no DataFrame
# que armazena o valor correspondente a cada mês extraido da coluna 'Data' através da função 'dt.month'.

dados['Mês'] = dados['Data'].dt.month
vendas_por_mes = dados.groupby('Mês')['Valor'].sum()

# Então agrupo os dados da coluna 'Mês' e calculo a soma dos valores da coluna 'Valor' para cada grupo de meses.
print(vendas_por_mes)


# In[18]:


# Estudo temporal - vendas por semestre

#como fiz antes criei uma nova coluna chamada 'Semestre' e então utilizei a função '(dados['Data'].dt.month - 1) // 6 + 1'
# para calcular o numero de semestres, primeira subtrai por 1 para ajustar o intervalo dos peses de 1 a 12 para 0 a 11, para que o intervalo dos meus meses seja contado certo
# então faço a divisão por 6 para dividir os meses de 0 a 5 para o primeiro semestre e os de 6 a 11 para o segundo semestre, no final somo mais um para cocertar os semestres
# que estavam 0 e 1, para 1 e 2

dados['Semestre'] = (dados['Data'].dt.month -1) // 6 + 1
vendas_por_semestre = dados.groupby('Semestre')['Valor'].sum()

print(vendas_por_semestre)


# In[19]:


dados['Semestre'] = (dados['Data'].dt.month) // 6 
vendas_por_semestre_teste = dados.groupby('Semestre')['Valor'].sum()

#se o mesmo codigo é executado sem as operações o computador interpreta como se existisse um mes 0 e acaba criando um terceiro semestre
# apenas para o mês 12, nesse caso o primeiro semeste esta com 1 mês a menos e o segundo com um mês a mais, já o terceiro é apenas um mês

print(vendas_por_semestre_teste)


# In[20]:


#Visualização do numero de vendas com relação aos meses

plt.figure(figsize=(8,6))
vendas_por_mes.plot(kind='line', marker='o')
plt.title('Vendas por Mês')
plt.xlabel('Vendas')
plt.ylabel('Total de Vendas')
plt.xticks(range(1,13)) #Utilizado para definir os rotulos do eixo x
plt.show


# In[21]:


#Visualização do numero de vendas por semestre

plt.figure(figsize=(8,6))
vendas_por_semestre.plot(kind='bar')
plt.title('Vendas por semestre')
plt.xlabel('Semestre')
plt.ylabel('Total de Vendas')
plt.xticks(range(2), ['Semestre 1', 'Semestre 2'])
plt.show()


# In[22]:


#Análise por Região, Agrupei os dados da coluna 'Região' e somei todos os valores 

regiao_vendas = dados.groupby('Região')['Valor'].sum()
print(regiao_vendas)


# In[23]:


#Visualização da relação entre Regiaão e Vendas

plt.figure(figsize=(8,6))
regiao_vendas.plot(kind='bar')
plt.title('Vendas por Região')
plt.xlabel('Região')
plt.ylabel('Total de Vendas')
plt.show()


# In[46]:


# Análise da relação entre produto e região

vendas_por_regiao_produto = dados.groupby(['Região', 'Produto'])['Valor'].sum().unstack()


# In[45]:


paleta_cores = sns.color_palette('Set3', n_colors=len(vendas_por_regiao_produto.index))


# In[47]:


#Visualização da relação entre produto e região

plt.figure(figsize=(10, 6))
vendas_por_regiao_produto.plot(kind='bar', color=paleta_cores)
plt.title('Vendas por Região e Produto')
plt.xlabel('Região e Produto')
plt.ylabel('Total de Vendas')
plt.legend(title='Região')
plt.show()


# In[24]:


# Análise Temporal e Regional
# Aproveitando da Coluna 'Mês' ja criada antes, agrupei os dados dela com o da região e somei os valores totais

vendas_por_mes_regiao = dados.groupby(['Mês', 'Região'])['Valor'].sum().unstack()
print(vendas_por_mes_regiao)


# In[25]:


plt.figure(figsize=(10, 6))
sns.lineplot(data=vendas_por_mes_regiao, markers=True)
plt.title('Vendas por Mês e Região')
plt.xlabel('Mês')
plt.ylabel('Total de Vendas')
plt.xticks(range(1, 13))
plt.legend(title='Região', loc='upper right')
plt.show()


# In[49]:


"""
Análise de vendas por dias da semana

Criei mais uma coluna 'DiasSemana' que guarda os dias da semana de acordo com os dados da coluna 'Data' através do dt.dayofweek
e atribui os valores dos dias da semana para 'dias_semana'.

"""

dados['DiasSemana'] = dados['Data'].dt.dayofweek
vendas_por_dia_semana = dados.groupby('DiasSemana')['Valor'].sum()
dias_semana = ['Seg', 'Ter','Qua', 'Qui', 'Sex', 'Sab', 'Dom']


# In[28]:


plt.figure(figsize=(8,6))
sns.barplot(x=dias_semana, y=vendas_por_dia_semana)
plt.title('Vendas por Dia da Semana')
plt.xlabel('Dias da Semana')
plt.ylabel('Total de Vendas')
plt.show()


# In[33]:


plt.figure(figsize=(10,6))
sns.boxplot(data=dados, x='Produto', y='Valor', hue='Região')
plt.title('Destribuição das Vendas por Produto e Região')
plt.xlabel('Produto')
plt.ylabel('valor')
plt.show()


# # Insights Finais

# ## Vendas Gerais

#      A partir da análise do grafico de Vendas totais dos produtos notou-se que o Produto C se apresentou como favorito pelo publico, enquanto o Produto A teve um numero de vendas mais baixo. Isso sugere de que o produto C é popular entre os clientes, porém o produto A necessita de uma estratégia de marketing adicional com intuito de impulsionar as vendas. Já o Produto B se apresentou mediano entre as vendas do A e do C, isso infere que ele não esta com numeros de venda a baixo do comum, porem, partindo do prssuposto de que as vendas de C são ideais, o Produto B precisa ter seu desempenho futuro análisado com cautela para prevenir possiveis baixas, e estudar formas para impulsionar sua popularidade.

# ## Análises Temporais

# Diante da análise da relação de vendas com os meses, foi-se possivel perceber um grande aumento nas vendas nos períodos do meses 9, 10, 11, 12 e 1, que correspondem respectivamente ao período da primavera e a maior parte do verão. Logo é possível concluir que o produto é mais popular em epocas mais quentes e ensolaradas. A partir dessas informações é póssível planejar estrategias de marketing sazonais e otimizar o estoque de acordo com a demanda.

# É possivel também observar que no primeiro semestre, embora os meses 1 e 6 tenham desempenhos muito bons, no seu geral tem o desempenho consideravelmente menor que no segundo semestre do ano. Como já analizamos antes é de se esperar que o produto tenha desempenho melhor nas epocas de primavera e verão, contudo diante do estudo mostra-se necessário um esforço maior no engajamento dos produtos no mercado nos períodos mais frios, com intuito de melhorar as vendas.

# Foi também observado a partir do grafico de relação entre vendas e dias da semana, que nos dias, Terça, Quarta e Quinta, as vendas tendem a ser maiores, e nos finais de semanas tendem a cair, o que sugere que o cliente tem como preferencia comprar no meio da semana e não muito em dias de final de semana e feriados. Portanto a partir disso é possivel desenvolver estrategias de promoção e marketing que casem com o costume de compra dos clientes.

# ## Análises Regionais

#  A partir da Análise da relação de vendas regionais, foi possivel se observar que a Região 4 se destacou porem a 1 e 2 mostraram ter o menor numero de vendas. Desta forma, é possível assumir que a Região 4 se tem o potencial grande, fazendo de si um mercado importante, exigindo foco adicional para maximizar o potencial de vendas, no entanto as regioes 1 e 2 mostram necessitar de esforços maiores para melhorar a participação no mercado.

# In[ ]:




