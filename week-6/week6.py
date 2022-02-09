from flask import Flask, url_for
from flask import request # 載入 Request 物件
from flask import render_template
from flask import session
from flask import redirect
from werkzeug.security import generate_password_hash
import mysql.connector
        
# mydb = mysql.connector.connect(
# host = "localhost",
# port = 3306,
# user = "root",
# database = "flaskapp",
# password = "jiggjo9182"
# )
    
# mycursor = mydb.cursor()
# sql = "INSERT INTO users (name, account, password) VALUES (%s, %s, %s)"
# val = ("Ben", "Benyeh", "benyeh123")
# mycursor.execute(sql)
# mydb.commit()
# mydb.close()

app = Flask(
    __name__,
    static_folder = "static", # 靜態檔案的資料夾名稱
    static_url_path = "/" # 靜態檔案對應的網址路徑
    )

app.secret_key="any string but secret" # 設定 session 的密鑰

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['name_new']
        account = userDetails['account_new']
        password = userDetails['password_new']
        hash_pwd = generate_password_hash(password)
        
        mydb = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        database = "flaskapp",
        password = "jiggjo9182",
        charset = "utf8"
        )
        
        mycursor = mydb.cursor()
        sql = """INSERT INTO users(name, account, password) VALUES (%s, %s, %s) """
        val = (name, account, hash_pwd)
        mycursor.execute(sql, val)
        mydb.commit()
        return 'success'
        # cur = """SELECT * FROM `users` WHERE `account` = %s"""
        # mycursor.execute(cur, (account, ))
        # result = int(mycursor.fetchall())
        # if (len(result) == 0):
        #     return False
        # else:
        #     return True
        # num = cur.fetchall()
        # num = int(num[0][0])
        # if num >= 1:
        #     result = "帳號已經被註冊"
        #     return redirect(url_for('error', message=result))
        # else:
        #     return redirect("/")
        # return 'success'
    # return render_template('home.html')

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