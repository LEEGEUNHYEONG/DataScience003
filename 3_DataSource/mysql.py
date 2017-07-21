#   mysql 접속
#   pip3 install mysqlclient

import MySQLdb

conn = MySQLdb.connect(
    user='',
    passwd='',
    host='',
    db=''
)

#   커서 추출
cur = conn.cursor()

#   테이블 생성
cur.execute('DROP table if exists items')
cur.execute('''
    CREATE TABLE items (
      item_id INTEGER PRIMARY KEY AUTO_INCREMENT,
      name TEXT,
      price INTEGER
    )
''')

#   데이터 추가하기
data = [('Banana', 300),('Mango', 640),('Kiwi', 280)]

for i in data :
    cur.execute("INSERT INTO innodb.items(name, price) VALUES (%s, %s)", i)

#   데이터 추출
cur.execute("SELECT * FROM innodb.items")
for row in cur.fetchall() :
    print(row)

conn.autocommit(on=True)
