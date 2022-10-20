while True:
        a = input("Введите натуральное число ")
        try:
            a = int(a)
            break;
        except ValueError:
            pass
print('Максимальный символ ', max(str(a)))
