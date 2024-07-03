# Step 1: Import Libraries
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from mlxtend.feature_selection import SequentialFeatureSelector as SFS

# Step 2: Load Data
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Step 3: Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 4: Forward Selection
# Initialize the model
model = LogisticRegression(max_iter=200)

# Initialize Sequential Feature Selector
sfs = SFS(model, 
          k_features=2, 
          forward=True, 
          floating=False, 
          scoring='accuracy',
          cv=5)

# Fit SFS
sfs = sfs.fit(X_train, y_train)

# Selected features
selected_features = list(sfs.k_feature_names_)

# Train model with selected features
model.fit(X_train[selected_features], y_train)
y_pred = model.predict(X_test[selected_features])

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)

# Display results
print("Selected features (Forward Selection):", selected_features)
print("Model accuracy with selected features:", accuracy)
