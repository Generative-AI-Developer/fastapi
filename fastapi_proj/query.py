import requests 

res = requests.get("http://127.0.0.1:8000/items/?q=12&skip=20")


print("Text", res.text)
print("Json", res.json())
print("Status Code", res.status_code)

