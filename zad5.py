sum=0
while True:
    a = input("Введите число ")
    if a=='':
            print(sum)
            break;
    try:
        a = float(a)
        sum += a  
    except ValueError:
        pass