def climb(n):
    if n < 3:
        return n
    return climb(n - 1) + climb(n - 2)

step = int(input('Введите кол-во ступенек:'))
print(climb(step))