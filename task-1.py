try:
    with open('city.txt', 'r') as text_file:
        lines = text_file.readlines()
        lines.sort()
        cities = []
        populations = []
        answer = []
        question = int(input('Enter the number:\n'))
        for i in range(len(lines)):
            line = lines[i].strip()
            colon = line.index(':')
            city = line[:colon]
            cities.append(city)
            population = line[colon+1:]
            populations.append(population)
        for j in range(len(populations)):
            if int(populations[j])>question:
                answer.append(cities[j])
                answer.append(':')
                answer.append(populations[j])
        
        
except FileNotFoundError:
    print('This file does not exist. Please come back later')
    


with open('filtered_cities.txt', 'w') as text_file:
    for k in range(len(answer)//3):
        print(*answer[3*k:3*(k+1)], sep ='', file = text_file)
       

