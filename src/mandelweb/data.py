import MySQLdb

def getConnection():
    db = MySQLdb.connect(host='localhost', user='dulcis', passwd='mandelkaka', db='dulcis')
    return db

def getAlmonds(start, end):
    db = getConnection()
    cursor = db.cursor()

    cursor.callproc('getSet', (start.real, start.imag, end.real, end.imag))
    db.close()

def insertAlmonds(almonds):
    db = getConnection()
    cursor = db.cursor()
    print almonds
#    cursor.executemany("""INSERT INTO almonds(re, im, iterations, resultRe, resultIm, outside)
#    VALUES({0:s}, {1:s}, {2:s}, {3:s}, {4:s}, {5:s})
#     ON DUPLICATE KEY UPDATE iterations = {2:s}, resultRe = {3:s}, resultIm = {4:s}, outside = {5:s};""", almonds)
    cursor.executemany("""INSERT INTO almonds(re, im, iterations, resultRe, resultIm, outside)
    VALUES(%s, %s, %s, %s, %s);""", almonds)
    db.close()
    