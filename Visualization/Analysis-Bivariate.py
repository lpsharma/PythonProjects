# Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Data
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)

# Bivariate Analysis: Relationship between Sepal Length and Sepal Width
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['sepal length (cm)'], y=df['sepal width (cm)'])
plt.title('Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.show()

