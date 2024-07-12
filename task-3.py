try:
    with open('input.txt', 'r') as text_file:
        lines = text_file.readlines()
        word = input('Write course what you need:\n')
        line = []
        answer=[]
        for i in range(len(lines)):
            line = lines[i]
            line = line.replace(':', ',')
            line = line.split(',')
            for j in range(len(line)):
                x = line[j].strip()    
                if x== word:
                    answer.append(line[0])
    print(*answer, sep ='\n')
        
except FileNotFoundError:
    print('This file does not exist. Please come back later')
    
    
    
    
