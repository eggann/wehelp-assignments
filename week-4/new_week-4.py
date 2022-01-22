from flask import Flask, url_for
from flask import request # 載入 Request 物件
from flask import render_template
from flask import session
from flask import redirect

app = Flask(
    __name__,
    static_folder = "static", # 靜態檔案的資料夾名稱
    static_url_path = "/" # 靜態檔案對應的網址路徑
    )

app.secret_key="any string but secret" # 設定 session 的密鑰

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/signin",methods=["GET","POST"])
def signin():
    account=request.form["account"]
    password=request.form["password"]
    
    if account and password == "test":
        session["account"] = account
        return redirect("/member/")
    elif (account == '' and password == '') or (account == '' and password != '') or (account != '' and password == ''):
        result = "請輸入帳號、密碼"
        return redirect(url_for('error', message=result))
    else:
        result = "帳號、或密碼輸入錯誤"
        return redirect(url_for('error', message=result)) 
     
@app.route("/member/")
def member():
    if "account" in session:
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/error")
def error():
    error = request.args.get("message")
    return render_template("error.html", message=error)
    
@app.route("/signout")
def signout():
    session.pop('account', None)
    return redirect('/')

app.run(port=3000)
