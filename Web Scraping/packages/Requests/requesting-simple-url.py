import requests

r = requests.get(
    "https://docs.pola.rs/user-guide/getting-started/#with_columns")

print(r)  # <Response [200]>
print(r.status_code)  # 200

print(r.content)  # Print the content of the request
