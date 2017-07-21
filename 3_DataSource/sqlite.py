import sqlite3

#   sqlite connect
dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)

#   create table, input data
cur = conn.cursor()
cur.executescript("""
/*  items 테이블 존재시 삭제*/
DROP table if exists items;

/*  테이블 생성  */
create table items(
  item_id integer PRIMARY KEY ,
  name text UNIQUE ,
  price INTEGER 
);

/*  데이터 입력  */
/*
INSERT INTO items(name, price) VALUES ('Apple', 800);
insert into items(name, price) VALUES ('Orange', 780);
insert into items(name, price) VALUES ('Banana', 430);
*/
""")

#   디비에 적용
conn.commit()

"""
#   sqlite 1
#   데이터 추출
cur = conn.cursor()
cur.execute("SELECT * FROM items")
item_list = cur.fetchall()

#   출력
for it in item_list:
    print(it)
"""

#   sqlite 2
#   데이터 추가
cur = conn.cursor()
cur.execute(
    "INSERT INTO items (name,price) VALUES (?,?)",
    ("Orange", 5200))
conn.commit()

#   여러 데이터 추가
cur = conn.cursor()
data = [ ("Mango", 7700), ("Kiwi", 4000), ("Grape", 8000),
         ("Peach", 9400), ("Persimmon", 7000), ("Banana", 4000)]
cur.executemany(
    "INSERT INTO items(name, price) values(?,?)", data
)
conn.commit()

#   출력
cur = conn.cursor()
price_range = (4000, 7000)
cur.execute(
    "SELECT * FROM items WHERE price >= ? AND price <= ?", price_range)

fr_list = cur.fetchall()
for fr in fr_list :
    print(fr)