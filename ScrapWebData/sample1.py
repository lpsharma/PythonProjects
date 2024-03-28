import requests
r = requests.get('http://www.google.com')

print ("\n")
print("request status: " + str(r.status_code))
# print(r.url)
# print(r.headers)
print(r.json)


