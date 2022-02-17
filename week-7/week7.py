from flask import Flask, jsonify, url_for, json, request, render_template, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
# from flask_restful import Resource, Api

app = Flask(
    __name__,
    static_folder = "static", # 靜態檔案的資料夾名稱
    static_url_path = "/" # 靜態檔案對應的網址路徑
    )

app.secret_key="any string but secret" # 設定 session 的密鑰

def db_connection():
    mydb = None
    try:
        mydb = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        database = "website",
        password = "",
        charset = "utf8"
        )
    except mysql.connector.Error as e:
        print(e)
    return mydb

@app.route("/")
def index():
    return render_template("home.html")

@app.route('/api/members', methods=['GET'])
def find_member():
    username = request.args.get('username')
    mydb = db_connection()
    mycursor = mydb.cursor()
    sql = """
        SELECT id, name, username FROM member WHERE username = %s;
    """
    val = (username, )
    mycursor.execute(sql, val)
    num = mycursor.fetchone()
    if num:
        return {'data': {
            'id': num[0],
            'name': num[1],
            'username': num[2]
            }
        }
    else:
        return {'data': None}

# 可以抓到全部的資料

@app.route("/api/members/",methods=["GET"])
def api_member():
    mydb = db_connection()
    mycursor = mydb.cursor()
    sql = """
            SELECT * FROM member;
        """
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    num = mycursor.fetchall()
    return jsonify(num)
    
@app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['name_new']
        username = userDetails['username_new']
        password = userDetails['password_new']
        # hash_pwd = generate_password_hash(password)
        
        sql = """
            SELECT count(username) FROM member WHERE username = %s;
        """
        val = (username, )
        mydb = db_connection()
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        num = tuple(mycursor)[0][0]
        if num:
            result = "帳號已經被註冊"
            return redirect(url_for('error', message=result))
        elif name == '' or username == '' or password == '':
            result = "請輸入姓名、帳號、密碼，謝謝"
            return redirect(url_for('error', message=result))
        else:
            sql = """
            INSERT INTO member(name, username, password) VALUES (%s, %s, %s);
            """
            val = (name, username, password)
            mycursor.execute(sql, val)
            mydb.commit()
            return redirect("/")

@app.route("/signin",methods=["GET","POST"])
def signin():
    if request.method == 'POST':
        username=request.form["username"]
        password=request.form["password"]
        # hash_pwd = generate_password_hash(password)

        sql = """
            SELECT * FROM member WHERE username = %s and password = %s;
        """
        val = (username, password)
        mydb = db_connection()
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        num = mycursor.fetchone()
        if num:
            session["name"] = num[1]
            session["username"] = username
            # session["password"] = password
            return redirect('/member')
        elif (username == '' and password == '') or (username == '' and password != '') or (username != '' and password == ''):
            result = "請輸入帳號、密碼"
            return redirect(url_for('error', message=result))
        else:
            result = "帳號或密碼輸入錯誤"
            return redirect(url_for('error', message=result)) 
     
@app.route("/member")
def member():
    if "username" in session:
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
    session.pop('username', None)
    return redirect('/')

app.run(port=3000, debug=True)
