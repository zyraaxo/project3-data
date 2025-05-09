import pandas
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import Image, display
file_name = "train_csv"

df = pd.read_csv(file_name)

print(df.head())
print(df.info())\


#This is to check for missing data

missing_values = df.isnull().sum()
print("\nMissing Values per Column: \n ")
print(missing_values)

# EDA for missing data in a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Data Heatmap")
plt.show()
