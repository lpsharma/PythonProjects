# Step 1: Import Libraries
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest, f_classif

# Step 2: Load Data
# Using the Iris dataset for demonstration
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Step 3: ANOVA Test
# Select the top 2 features based on the ANOVA F-test
anova_selector = SelectKBest(f_classif, k=2)
X_kbest = anova_selector.fit_transform(X, y)

# Display results
print("Original feature names:", X.columns)
print("F-scores for each feature:", anova_selector.scores_)
print("Selected top 2 feature names:", X.columns[anova_selector.get_support(indices=True)])
print("Selected top 2 features shape:", X_kbest.shape)
