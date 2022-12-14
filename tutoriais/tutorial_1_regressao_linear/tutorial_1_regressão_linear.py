# -*- coding: utf-8 -*-
"""Tutorial 1 - Regressão Linear.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KiP5ojTZjq-6VxbN3VzSaOpyeKf9W38k

imports das lib
"""

import pandas as pd
import numpy as np
import math as math
from sklearn import linear_model

"""caminho do **dataset**"""

path_to_ds = "/content/drive/MyDrive/Colab Notebooks/IA/bcc/tutorial_1_regressão_linear/candidatos.csv"

"""leitura do .csv **dataset**"""

df = pd.read_csv(path_to_ds)

"""exibição do **dataset**"""

df

"""transformar as celulas string da coluna *'experience'* do **dataset** para int"""

xp = {
    'zero':0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15, 
    }

array = df["experience"].copy()
for index, cel in enumerate(array):
  if type(cel) is str and not pd.isnull(cel):
    df["experience"][index] = xp[cel]

"""ccalcular média da coluna *'experience'* e *'test_score'* e alterar os valores nulos *'NaN'* do **dataset**"""

median_experience = math.floor(df["experience"].median())
df["experience"] = df["experience"].fillna(median_experience)

median_test_score = math.floor(df["test_score"].median())
df["test_score"] = df["test_score"].fillna(median_test_score)

"""exibição do **dataset** com *'NaN'* corrigido"""

df

"""trinando o modelo"""

reg = linear_model.LinearRegression()
reg.fit(df[['experience', 'test_score', 'interview_score']], df['salary'])

"""exibindo os coeficientes"""

reg.coef_

"""testando para um novo colaborador com: 1 ano de experiência, tirou 7 no teste técnico e 8 na entrevista"""

collaborator = [[1, 7.0, 8]]
reg.predict(collaborator)

"""o slário ideial para esse colaborador a partir do modelo é: $46501.52 anual"""