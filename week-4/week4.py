from flask import Flask
from flask import request # 載入 Request 物件
from flask import render_template
from flask import session

app = Flask(
    __name__,
    static_folder = "static", # 靜態檔案的資料夾名稱
    static_url_path = "/" # 靜態檔案對應的網址路徑
    )

@app.route("/")
def index():
    return render_template("home.html")

app.run(port=3000)
