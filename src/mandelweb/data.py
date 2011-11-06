import MySQLdb

def getConnection():
    db = MySQLdb.connect(host='localhost', user='dulcis', passwd='mandelkaka')
    return db

def getAlmonds(start, end):
    db = getConnection()
    cursor = db.getCursor()
    cursor.callproc('getSet', (start.real, start.imag, end.real, end.imag))
    db.close()

def insertAlmonds(almonds):
    db = getConnection()
    cursor = db.getCursor()
    cursor.executeMany("""INSERT INTO almonds(re, im, iterations, resultRe, resultIm, outside)
    VALUES({0}, {1}, {2}, {3}, {4}, {5})
     ON DUPLICATE KEY UPDATE iterations = {2}, resultRe = {3}, resultIm = {4}, outside = {5};""", almonds)
    db.close()
    