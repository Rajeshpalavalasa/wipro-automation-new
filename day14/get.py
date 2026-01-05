import requests
import json

#uri - uniform identified identifier
#url - uniform resource location

url="https://jsonplaceholder.typicode.com/users"

#making the GEt request (Fetch the data)
response=requests.get(url)
if response.status_code == 200:
    data = response.json()   # Convert JSON to Python object
    
    print("Fetched Data:")
    for user in data:
        print(user["name"])
else:
    print("Request failed with status code:", response.status_code)

