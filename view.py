from flask import Flask, render_template
import pymysql


con = pymysql.connect(host='localhost',
                      user='root',
                      password='',
                      db='dbmember',
                      charset='utf8')
app = Flask(__name__)


@app.route("/")
def Showdatamember():
    with con:
        cur = con.cursor()
        cur.execute("")
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
