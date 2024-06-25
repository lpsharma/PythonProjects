# Step 1: Import Libraries
import pandas as pd
from sklearn.datasets import load_iris

# Step 2: Load Data
# Using the Iris dataset for demonstration
data = load_iris()

X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name='target')

# Combine features and target into a single DataFrame for correlation computation
data_combined = pd.concat([X, y], axis=1)

# Step 3: Calculate Correlation
# Compute correlation matrix
correlation_matrix = data_combined.corr()

# Extract correlation of each feature with the target variable
correlation_with_target = correlation_matrix['target'].drop('target')

# Step 4: Select Features
# Select features with the highest absolute correlation
# For example, selecting top 2 features
top_features = correlation_with_target.abs().sort_values(ascending=False).head(1).index

# Subset the original feature set to include only the selected top features
X_selected = X[top_features]

# Display results
print("Original feature names:", X.columns.tolist())
print("Correlation with target:", correlation_with_target)
print("Selected top 2 feature names:", top_features.tolist())
print("Selected top 2 features shape:", X_selected.shape)

