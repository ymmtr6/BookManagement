from book_search_api import BookSearchAPI
from db_accessor import DBAccess
from flask import Flask, render_template, request, jsonify, make_response, send_from_directory, send_file
import json
from flask_cors import CORS

static_folder = "bookmanagement/build/static"
build_folder = "bookmanagement/build"

app = Flask(__name__, static_folder=static_folder)
# CORS対策
CORS(app)
# 日本語文字化け対応
app.config["JSON_AS_ASCII"] = False

book_search_api = BookSearchAPI()
database = DBAccess()


@app.route("/get")
def get():
    """
    ISBNからJSONを返す
    """
    isbn = request.args.get("isbn", default=None)
    json_data = {}
    json_data = book_search_api.get_json(
        isbn, json_data=json_data) if isbn else {}
    res = jsonify(json_data)
    return res


@app.route("/register")
def regist():
    """
    ISBNを利用してDBに登録する
    未実装なので，「204 No Content」を返す
    """
    isbn = request.args.get("isbn", default=None)
    json_data = {}
    json_data = book_search_api.get_json(
        isbn, json_data=json_data) if isbn else None
    if json_data is not None:
        database.insert(json_data)

    try:
        res = jsonify(json_data)
    except:
        res = "{}"
    return res


@app.route("/list")
def _list():
    """
    DBから書籍リストを返す．
    json.dumpsに自作handlerを利用しているため，苦肉の策で
    list->json->dict->jsonと変換を噛ます
    本来はページングするべきか．
    """
    return jsonify(json.loads(database.show_all()))


@app.route("/status")
def status():
    """
    生存確認用
    """
    return make_response("OK", 200)


@app.route("/norep")
def no_reply():
    """
    未実装は「204 No Content」を返す
    """
    response = make_response("", 204)
    response.mimetype = app.config["JSONIFY_MIMETYPE"]
    return response


@app.route("/")
def root():
    """
    プロジェクトROOTのindex.htmlを返す
    """
    return send_from_directory(build_folder, "index.html")


@app.route("/<path:path>")
def index(path):
    """
    static rootを返す
    """
    return send_from_directory(build_folder, path)


if __name__ == "__main__":
    # print(app.url_map)
    app.run(host="0.0.0.0", port=80)
