# Step 1: Import Libraries
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest, chi2

# Step 2: Load Data
# Using the Iris dataset for demonstration
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Step 3: Chi-square Test
# Select the top 2 features based on the chi-square test
chi2_selector = SelectKBest(chi2, k=1)
X_kbest = chi2_selector.fit_transform(X, y)

# Display results
print("Original feature names:", X.columns)
print("Scores for each feature:", chi2_selector.scores_)
print("Selected top 2 feature names:", X.columns[chi2_selector.get_support(indices=True)])
print("Selected top 2 features shape:", X_kbest.shape)
