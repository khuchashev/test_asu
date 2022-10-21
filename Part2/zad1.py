import sqlite3
conn = sqlite3.connect('Part2/zad1.db')
cur = conn.cursor()
result = cur.execute("SELECT * FROM data Where Категория='скорый' or Вокзал='Павелецкий';").fetchall()
print('Вопрос 1: Количество записей ',len(result))
result = cur.execute("SELECT * FROM data Where Категория='скорый' and Время='40:00';").fetchall()
print('Вопрос 2: Количество записей ',len(result))
result = cur.execute("SELECT * FROM data Where Время='35:00' or Вокзал='Павелецкий';").fetchall()
print('Вопрос 3: Количество записей ',len(result))
