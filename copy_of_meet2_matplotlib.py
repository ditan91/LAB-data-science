# -*- coding: utf-8 -*-
"""Copy of Meet2 Matplotlib.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OeueUNc3s51E9NXxTNWDrGRaoMomKgD0
"""

import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as plt

print(f"Version Pandas : {pd.__version__}")
print(f"Version Matplotlib : {mp.__version__}")
pd.set_option("max_columns",None)

!gdown --id 1uQmrIlMDR5bQAJt5IvJTjsMSBXCZ-Cdo

df = pd.read_csv('RAWtrain.csv')

df.columns = [i.lower() for i in df.columns]
df.head(1)

"""### Scatter plot < 2 numeric values > """

df["mssubclass"]

plt.plot(df["mssubclass"],df["saleprice"],"o")
plt.title("msSubClass")
plt.xlabel("Sale Price")
plt.show()

"""### Scatter plot < 2 numeric values >  """

plt.plot(df["grlivarea"],df["saleprice"],"o")
plt.title("grlivarea")
plt.ylabel("Sale Price")
plt.show()

"""### Barplot < 1 Categorical  1 Numeric > """

plt.bar(df["heating"],df["saleprice"])
plt.title("heating")
plt.ylabel("Sale Price")
plt.show()

plt.plot(df["saleprice"],df["saleprice"])
plt.title("saleprice")
plt.ylabel("Sale Price")
plt.show()

import seaborn as sns # Lebih baik lagi dari MPL
plt.figure(figsize=(10,8))
sns.barplot(df["heating"],df["saleprice"])

df[df["heating"] == "Grav"]["saleprice"].mean()

df.shape

plt.figure(figsize=(12,8))
sns.countplot(x = df["heating"])

sale = df[df["heating"] == "GasA"]["saleprice"]
count = range(0,df[df["heating"] == "GasA"]["id"].count())
plt.figure(figsize=(10,7))
sns.scatterplot(count,sale)

for i in df["heating"].unique():
    sale = df[df["heating"] == i]["saleprice"]
    count = range(0,df[df["heating"] == i]["id"].count())
    plt.figure(figsize=(10,8))
    sns.scatterplot(count,sale)   
    plt.title(i)
    plt.xlabel("count")
    plt.show()

df.columns

for i in df["heating"].unique():
    dfonlyGasI = df[df["heating"] == i]
    sale = df[df["heating"] == i]["saleprice"]
    count = range(0,df[df["heating"] == i]["id"].count())
    plt.figure(figsize=(15,8))
    sns.scatterplot(x = count,y = sale,hue=dfonlyGasI["alley"]) 
    plt.title(i)
    plt.xlabel("count")
    plt.show()

df[df["heating"] == "Floor"]

plt.figure(figsize=(12,10))
sns.boxplot(df["lotconfig"],df["saleprice"])

plt.figure(figsize=(12,10))
sns.violinplot(x = "lotconfig",y ="saleprice",data=df)

plt.figure(figsize=(12,10))
sns.boxenplot(x = "lotconfig", y="saleprice",data = df)

df.loc[df["lotconfig"] == "Inside","saleprice"].describe()

sns.barplot(x="lotconfig",y="saleprice",data =df)

#Euclidian
index = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17']
plt.bar(index, Jarak_Euclidian)
plt.title("Jarak Euclidean")
plt.ylabel("Jarak Euclidean")
plt.show()

plt.bar(mobil_terbaik, hasil)
plt.title("3 Mobil Terbaik")
plt.ylabel("Jarak Euclidean")
plt.show()