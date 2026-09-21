import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('diabetes.csv')
print(data.head())
print(data.tail())

print(data.describe())

print(data.info()) #shows how many null values there are
print(data.isna().sum()) #null values in columns

print(data.duplicated().sum()) #shows duplicates in dataset


#############################
# DATA VISUALISATION #
#############################

plt.figure(figsize=(12,6)) # matplot fig
sns.countplot(x = 'Outcome', data = data) # seaborn countplot
plt.show()

#observing outliers
plt.figure(figsize=(10,10))
for i, col in enumerate(data.columns):
    plt.subplot(3,3,i+1)
    sns.boxplot(x = col, data = data)
plt.show() # shows how many outliers there are

sns.pairplot(data = data, hue = 'Outcome', height = 1.5)
plt.show() # shows relationships between columns

