from mysql_session import MySQLSession 

def main():
    accout = {
        "db": "sandbox",
        "host": "127.0.0.1",
        "port": "13306",
        "user": "sandbox",
        "pass": "sandbox"
    }
    with MySQLSession(accout) as session:
        cursor = session.cursor()
        cursor.execute("show tables")
        for row in cursor.fetchall():
            print(row)

        cursor.execute("select 1")
        for row in cursor.fetchall():
            print(row)
 
        cursor.close()
    

if __name__ == '__main__':
    main()
