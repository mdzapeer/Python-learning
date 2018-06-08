import sqlite3

def createTable():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insertRow(item,quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

def viewRows():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM STORE")
    rows=cur.fetchall()
    return rows

def deleteRow(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM STORE WHERE item=?",(item,))
    conn.commit()
    conn.close()

def updateRow(item, quantity, price):
        conn=sqlite3.connect("lite.db")
        cur=conn.cursor()
        cur.execute("UPDATE STORE SET quantity=?, price=? WHERE item=?",(quantity, price, item))
        conn.commit()
        conn.close()


createTable()
print("Before: \n")
print(viewRows())
updateRow("MUG",29,3.6)
#insertRow("Wine glass",30,10.5)
print("After: \n")
print(viewRows())
