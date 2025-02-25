import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv('wine.csv')
print(df.head())
print(df.describe())
print(df.info())

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()

sns.countplot(x="quality", data=df, palette="viridis")
plt.title("Distribution of Wine Quality")
plt.xlabel("Quality Rating")
plt.ylabel("Count")
plt.show()

sns.boxplot(x="quality", y="fixed acidity", data=df, palette="coolwarm")
plt.title("Fixed Acidity vs. Wine Quality")
plt.show()

df["quality_label"] = df["quality"].apply(lambda x: 1 if x >= 7 else 0)
scaler = StandardScaler()
features = df.drop(["quality", "quality_label"], axis=1)
df_scaled = pd.DataFrame(scaler.fit_transform(features), columns=features.columns)
df_scaled["quality_label"] = df["quality_label"]

X = df_scaled.drop("quality_label", axis=1)
y = df_scaled["quality_label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

importances = model.feature_importances_
feature_names = X.columns
plt.figure(figsize=(10, 5))
sns.barplot(x=importances, y=feature_names, palette="magma")
plt.title("Feature Importance in Wine Quality Prediction")
plt.xlabel("Importance Score")
plt.show()
