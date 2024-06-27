try:
    with open('input.txt', 'r') as text_file:
        lines = text_file.readlines()
except FileNotFoundError:
    print('This file does not exist. Please come back later')

symbols = input('Enter the symbols to delete:')
print(repr(symbols))

    
with open('output.txt', 'w') as text_file:
    for line in lines:
        line = line.rstrip()
        line = line.rstrip(str(symbols))
        line += ';'
        line = line[::-1]
        print(line, file = text_file)