from db_accessor import DBAccess
from amazon_search_api import Amazon
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser(description="DB Update Script")
parser.add_argument("field", type=str, default="thumbnail", help="補完したいレコード")
parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("-y", "--yes", action="store_true")
args = parser.parse_args()


db = DBAccess()
amazon = Amazon()

l = db.null_data(args.field)

if args.verbose:
    for i in l:
        print("[{}]{}".format(i["isbn"], i["title"]))

print("UPDATE DATABASE: {} records".format(len(l)))

if not args.yes:
    choice = input("Please response with \"yes\" [y/N]:")
    if choice.lower() in ["y", "ye", "yes"]:
        pass
    else:
        print("Abort.")
        exit()

for i in tqdm(l):
    json_data = i.copy()
    if "_id" in json_data:
        del json_data["_id"]
    #print("[{}]".format(json_data["isbn"]), end="")
    json_data = amazon.parse(None, i["isbn"], json_data)
    db.update({"isbn": i["isbn"]}, json_data)
    #print("None" if "title" not in json_data else json_data["title"])

print("FINISH")
