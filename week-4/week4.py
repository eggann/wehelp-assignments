from email import message
from unittest import result
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

app.secret_key="ant string but secret" # 設定 session 的密鑰

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/signin",methods=["POST"])
def signin():
    account=request.form["account"]
    account=str(account)
    session["account"]=account
    
    password=request.form["password"]
    password=str(password)
    session["password"]=password
    
    if session["account"]=="" or session["password"]=="":
        result = "要填滿它哦"
        return redirect(url_for('error', message=result))
    elif session["account"] == session["password"] == "test":
        return redirect("/member/")
    else:
        result = "填錯了哦"
        return redirect(url_for('error', message=result))      
     
@app.route("/member/")
def member():
    return render_template("member.html")

@app.route("/error/")
def error():
    if session["account"]=="" or session["password"]=="":
        result = "請輸入帳號、密碼"
        return render_template("error.html", data=result)
    else:
        result = "帳號、或密碼輸入錯誤"
        return render_template("error.html", data=result)
    
@app.route("/signout")
def signout():
    session.pop('account', None)
    return redirect('/')

app.run(port=3000)
