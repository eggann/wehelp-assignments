from flask import Flask, url_for
from flask import request # 載入 Request 物件
from flask import render_template
from flask import session
from flask import redirect
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

mydb = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        database = "flaskapp",
        password = "",
        charset = "utf8"
        )

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
        # hash_pwd = generate_password_hash(password)
        
        sql = """
            SELECT count(account) FROM users WHERE account = %s;
        """
        val = (account, )
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        num = tuple(mycursor)[0][0]
        if num:
            result = "帳號已經被註冊"
            return redirect(url_for('error', message=result))
        elif name == '' or account == '' or password == '':
            result = "請輸入姓名、帳號、密碼，謝謝"
            return redirect(url_for('error', message=result))
        else:
            sql = """
            INSERT INTO users(name, account, password) VALUES (%s, %s, %s);
            """
            val = (name, account, password)
            mycursor.execute(sql, val)
            mydb.commit()
            return redirect("/")

@app.route("/signin",methods=["GET","POST"])
def signin():
    if request.method == 'POST':
        account=request.form["account"]
        password=request.form["password"]
        # hash_pwd = generate_password_hash(password)

        sql = """
            SELECT * FROM users WHERE account = %s and password = %s;
        """
        val = (account, password)
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        num = mycursor.fetchone()
        if num:
            session["name"] = num[0]
            session["account"] = account
            session["password"] = password
            return redirect('/member/')
        elif (account == '' and password == '') or (account == '' and password != '') or (account != '' and password == ''):
            result = "請輸入帳號、密碼"
            return redirect(url_for('error', message=result))
        else:
            result = "帳號或密碼輸入錯誤"
            return redirect(url_for('error', message=result)) 
     
@app.route("/member/")
def member():
    if "account" in session:
        name = session['name']
        return render_template("member.html", name=name)
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