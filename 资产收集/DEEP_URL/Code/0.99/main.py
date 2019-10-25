# coding:utf-8
import sqlite3

coon = sqlite3.connect('urls.db')
cur = coon.cursor()


fet = cur.execute('select url from urls LIMIT 0,1').fetchone()
cur.close()
coon.commit()
coon.close()
aaa = str(fet).replace("(u'","").replace("',)",'')
print type(aaa)