import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler

df = pd.read_csv('employee.csv')
print(df.head())
print(df.isnull().sum())
df = df.dropna(subset=['Gender'])
print(df)
print(df.isnull().sum())
df = df.dropna(subset=['Senior Management'])
df = df.dropna(subset=['Team'])
print(df)
print(df.isnull().sum())
label_encoders = {}
for column in ["First Name", "Gender", "Senior Management", "Team"]:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column].astype(str))
    label_encoders[column] = le
print(df.head())
for column in df.select_dtypes(include=['float']).columns:
    df[column] = df[column].astype(int)
print(df)
plt.figure(figsize=(10, 5))
sns.barplot(x="Team", y="Salary", data=df, palette="viridis")
plt.xlabel("Team")
plt.ylabel("Salary")
plt.title("Salary Distribution per Team")
plt.xticks(rotation=45)
plt.show()
plt.figure(figsize=(8, 5))
sns.histplot(df["Salary"], bins=5, kde=True, color="blue")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.title("Salary Distribution")
plt.show()
plt.figure(figsize=(8, 5))
sns.boxplot(x="Gender", y="Salary", data=df, palette="coolwarm")
plt.xlabel("Gender (0 = Female, 1 = Male)")
plt.ylabel("Salary")
plt.title("Salary Distribution by Gender")
plt.show()
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Bonus %", y="Salary", data=df, hue="Gender", palette="Dark2", s=100)
plt.xlabel("Bonus %")
plt.ylabel("Salary")
plt.title("Salary vs Bonus %")
plt.legend(title="Gender", labels=["Female", "Male"])
plt.show()
