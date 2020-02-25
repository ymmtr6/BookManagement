# BookManagement

ISBNをパラメータにセットしたリクエストを登録する機能をつけた簡単なWebサーバ．

iOSアプリを子機として扱えるようにしている．

APIサービスから情報を取得し，mongoDBに保存する．
また，Reactでビューアーを作成．

## TODO

* 編集機能
* ビューアーの機能追加

##　ファイル構造

bookmanagement (React)
 - フロントユーザインターフェースを提供
app.py (Flask)
 - バックエンドAPIを提供
mongoDB
 - DBを担当
