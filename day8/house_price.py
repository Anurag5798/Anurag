import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("Book2.csv")
print(df.head())
print(df.info())
print(df.isnull().sum())

df['Brick'] = LabelEncoder().fit_transform(df['Brick'])
df['Neighborhood'] = LabelEncoder().fit_transform(df['Neighborhood'])
print(df)

plt.figure(figsize=(8, 5))
sns.histplot(df["Price"], bins=30, kde=True, color="blue")
plt.title("House Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["SqFt"], y=df["Price"], alpha=0.6, color="red")
plt.title("Price vs. Square Footage")
plt.xlabel("Square Footage (SqFt)")
plt.ylabel("Price")
plt.show()

plt.figure(figsize=(10, 5))
sns.boxplot(x=df["Bedrooms"], y=df["Price"], palette="coolwarm")
plt.title("Price vs. Number of Bedrooms")
plt.xlabel("Number of Bedrooms")
plt.ylabel("Price")
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(x=df["Neighborhood"], y=df["Price"], estimator=np.mean, palette="magma")
plt.xticks(rotation=45)
plt.title("Average House Price by Neighborhood")
plt.xlabel("Neighborhood")
plt.ylabel("Average Price")
plt.show()

plt.figure(figsize=(6, 5))
sns.boxplot(x=df["Brick"], y=df["Price"], palette="coolwarm")
plt.title("Impact of Brick Houses on Price")
plt.xlabel("Brick House (Yes/No)")
plt.ylabel("Price")
plt.show()
