while True:
        a = input("Введите код ASCII ")
        try:
            a = int(a)
            break;
        except ValueError:
            pass
if (a>=65) and (a<=90):
    print('Прописная английская буква ',chr(a))
else:
    if (a>=97) and (a<=122):
        print('Строчная английская буква ',chr(a))
    else:
        print('Иной символ ',chr(a))

