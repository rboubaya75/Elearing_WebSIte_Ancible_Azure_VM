import psycopg2
import logging

host="localhost"
dbname="postgres"
user="postgres"
password="123"
sslmode = "require"


logging.basicConfig(filename='logging.log', level=logging.INFO,
                    format='%(asctime)s: %(name)s :%(levelname)s:%(message)s')

logging.info('This is an info:')
logging.error('This is an error:')


# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()


def create_table():
    logging.info("Creating Table: start")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Course (id serial NOT NULL, CATEGORY VARCHAR(255), TITLE VARCHAR(255), LINK VARCHAR(255));")
    logging.info("Creating Table: end")
    print("table created")
    conn.commit()

create_table()

cursor.close()
conn.close()
