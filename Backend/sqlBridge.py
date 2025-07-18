import mysql.connector

def conn():
    database = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="mydompet"
    )
    return database

def sub(Pemasukan, Pengeluaran, Keterangan):
    db = conn()
    cur = db.cursor()  # Tidak pakai dictionary=True untuk INSERT

    query = """INSERT INTO tunai (Pemasukan, Pengeluaran, Keterangan) VALUES (%s, %s, %s)"""
    values = (Pemasukan, Pengeluaran, Keterangan)

    try:
        cur.execute(query, values)
        db.commit()
    except Exception as e:
        print("Error saat INSERT:", e)
    finally:
        cur.close()
        db.close()

def debitUpdate(UdateDebite):
    db = conn()
    cur = db.cursor()

    query = """UPDATE debit SET UdateDebite = %s WHERE debindex = 1"""
    Value = (UdateDebite,)

    try:
        cur.execute(query, Value)
        db.commit()
    except Exception as e:
        print("debitUpdate on Troble", e)
    finally:
        cur.close()
        db.close()

def showDataTunai():
    db = conn()
    cur = db.cursor()

    query = """SELECT Pemasukan, Pengeluaran, Keterangan FROM tunai"""

    try:
        cur.execute(query)
        fecting = cur.fetchall()

        return fecting
    except Exception as e:
        print("Failed", e)
    finally:
        cur.close()
        db.close()

def infoUang():
    db = conn()
    cur = db.cursor()
    
    query = """SELECT SUM(Pemasukan) as TotalMasuk, SUM(Pengeluaran) as TotalKeluar FROM tunai"""

    try:
        cur.execute(query)
        fecthing = cur.fetchall()
        
        return fecthing
    except:
        cur.close()
        db.close()

def infoDebit():
    db = conn()
    cur = db.cursor()

    querry = """SELECT UdateDebite FROM debit WHERE debindex = 1"""

    try:
        cur.execute(querry)
        fecthing = cur.fetchall()

        return fecthing
    except:
        return "error"
    finally:
        cur.close()
        db.close()