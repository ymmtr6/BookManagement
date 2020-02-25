import json
import requests
import datetime

from google_api_parser import GoogleAPI
from openbd_parser import OpenBD
from amazon_search_api import Amazon


class BookSearchAPI(object):
    """
    BookSearch API
    """

    def __init__(self):
        """

        """
        self.google_books_url = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
        self.openbd_url = "https://api.openbd.jp/v1/get?isbn="

    def get_json(self, isbn: str, method="amazon", json_data={}) -> dict:
        """

        """
        if method == "google":
            print("[Google]", end="")
            json_api_data = self.__call_api(
                url=self.google_books_url, isbn=isbn)
            json_data = GoogleAPI().parse(json_api_data, isbn, json_data)
            print(json_data)
        elif method == "openbd":
            print("[OpenBD]", end="")
            json_api_data = self.__call_api(url=self.openbd_url, isbn=isbn)
            json_data = OpenBD().parse(json_api_data, isbn, json_data)
            print(json_data)
        elif method == "amazon":
            print("[Amazon]", end="")
            json_data = Amazon().parse(None, isbn, json_data)
            print(json_data)
        else:  # All
            print("[All]", end="")
            json_api_data = self.__call_api(
                url=self.google_books_url, isbn=isbn)
            json_data = GoogleAPI().parse(json_api_data, isbn, json_data)
            json_dpi_data = self.__call_api(url=self.openbd_url, isbn=isbn)
            json_data = OpenBD().parse(json_api_data, isbn, json_data)
            json_data = Amazon().parse(None, isbn, json_data)
            print(json_data)

        json_data["isbn"] = isbn
        json_data["registered"] = self.get_datetime()

        return json_data

    def __call_api(self, url: str, isbn: str) -> dict:
        """
        Call Google Books API
        """
        response = requests.get(url + isbn)
        if response.status_code != 200:
            return None
        try:
            d = json.loads(response.text)
        except:
            d = None
        return d

    def get_datetime(self) -> str:
        """

        """
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d")


if __name__ == "__main__":
    api = BookSearchAPI()
    #data = api.get_json("9784295004806")
    #data = api.get_json("9784121006240")
    # print(data)
    data = api.transrate10("9784295004806")
    print(data)
