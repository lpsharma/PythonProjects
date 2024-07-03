import json

def read_json_file(file_name):
  # Read the JSONL file
  print(file_name)
  with open(file_name) as f:
    for line in f:
      txn = json.loads(line)
      print(txn)
      # Yield valid transactions only
      if (txn['orderID'] != ""):
        yield(txn)

txn_generator = read_json_file('./data/json/retail_transactions.jsonl')
print(txn_generator)

