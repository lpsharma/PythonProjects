# Step 1: Import Libraries
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler

# Step 2: Load Data
# Using the Iris dataset for demonstration
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Apply Lasso Regression
# Initialize the Lasso model with a regularization parameter (alpha)
lasso = Lasso(alpha=0.1)

# Fit the Lasso model
lasso.fit(X_scaled, y)

# Get the coefficients of the features
coefficients = pd.Series(lasso.coef_, index=X.columns)

# Select features with non-zero coefficients
selected_features = coefficients[coefficients != 0].index.tolist()

# Display results
print("Original feature names:", X.columns.tolist())
print("Lasso coefficients:", coefficients)
print("Selected features:", selected_features)



"""

Explanation:
Import Libraries:

    pandas for data manipulation.
    load_iris to load the sample dataset.
    Lasso for Lasso regression.
    StandardScaler to standardize the data.

Load Data:

    Load the Iris dataset and create X (features) and y (target variable).

Standardize Data:

    Standardize the data using StandardScaler. Lasso regression is sensitive to the scale of the input data, so standardization is important.

Apply Lasso Regression:

    Initialize the Lasso model with a chosen regularization parameter (alpha). The value of alpha controls the strength of the regularization; higher values lead to more coefficients being shrunk to zero.
    Fit the Lasso model to the standardized data.
    Extract the coefficients of the features from the fitted model.
    Select features that have non-zero coefficients.
Output:
    This code will output:
    Original feature names.
    Lasso coefficients for each feature.
    Names of the selected features (those with non-zero coefficients).

"""