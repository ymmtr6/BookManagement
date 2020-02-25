
class GoogleAPI(object):
    """
    Google API Paser
    """

    def __init__(self):
        pass

    def update(self, json_data, key, value):
        if key not in json_data:
            json_data[key] = value

    def parse(self, api_data: dict, isbn: str, json_data={}) -> dict:

        if api_data == None or api_data["totalItems"] == 0:
            return json_data

        try:
            self.update(json_data, "title",
                        api_data["items"][0]["volumeInfo"]["title"])
        except:
            pass

        try:
            self.update(json_data, "authors",
                        api_data["items"][0]["volumeInfo"]["authors"])
        except:
            pass

        try:
            self.update(json_data, "publisher",
                        api_data["items"][0]["volumeInfo"]["publisher"])
        except:
            pass

        try:
            self.update(json_data, "publishedDate",
                        api_data["items"][0]["volumeInfo"]["publishedDate"])
        except:
            pass

        try:
            self.update(json_data, "description",
                        api_data["items"][0]["volumeInfo"]["description"])
        except:
            pass

        try:
            self.update(json_data, "thumbnail",
                        api_data["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"])
        except:
            pass

        return json_data
