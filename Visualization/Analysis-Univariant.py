# Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Data
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)

# Univariate Analysis: Distribution of Sepal Length
plt.figure(figsize=(8, 5))
sns.histplot(df['sepal length (cm)'], kde=True)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()
