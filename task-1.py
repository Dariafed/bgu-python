try:
    with open('input.txt', 'r') as text_file:
        lines = text_file.readlines()
except FileNotFoundError:
    print('This file does not exist. Please come back later')

#with open('input.txt', 'r') as text_file:
#    lines = text_file.readlines()

grades = []
names = []
for line in lines:
    line= line.strip()
    coma = line.index(',')
    line = line[coma+1::].strip()
    grades.append(int(line))
for line in lines:
    line= line.strip()
    coma = line.index(',')
    line = line[:coma].strip()
    names.append(line)

average = sum(grades)/len(grades)

with open('output.txt', 'w') as text_file:
    for i in range(len(grades)):
        if grades[i] > average:
            print(names[i], file = text_file)
        
