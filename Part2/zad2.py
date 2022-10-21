import sqlite3
conn = sqlite3.connect('Part2/zad2.db')
cur = conn.cursor()
result = cur.execute("SELECT DISTINCT t2.ID_Ребенка FROM data2 t2 join data1 t1 on t2.ID_Ребенка=t1.ID WHERE t1.Gender='М' and ID_Родителя IN (SELECT t2.ID_Родителя From data2 t2 join data1 t1 on t2.ID_Ребенка=t1.ID Where t1.FIO LIKE 'Седых В.А.')").fetchall()
for i in result:
    for j in i:
        print('Вопрос 1: ID брата Седых В.А. ',j)
result = cur.execute("SELECT count (DISTINCT t2.ID_Ребенка) FROM data2 t2 join data1 t1 on t2.ID_Ребенка=t1.ID WHERE t1.Gender='М' and ID_Родителя IN (SELECT t2.ID_Родителя From data2 t2 join data1 t1 on t2.ID_Ребенка=t1.ID Where t1.FIO LIKE 'Саенко М.А.')").fetchall()
for i in result:
    for j in i:
        print('Вопрос 2: Братьев Саенко М.А. ',j)
result = cur.execute("SELECT DISTINCT t1.FIO from data2 t2 join data1 t1 on t2.ID_Ребенка=t1.ID group by t2.ID_Ребенка Having Count('t2.ID_Ребенка')=1").fetchall()
for i in result:
    for j in i:
        print('Вопрос 3: Ребенок в неполной семье ',j)

