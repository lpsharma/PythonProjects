import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

file_path = os.getcwd() + '/LogisticRegression/bank.csv'

data = pd.read_csv(file_path,header=0)

pd.crosstab(data.education, data.y).plot(kind='area')
plt.show()