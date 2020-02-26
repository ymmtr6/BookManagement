
class OpenBD(object):

    def __init__(self):
        pass

    def update(self, json_data, key, value):
        if key not in json_data:
            json_data[key] = value

    def parse(self, api_data: dict, isbn: str, json_data={}) -> dict:

        if api_data == None or len(api_data) == 1:
            return json_data

        try:
            self.update(json_data, "title", api_data["summary"]["title"])
        except:
            pass

        try:
            self.update(json_data, "authors", api_data["summary"]["author"])
        except:
            pass

        try:
            self.update(json_data, "publisher",
                        api_data["summary"]["publisher"])
        except:
            pass

        try:
            self.update(json_data, "publishedDate",
                        api_data["summary"]["pubdate"])
        except:
            pass

        try:
            self.update(json_data, "description",
                        api_data["onix"]["ColateralDetail"]["TextContent"][0]["Text"].strip())
        except:
            pass

        try:
            self.update(json_data, "thumbnail", api_data["summary"]["cover"])
        except:
            pass

        return json_data
