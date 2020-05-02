import sqlite3
import os.path

#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#db_path = os.path.join(BASE_DIR, "worker2.db")



def workerData():
    con = sqlite3.connect("worker.db")
    cur.execute("CREATE TABLE IF NOT EXISTS worker(id INTEGER PRIMARY KEY, WorID text, Firstname text, Surname text Posada text, Age text, Gender text, Adress text, Mobile text)")
    con.commit()
    con.close()



def WorkerRec(WorID, Firstname, Surname, Posada, Age, Gender, Adress, Mobile):
    con = sqlite3.connect("worker.db")
    cur = con.cursor()
    cur.execute("INSERT INTO worker VALUES (NULL, ?,?,?,?,?,?,?)",(WorID, Firstname, Surname , Posada, Age, Gender, Adress, Mobile))
    con.commit()
    con.close()





def viewData():
    con = sqlite3.connect("worker.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM worker")
    row = cur.fetchall()
    con.close()
    return rows


def deleteRec(id):
    con = sqlite3.connect('worker2.db')
    cur = con.cursor()
    cur.execute("DELETE FROM worker WHERE id=?", (id,))
    con.commit()
    con.close()

    workerData()


def searchData(WorID="", Firstname="", Surname="" , Posada="", Age="", Gender="", Adress="", Mobile=""):
    con = sqlite3.connect("worker.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM worker WHERE WorID=? OR Firstname=? OR Surname=? OR Posada=? OR Age=? OR Gender=? OR Adress=? OR Mobile=?", (WorID, Firstname, Surname, Posada, Age, Gender, Adress, Mobile))
    rows =cur.fetchall()
    con.close()
    return rows


def dataUpdate(id, WorID="", Firstname="", Surname="", Posada="", Age="", Gender="", Adress="", Mobile=""):
    con = sqlite3.connect("worker.db")
    cur = con.cursor()
    cur.execute("UPDATE worker SET WorID=?, Firstname=?, Surname=?, Posada=?,Age=?,Gender=?,Adress=?,Mobile=?, WHERE id=?", (WorID, Firstname, Surname, Posada, Age, Gender, Adress, Mobile, id))

    con.commit()
    con.close()




