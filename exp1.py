import csv
import cx_Oracle

def import_data(file):
    with open(file, 'rb') as csvfile:
        datareader = csv.reader(csvfile, delimiter = ',', quotechar='"')
        for row in datareader:
            yield row

def write_to_db_arr(gen_source):
    arSource = []
    for elm in gen_source:
        arSource.append(elm)
    db = cx_Oracle.connect('user/password@127.0.0.1/orcl')
    cursor = db.cursor()
    cursor.prepare("INSERT INTO MyDemo (x, y) VALUES (:1, :2)")
    cursor.executemany(None, arSource)

def write_to_db_ser(gen_source):
    db = cx_Oracle.connect('user/password@127.0.0.1/orcl')
    cursor = db.cursor()
    cursor.prepare("INSERT INTO MyDemo (x, y) VALUES (:1, :2)")
    for elm in gen_source:
        cursor.execute(None, elm)