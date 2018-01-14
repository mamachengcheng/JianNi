# JianNi
# -*- coding: UTF-8 -*-
import MySQLdb
import sys
import socket

reload(sys)
sys.setdefaultencoding('utf-8')

db = MySQLdb.Connection("120.77.38.20", "root", "Mcc616254086", "SM", use_unicode=True, charset="utf8")
cursor = db.cursor()
sql = "SELECT * FROM SM.order WHERE id = 1"
try:
    cursor.execute(sql)
    items = cursor.fetchall()
    info = []
    for item in items:
        order_id = item[1]                           # order_id
        order_date = str(item[2])                         # order_date
        customer_name = item[3]                      # customer_name
        content = '1' + item[5] + 'DIY手机壳 1个'    # content
        info.append(customer_name)
        info.append('15623637978')
        info.append(content)
        info.append(order_date)
        info.append(order_id)
        msg = ','.join(info)
        s = socket.socket()
        host = socket.gethostname()
        port = 5050

        s.connect((host, port))
        print(msg)
        s.sendall(msg)
        s.close()


except db.DatabaseError:
    db.rollback()
