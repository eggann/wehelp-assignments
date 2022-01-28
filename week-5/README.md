<h1>要求三：SQL CRUD</h1>

<br/>

<p>使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料</p>

![img](https://raw.githubusercontent.com/eggann/wehelp-assignments/main/week-5/images/1_INSERT_DATA.jpg)

<br/>

<p>使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序</p>

<p style= color: red;>把 LIMIT 那行去除就是直接用 `time` 排序 (由近到遠)</p>

![img](https://raw.githubusercontent.com/eggann/wehelp-assignments/main/week-5/images/2_SORTBY_TIME.jpg)

<br/>

<p>使用 SELECT 指令取得欄位 username 是 test 的會員資料</p>

![img](https://raw.githubusercontent.com/eggann/wehelp-assignments/main/week-5/images/3_USERNAMEISTEST.jpg)

<br/>

<p>使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料</p>

![img](https://raw.githubusercontent.com/eggann/wehelp-assignments/main/week-5/images/4_USERNAMEANDPASSWOEDARETEST.jpg)

<br/>

<p>使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2</p>

![img](https://raw.githubusercontent.com/eggann/wehelp-assignments/main/week-5/images/5_CHANGE_NAME.jpg)

<br/>

<br/>

<h1>要求四：SQL Aggregate Functions</h1>

<br/>

<p>取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )</p>

![img](https://raw.githubusercontent.com/eggann/wehelp-assignments/main/week-5/images/6_COUNT.jpg)

<br/>

<p>取得 member 資料表中，所有會員 follower_count 欄位的總和</p>

![img](https://raw.githubusercontent.com/eggann/wehelp-assignments/main/week-5/images/7_SUM.jpg)

<br/>

<p>取得 member 資料表中，所有會員 follower_count 欄位的平均數</p>

![img](https://raw.githubusercontent.com/eggann/wehelp-assignments/main/week-5/images/8_AVG.jpg)

<br/>

<br/>

<h1>要求五：SQL JOIN (Optional)</h1>

<p>在資料庫中，建立新資料表，取名字為 message。資料表中必須包含以下欄位設定：</p>

![img](https://raw.githubusercontent.com/eggann/wehelp-assignments/main/week-5/images/9_MESSAGE.jpg)

<br/>

<p>使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名</p>

![img](https://raw.githubusercontent.com/eggann/wehelp-assignments/main/week-5/images/10_ALL_MESSAGE.jpg)

<br/>

<p>使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名</p>

![img](https://raw.githubusercontent.com/eggann/wehelp-assignments/main/week-5/images/11_USERNAME_TEST.jpg)

<br/>

<h1>額外補充</h1>

<p>用 mysqldump 匯出 data.sql 步驟</p>

<br/>

<li>找到存放 mysqldump.exe 的路徑</li>
