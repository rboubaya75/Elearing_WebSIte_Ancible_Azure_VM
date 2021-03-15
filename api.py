import psycopg2
import logging
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

"""
host = "rachid.postgres.database.azure.com"
dbname = "postgres"
user = "rachid@rachid"
password = "Leouf2017."
sslmode = "require"
"""
host = "localhost"
user = "postgres"
dbname = "postgres"
password = "123"
sslmode = "require"


# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(
    host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()

cursor.execute("ROLLBACK")
conn.commit()


@app.route('/')
def welcome():
    return redirect(url_for('home'))


@app.route('/home', methods=["GET", "POST"])
def home():
    logging.info("Launching homepage: start")

    if request.method == "POST":
        my_title = request.form.get("title")
        my_link = request.form.get("video_link")
        my_category = request.form.get("category")
        print("MES DATAS", my_link, my_title, my_category)
        cursor.execute("INSERT INTO Course (CATEGORY, TITLE, LINK) VALUES (%s,%s,%s) ",
                       (my_category, my_title, my_link))
        conn.commit()

    logging.info("Launching homepage: end")

    return render_template("index.html")


@app.route('/python', methods=["GET"])
def python():
    logging.info("Launching javascript page: start")

    cursor.execute("SELECT * FROM Course WHERE CATEGORY LIKE 'Python';")
    result = cursor.fetchall()
    logging.info("Launching Python page: end")

    return render_template("python.html", len=len(result), results=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
