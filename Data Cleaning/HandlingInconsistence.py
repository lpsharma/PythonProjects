import pandas as pd
from sklearn.impute import KNNImputer
import os

# Load data
df = pd.read_csv(os.getcwd() + '/data/csv/bank.csv')

# Handling Missing Values
# Mean Imputation
df['day_of_week'].fillna(df['day_of_week'].mean(), inplace=False)

# Final cleaned data
df.to_csv(os.getcwd() + '/data/csv/cleaned_data.csv', index=False)


# KNN Imputation
#imputer = KNNImputer(n_neighbors=5)
#df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

# Handling Inconsistent Data
# Standardization
# df['date_column'] = pd.to_datetime(df['date_column'], errors='coerce')

# Validation Rule Example
#df['age'] = df['age'].apply(lambda x: x if x > 0 else None)

# Regular Expressions Example
#df['phone_number'] = df['phone_number'].str.replace(r'\D', '')

