import tables



def createAlmondTable():
    almondTable = {
        're': tables.FloatCol(pos=1),
        'im': tables.FloatCol(pos=2),
        'iterations': tables.IntCol(pos=3),
        'outside': tables.BoolCol(pos=4),
        'result': tables.ComplexCol(itemsize=16, pos=5)
    }
    db = tables.openFile('almonds.h5', 'w')
    tbl = db.createTable(db.root, 'almonds', almondTable)
    #tbl.cols.re.createIndex()
    #tbl.cols.im.createIndex()
    tbl.row['re'] = 90
    tbl.row['im'] = 90
    tbl.row.append()
    tbl.flush()
    db.flush()
    print tbl
    db.close()

def getAlmonds(start, end):
    db = tables.openFile('almonds.h5', 'r')
    tbl = db.root.almonds
    query = "(re >= %f) & (re <= %f) & (im >= %f) & (im <= %f)" % (start.real, end.real, start.imag, end.imag)
    rows = tbl.readWhere(query)
    db.close()
    return rows
    #cursor.callproc('getSet', (start.real, start.imag, end.real, end.imag))
    #db.close()

def insertAlmonds(almonds):
    db = tables.openFile('almonds.h5', 'a')
    tbl = db.root.almonds
    tbl.append(almonds)
    tbl.flush()
    db.close()
#    cursor.executemany("""INSERT INTO almonds(re, im, iterations, resultRe, resultIm, outside)
#    VALUES({0:s}, {1:s}, {2:s}, {3:s}, {4:s}, {5:s})
#     ON DUPLICATE KEY UPDATE iterations = {2:s}, resultRe = {3:s}, resultIm = {4:s}, outside = {5:s};""", almonds)
#    sql = ''
#    i = 0
#    print "Inserting into DB..."
#    db = getConnection()
#    cursor = db.cursor()
##    for almond in almonds:
#        i += 1
#        sql += """insert into almonds(re, im, iterations, resultRe, resultIm, outside)
#            values(%(re)f, %(im)f, %(iterations)d, %(resultRe)f, %(resultIm)f, %(outside)d) 
##            ON DUPLICATE KEY UPDATE iterations = %(iterations)d, resultRe = %(resultIm)f, resultIm = %(resultRe)f, outside = %(outside)d; """ % almond
#       if i % 100 == 0:
#            print "executing!"
#            cursor.execute(sql)
#            cursor.fetchall()
#            sql = ''
#    cursor._query(sql)
#    cursor.close()
#    db.close()
#    print "Finished inserting!"
    