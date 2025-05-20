import requests 

res = requests.post("http://127.0.0.1:8000/items",json = 
{
  "name": "Asif",
  "description": "Hello Asif",
  "price": 2
})


print("Text", res.text)
print("Json", res.json())
print("Status Code", res.status_code)

