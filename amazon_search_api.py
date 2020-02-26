import requests
from bs4 import BeautifulSoup


class Amazon(object):

    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0"}

    def update(self, json_data, key, value):
        if key not in json_data:
            json_data[key] = value

    def parse(self, api_data: dict, isbn: str, json_data={}) -> dict:
        soup = self.call(isbn)
        if soup is None:
            return json_data

        a = soup.find(id="productTitle")
        if a is not None:
            self.update(json_data, "title", a.string)

        a = soup.find(id="img-canvas")
        if a is not None:
            try:
                images = a.img["data-a-dynamic-image"]
                thumb = list(json.loads(images).keys())[-1]
                self.update(json_data, "thumbnail", thumb)
            except:
                import traceback
                traceback.print_exc()

        # 余裕があれば後々複数人対応を行う
        a = soup.find(class_="contributorNameID")
        if a is not None:
            self.update(json_data, "authors", [a.string])

        # publisher, publishedDate
        detail = soup.find(id="detail_bullets_id")
        if detail is not None:
            for li in detail.find_all("li"):
                if li.text.startswith("出版社:"):
                    self.update(json_data, "publisher",
                                li.text.replace("出版社: ", "").strip())
                elif li.text.startswith(" 発売日："):
                    self.update(json_data, "publishedDate",
                                li.text.replace(" 発売日：", "").strip())

        detail = soup.find(id="productDescription")
        try:
            description = detail.find("p").text
            self.update(json_data, "description", description)
        except:
            pass

        return json_data

    def call(self, isbn13: str):
        asin = self.transrate10(isbn13)
        res = requests.get(
            "https://amazon.jp/dp/{}".format(asin), headers=self.headers)
        if res.status_code != 200:
            return None
        return BeautifulSoup(res.text, "html.parser")

    def transrate10(self, isbn13: str):
        isbn10 = isbn13[3:12]
        check_digit = 0

        for i in range(len(isbn10)):
            check_digit += int(isbn10[i]) * (10 - i)
        check_digit = 11 - (check_digit % 11)

        if check_digit == 10:
            check_digit = "X"
        elif check_digit == 11:
            check_digit = "0"
        else:
            check_digit = str(check_digit)
        return isbn10 + check_digit


if __name__ == "__main__":
    obj = Amazon()
    j = obj.parse(None, "9784295004806")
    print(j)
