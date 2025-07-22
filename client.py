import requests

# params = {"q": "test query"}
#
# item_data = {
#     "name": "New Phone",
#     "price": 599.99,
#     "quantity": 10
# }
# response = requests.post(f"http://127.0.0.1:8000/items/", json=item_data)
# print("POST /items/ response:", response.json())
#
# response = requests.get("http://127.0.0.1:8000/items/")
# print("GET /items/ response:", response.json())
#
# update_item_data = {
#     "name": "New Phone",
#     "price": "649.00",
#     "quantity": 5
# }
#
# response = requests.put("http://127.0.0.1:8000/items/New Phone", json=update_item_data)
# print("PUT /items/{item_name}/ response:", response.json())
#
# response = requests.delete("http://127.0.0.1:8000/items/New Phone")
# print("DELETE /items/{item_name}/ response:", response.json())


books_data = [
    {
        "title": "Thinking Java",
        "author": "Bruce Eckel",
        "pages": 600
    },
    {
        "title": "Clean Code",
        "author": "Robert Martin",
        "pages": 464
    },
    {
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "pages": 560
    }
]

updated_book = {
    "title": "SQL Quick start guide",
    "author": "Shields",
    "pages": 223
}

for book in books_data:
    response = requests.post("http://127.0.0.1:8000/books", json=book)
    print("POST /books/ response:", response.json())

print()

response = requests.get("http://127.0.0.1:8000/books/")
for book in response.json()["books"]:
    print(f"GET /books/ response: {book['title']} by {book['author']}")

print()

response = requests.get("http://127.0.0.1:8000/books/2")
print("GET /books/book_id response:", response.json())

print()

response = requests.put("http://127.0.0.1:8000/books/1", json=updated_book)
print("PUT /books/book_id response:", response.json())

print()

response = requests.get("http://127.0.0.1:8000/books/")
for book in response.json()["books"]:
    print(f"GET /books/ response: {book['title']} by {book['author']}")

print()

response = requests.delete("http://127.0.0.1:8000/books/2")
print("DELETE /books/book_id response:", response.json())

print()

response = requests.get("http://127.0.0.1:8000/books/")
for book in response.json()["books"]:
    print(f"GET /books/ response: {book['title']} by {book['author']}")
