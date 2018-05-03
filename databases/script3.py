import psycopg2

def createTable():
    conn=psycopg2.connect("dbname='db_1' user='postgres' password='123456' host='192.168.3.2' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insertRow(item,quantity,price):
    conn=psycopg2.connect("dbname='db_1' user='postgres' password='123456' host='192.168.3.2' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,quantity,price))
    conn.commit()
    conn.close()

def viewRows():
    conn=psycopg2.connect("dbname='db_1' user='postgres' password='123456' host='192.168.3.2' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM STORE")
    rows=cur.fetchall()
    return rows

def deleteRow(item):
    conn=psycopg2.connect("dbname='db_1' user='postgres' password='123456' host='192.168.3.2' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM STORE WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def updateRow(item, quantity, price):
        conn=psycopg2.connect("dbname='db_1' user='postgres' password='123456' host='192.168.3.2' port='5432'")
        cur=conn.cursor()
        cur.execute("UPDATE STORE SET quantity=%s, price=%s WHERE item=%s",(quantity, price, item))
        conn.commit()
        conn.close()


createTable()
print("Before: \n")
print(viewRows())
#updateRow("MUG",29,3.6)
insertRow("Wine glass",30,10.5)
print("After: \n")
print(viewRows())
