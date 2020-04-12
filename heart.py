#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:17:17 2020

@author: isaac
"""
#Importar as bibliotecas para tratamento matemático, pré-processamento, gráficos e aplicação de modelos
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
df = pd.read_csv('/home/isaac/Documents/2019_PUC-RJ_BIMaster/201902_SAD/Data_Mining/Trabalho/heart.csv')
df.info()
#%%
df.head(10)
#%%
#Distribuição dos pacientes por sexo (1 = M; 0 = F)
df.sex.value_counts()
#%%
#Distribuição das idades e média
x = df.age.values
plt.hist(x, bins=15)
plt.show
media_idade = np.average(x)
print(media_idade)
#%%
#Distribuição das medições de colesterol e média
colesterol = df.chol.values
plt.hist(colesterol, bins=8)
plt.show
media_col = np.average(colesterol)
print(media_col)