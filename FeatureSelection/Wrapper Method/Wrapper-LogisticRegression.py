# Step 1: Import Libraries
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE

# Step 2: Load Data
# Using the Iris dataset for demonstration
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Step 3: Apply RFE
# Initialize the model
model = LogisticRegression(max_iter=200)

# Initialize RFE with the model and number of features to select (e.g., 2)
rfe = RFE(estimator=model, n_features_to_select=2)

# Fit RFE
fit = rfe.fit(X, y)

# Display results
print("Original feature names:", X.columns.tolist())
print("Selected feature ranking:", fit.ranking_)
print("Selected top features:", X.columns[fit.support_].tolist())
print("Selected top features shape:", X.loc[:, fit.support_].shape)
