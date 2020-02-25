from db_accessor import DBAccess
from amazon_search_api import Amazon

db = DBAccess()
amazon = Amazon()

l = db.null_data()

print("UPDATE DATABASE")

for i in l:
    json_data = {
        "isbn": i["isbn"],
        "registered": i["registered"]
    }
    print(json_data["isbn"], end="")
    json_data = amazon.parse(None, i["isbn"], json_data)
    db.update({"isbn": i["isbn"]}, json_data)
    print("None" if "title" not in json_data else i["title"])

print("END")
