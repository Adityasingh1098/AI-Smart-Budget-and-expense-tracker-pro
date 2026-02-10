import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def verify_email(emailid):

    con = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT"))
    )

    cur = con.cursor()

    sql = "SELECT emailid FROM userrecord WHERE emailid = %s"
    cur.execute(sql, (emailid,))

    result = cur.fetchone()

    cur.close()
    con.close()

    return result is not None
