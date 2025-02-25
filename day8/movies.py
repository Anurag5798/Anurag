import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler

df = pd.read_csv('movies.csv')
print(df)
print(df.info())
print(df.describe())
print(df.isnull().sum())
df = df.fillna(0).replace([np.inf, -np.inf], 0)
df[df.select_dtypes(include=['float']).columns] = df.select_dtypes(include=['float']).astype(int)
print(df)
print(df.isnull().sum())

sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))
sns.histplot(df["WorldGross"], bins=20, kde=True, color="blue")
plt.title("Distribution of World Gross", fontsize=14, fontweight='bold')
plt.xlabel("World Gross (in millions)")
plt.ylabel("Frequency")
plt.show()

top_movies = df.nlargest(10, "WorldGross")
plt.figure(figsize=(10, 6))
sns.barplot(y=top_movies["Movie"], x=top_movies["WorldGross"], palette="viridis")
plt.title("Top 10 Highest-Grossing Movies", fontsize=14, fontweight='bold')
plt.xlabel("World Gross (in millions)")
plt.ylabel("Movie")
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(x="Budget", y="Genre", data=df, palette="Set2")
plt.title("Budget Distribution by Genre", fontsize=14, fontweight='bold')
plt.xlabel("Budget (in millions)")
plt.ylabel("Genre")
plt.show()

plt.figure(figsize=(12, 6))
corr_matrix = df.select_dtypes(include=["number"]).corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap", fontsize=14, fontweight='bold')
plt.show()

studio_gross = df.groupby("LeadStudio")["WorldGross"].sum().nlargest(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=studio_gross, y=studio_gross.index, palette="magma")
plt.title("Top 10 Studios by Total World Gross", fontsize=14, fontweight='bold')
plt.xlabel("Total World Gross (in billions)")
plt.ylabel("Lead Studio")
plt.show()
