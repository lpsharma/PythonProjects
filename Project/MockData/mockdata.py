import json
import random
import numpy as np
import datetime

no_of_iteration = 10000  # Example value, replace with the desired number of iterations

file_name = './data/json/retail_transactions.jsonl'

with open(file_name, 'w') as f:
    for num in range(10000,99999,+200):
        new_txn = {
            'orderID': num,
            'customerID': random.randint(1000, 1999),
            'productID': np.random.randint(20, size=random.randint(1, 5)).tolist(),
            'paymentMthd': random.choice(['Credit card', 'Debit card', 'Digital wallet', 'Cash on delivery', 'Cryptocurrency']),
            'totalAmt': round(random.random() * 5000, 2),
            'invoiceTime': datetime.datetime.now().isoformat()
        }
        f.write(json.dumps(new_txn) + "\n")

with open(file_name) as f:
    for line in f:
      txn = json.loads(line)
      print(txn)
      