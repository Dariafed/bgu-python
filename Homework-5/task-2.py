def alg_ev(a, b):
    if a == 0 or b == 0:
       return max(a, b)
    else:
        if a > b:
            return alg_ev(a%b, b)
        else:
            return alg_ev(a, b%a)
    
x = int(input('Введите первое число'))
y = int(input('Введите второе число'))

print('Самый большой общий делитель:', alg_ev(x, y))