import requests

params = {"q": "test query"}

item_data = {
    "name": "New Phone",
    "price": 599.99,
    "quantity": 10
}
response = requests.post(f"http://127.0.0.1:8000/items/", json=item_data)
print("POST /items/ response:", response.json())

response = requests.get("http://127.0.0.1:8000/items/")
print("GET /items/ response:", response.json())

update_item_data = {
    "name": "New Phone",
    "price": "649.00",
    "quantity": 5
}

response = requests.put("http://127.0.0.1:8000/items/New Phone", json=update_item_data)
print("PUT /items/{item_name}/ response:", response.json())

response = requests.delete("http://127.0.0.1:8000/items/New Phone")
print("DELETE /items/{item_name}/ response:", response.json())
