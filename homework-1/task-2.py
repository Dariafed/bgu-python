while True:
    number = input("Please enter a number between 1 to 999: ")
    if number.isdigit() and int(number) <= 999 and int(number) >= 1:
        number = int(number)
        break
    else:
        print("You made a mistake. Please enter a valid number.")


units = {
    1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
    6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять',
    11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать',
    15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать',
    19: 'девятнадцать'
}
tens = {
    20: 'двадцать', 30: 'тридцать', 40: 'сорок', 50: 'пятьдесят',
    60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто'
}
hundreds = {
    100: 'сто', 200: 'двести', 300: 'триста', 400: 'четыреста',
    500: 'пятьсот', 600: 'шестьсот', 700: 'семьсот', 800: 'восемьсот', 900: 'девятьсот'
}

if number < 20:
    print(units[number])
elif number < 100:
    if number % 10 == 0:
        print(tens[number])
    else:
        print(tens[number // 10 * 10] + " " + units[number % 10])
elif number < 1000:
    if number % 100 == 0:
        print(hundreds[number])
    else:
        print(hundreds[number // 100 * 100] + " " + tens[(number%100) // 10 * 10] + " " + units[(number % 100)%10])