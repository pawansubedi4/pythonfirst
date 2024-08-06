import requests
url ="https://jsonplaceholder.typicode.com/users"
data = requests.get(url)
data = data.json()

for i in data:
    print(i["name"])
for j in data:
    print(i["address"]["zipcode"])