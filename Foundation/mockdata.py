import json
import random
import numpy as np
import datetime
import os

# Remove existing 'retail_transactions.jsonl' file, if any
# ! rm -f /p/a/t/h retail_transactions.jsonl

# Set the no of transactions
no_of_iteration = 500000

# Open a file in write mode
with open(os.getcwd() + '/data/json/retail_transactions.json', 'w') as f:
  for num in range(no_of_iteration):
    if (random.randint(1, 10000) != 5000):
      # Create a valid transaction
      new_txn = {
        'orderID': num,
        'customerID': random.randint(1, 100000),
        'productID': np.random.randint(10000, size=random.randint(1, 5)).tolist(),
        'paymentMthd': random.choice(['Credit card', 'Debit card', 'Digital wallet', 'Cash on delivery', 'Cryptocurrency']),
        'totalAmt': round(random.random() * 5000, 2),
        'invoiceTime': datetime.datetime.now().isoformat()
      }
    else:
      # Create an invalid transaction
      new_txn = {
        'orderID': "",
        'customerID': "",
        'productID': "",
        'paymentMthd': "",
        'totalAmt': "",
        'invoiceTime': ""
       }
     
# Write the transaciton as a JSON line to the file
f.write(json.dumps(new_txn) + "\n")
