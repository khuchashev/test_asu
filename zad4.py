def abc(n):
    i = 0
    while n > 0:
        n = n//10
        i += 1
    return i
while True:
    num = input('Введите число: ')
    try:
        num = int(num)
        break;
    except ValueError:
        pass
print('Количество разрядов:', abc(num))