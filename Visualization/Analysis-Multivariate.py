# Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Data
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)

# Add the target variable to the DataFrame
df['species'] = pd.Categorical.from_codes(data.target, data.target_names)

# Multivariate Analysis: Pairplot of All Features Colored by Species
sns.pairplot(df, hue='species', markers=["o", "s", "D"])
plt.suptitle('Pairplot of Iris Features', y=1.02)
plt.show()