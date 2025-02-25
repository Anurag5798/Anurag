import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/SIC/Desktop/newfold/hackathon/Banglore_traffic_Dataset.csv")
print(list(df.columns))
df["Date"] = pd.to_datetime(df["Date"])

plt.figure(figsize=(12, 6))
grp_speed = df.groupby("Area Name")["Average Speed"].mean().reset_index()
sns.barplot(data=grp_speed, x="Area Name", y="Average Speed")
plt.xticks(rotation=45)
plt.title("Average Speed by Area")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 8))
numeric_cols = df.select_dtypes(include="number")
corr = numeric_cols.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of Numeric Columns")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 8))
incident_area = df.groupby("Area Name")["Incident Reports"].sum()
plt.pie(incident_area, labels=incident_area.index, autopct='%1.1f%%', startangle=90)
plt.title("Incident Reports Distribution by Area")
plt.tight_layout()
plt.show()
