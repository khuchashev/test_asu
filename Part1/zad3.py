import random
items = list(range(20))
tup=0
for i in items:
    items[i]=random.randint(-15,14)
m=max(items)
for i in items:
    if (i+m)<0:
        tup=tup+1
print('Массив ',items,', Максимальный элемент ',m, ', количество элементов ',tup)  
