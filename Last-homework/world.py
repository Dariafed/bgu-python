from random import randint

def rand_mas(x):
    size = [0]*10
    fullnes_for_all1 = [0]*10
    number1 = []
    if x == 1:
        for i in range(10):
            size[i] = randint(0, 14)
            fullnes_for_all1[i] = randint(35, 100)
            number1.append(i)
    elif x == 2:
        for i in range(10):
            size[i] = randint(0, 29)
            fullnes_for_all1[i] = randint(35, 100)
            number1.append(i)
    elif x == 3:
        for i in range(10):
            size[i] = randint(0, 44)
            fullnes_for_all1[i] = randint(35, 100)
            number1.append(i)
    return number1, size, fullnes_for_all1
    
class Animal:
    def __init__(self, name, number, type_food, sex, age, max_age, habitat, size, fullnes):
        self.name = name
        self.number = number
        self.type_food = type_food
        self.sex = sex
        self.age = age
        self.max_age = max_age
        self.habitat = habitat
        self.size = size
        self.fullnes = fullnes
    
    def die(self, grass_food):
        for i in range(len(self.age)):
            self.age[i] += 1
        for i in range(len(self.age)-1, -1, -1):
            if self.age[i] >= self.max_age:
                if self.size == 'small':
                    grass_food += 2
                if self.size == 'medium':
                    grass_food += 5
                if self.size == 'big':
                    grass_food += 9
                self.number.pop(i)
                self.age.pop(i)
                self.sex.pop(i)
                self.fullnes.pop(i)
        return grass_food
    
    def anotherOne(self):
        self.number.append(len(number))
        self.age.append(randint(0, 10))
        x = randint(0,1)
        if x == 0:
            self.sex.append('male')
        else:
            self.sex.append('female')
        self.fullnes.append(randint(35, 100))
        print('\nNew animal has been added!\n')
        return None
    
    def writeChar(self, name):
        for i in range(len(self.number)):
            print(f'Age of {i + 1} {name} - {self.age[i]}')
            print(f'Fullnes of {i + 1} {name} - {self.fullnes[i]}')
            print(f'Sex of {i + 1} {name} - {self.sex[i]}')
            print('------------')
        return None
    
    def fuck(self, first, second):
        if first < len(self.fullnes) and second < len(self.fullnes):
            if self.sex[first] == self.sex[second]:
                print("They have same gender, they can't have children")
                return 1
            if self.habitat == 'farm':
                if self.fullnes[first] >= 20 and self.fullnes[second] >= 20 and self.age[first] >= 5 and self.age[second] >= 5:
                    for i in range(2):
                        self.number.append(len(self.number))
                        self.age.append(0)
                        x = randint(0,1)
                        if x == 0:
                            self.sex.append('male')
                        else:
                            self.sex.append('female')
                        self.fullnes.append(73)
                    print("Congratulations! They have children!")
                else:
                    print('The fullnes or age are not enough!')
            elif self.habitat == 'water':
                if self.fullnes[first] >= 50 and self.fullnes[second] >= 50:
                    for i in range(10):
                        self.number.append(len(self.number))
                        self.age.append(0)
                        x = randint(0,1)
                        if x == 0:
                            self.sex.append('male')
                        else:
                            self.sex.append('female')
                        self.fullnes.append(23)
                    print("Congratulations! They have children!")
                else:
                    print('The fullnes or age are not enough!')
            elif self.habitat == 'air':
                if self.fullnes[first] >= 42 and self.fullnes[second] >= 42 and self.age[first] >= 3 and self.age[second] >= 3:
                    for i in range(4):
                        self.number.append(len(self.number))
                        self.age.append(0)
                        x = randint(0,1)
                        if x == 0:
                            self.sex.append('male')
                        else:
                            self.sex.append('female')
                        self.fullnes.append(64)
                    print("Congratulations! They have children!")
                else:
                    print('The fullnes or age are not enough!')           
            return None
        else:
            print("Don't exist animal with this index!")
    def dieForMeat(self):
        if len(self.number) != 0:
            animalDie = randint(0, len(self.number) - 1)
            self.number.pop(animalDie)
            self.age.pop(animalDie)
            self.sex.pop(animalDie)
            self.fullnes.pop(animalDie)
            food = 1
        else:
            food = 0
        return food
    
    def Eating(self, grass_food):
        if self.type_food == "grass":
            for i in range(len(self.fullnes)):
                if grass_food > 0:
                    if self.fullnes[i] > 74:
                        self.fullnes[i] = 100
                        grass_food -= 1
                    else:
                        self.fullnes[i] += 26
                        grass_food -= 1
                else:
                    self.fullnes -= 9
        if self.type_food == "meat":
            for i in range(len(self.fullnes)):
                chance = randint(0,1)
                if chance == 1:
                    animal_die = randint(1, 8)
                    YoN = 0
                    trys = 1
                    while YoN == 0 and trys != 9:
                        if animal_die == 1:
                            YoN = cats.dieForMeat()
                            if YoN == 0:
                                trys += 1
                                animal_die = 2
                        elif animal_die == 2:
                            YoN = cow.dieForMeat()
                            if YoN == 0:
                                trys += 1
                                animal_die = 3
                        elif animal_die == 3:
                            YoN = pig.dieForMeat()
                            if YoN == 0:
                                trys += 1
                                animal_die = 4
                        elif animal_die == 4:
                            YoN = horse.dieForMeat()
                            if YoN == 0:
                                trys += 1
                                animal_die = 5
                        elif animal_die == 5:
                            YoN = whale.dieForMeat()
                            if YoN == 0:
                                trys += 1
                                animal_die = 6
                        elif animal_die == 6:
                            YoN = goldfish.dieForMeat()
                            if YoN == 0:
                                trys += 1
                                animal_die = 7
                        elif animal_die == 7:
                            YoN = pigeon.dieForMeat()
                            if YoN == 0:
                                trys += 1
                                animal_die = 8
                        elif animal_die == 8:
                            YoN = sparrow.dieForMeat()
                            if YoN == 0:
                                trys += 1
                                animal_die = 1
                    if YoN == 1:
                        if self.fullnes[i] > 47:
                            self.fullnes[i] = 100
                        else:
                            self.fullnes[i] += 53
                elif chance == 0 or YoN == 0:
                    self.fullnes[i] -= 16 
        for i in range(len(self.fullnes)-1, -1, -1):
            if self.fullnes[i] < 10:
                if self.size == 'small':
                    grass_food += 2
                if self.size == 'medium':
                    grass_food += 5
                if self.size == 'big':
                    grass_food += 9
                self.number.pop(i)
                self.age.pop(i)
                self.sex.pop(i)
                self.fullnes.pop(i)
        print("Somebody died, somebody was eaten, somebody still alive. That's life...")
        return grass_food
                             
grass_food = 100
number = []
size1 = []
fullnes_for_all = []

sex = ['male', 'female', 'male', 'female', 'female', 'male', 'female', 'male', 'female', 'female']
'''ANIMALS FARM'''
number, size1, fullnes_for_all = rand_mas(1)
cats = Animal('cat', number, 'grass', sex, size1, 15, 'farm', 'small', fullnes_for_all)

number, size1, fullnes_for_all = rand_mas(2)
sex = ['male', 'female', 'male', 'female', 'female', 'male', 'female', 'male', 'female', 'female']
cow = Animal('cow', number, 'grass', sex, size1, 30, 'farm', 'medium', fullnes_for_all)

number, size1, fullnes_for_all = rand_mas(2)
sex = ['male', 'female', 'male', 'female', 'female', 'male', 'female', 'male', 'female', 'female']
pig = Animal('pig', number, 'grass', sex, size1, 30, 'farm', 'medium', fullnes_for_all)

number, size1, fullnes_for_all = rand_mas(2)
sex = ['male', 'female', 'male', 'female', 'female', 'male', 'female', 'male', 'female', 'female']
horse = Animal('horse', number, 'grass', sex, size1, 30, 'farm', 'medium', fullnes_for_all)

number, size1, fullnes_for_all = rand_mas(2)
sex = ['male', 'female', 'male', 'female', 'female', 'male', 'female', 'male', 'female', 'female']
wolf = Animal('wolf', number, 'meat', sex, size1, 30, 'farm', 'medium', fullnes_for_all)

number, size1, fullnes_for_all = rand_mas(3)
sex = ['male', 'female', 'male', 'female', 'female', 'male', 'female', 'male', 'female', 'female']
lion = Animal('lion', number, 'meat', sex, size1, 45, 'farm', 'big', fullnes_for_all)
'''ANIMALS WATER'''
number, size1, fullnes_for_all = rand_mas(3)
sex = ['male', 'female', 'male', 'female', 'female', 'male', 'female', 'male', 'female', 'female']
whale = Animal('whale', number, 'grass', sex, size1, 45, 'water', 'big', fullnes_for_all)

number, size1, fullnes_for_all = rand_mas(2)
sex = ['male', 'female', 'male', 'female', 'female', 'male', 'female', 'male', 'female', 'female']
shark = Animal('shark', number, 'meat', sex, size1, 30, 'water', 'medium', fullnes_for_all)

number, size1, fullnes_for_all = rand_mas(1)
sex = ['male', 'female', 'male', 'female', 'female', 'male', 'female', 'male', 'female', 'female']
goldfish = Animal('golgfish', number, 'grass', sex, size1, 15, 'water', 'small', fullnes_for_all)
'''ANIMALS AIR'''
number, size1, fullnes_for_all = rand_mas(2)
sex = ['male', 'female', 'male', 'female', 'female', 'male', 'female', 'male', 'female', 'female']
eagle = Animal('eagle', number, 'meat', sex, size1, 30, 'air', 'medium', fullnes_for_all)

number, size1, fullnes_for_all = rand_mas(1)
sex = ['male', 'female', 'male', 'female', 'female', 'male', 'female', 'male', 'female', 'female']
pigeon = Animal('pigeon', number, 'grass', sex, size1, 15, 'air', 'small', fullnes_for_all)

number, size1, fullnes_for_all = rand_mas(1)
sex = ['male', 'female', 'male', 'female', 'female', 'male', 'female', 'male', 'female', 'female']
sparrow = Animal('sparrow', number, 'grass', sex, size1, 15, 'air', 'small', fullnes_for_all)

#grass_food = cats.die(grass_food)
#x = int(input("What to do?"))
print("\nHi! It's a game 'Planet ecosystem simulator'")
flag = True
while flag == True:
    x = int(input("\nWhat do you want to do?\n\nPick 1 to add new animal\nPick 2 to increase the supply of plant food on the planet\nPick 3 to view the current characteristics of each individual\nPick 4 to reproduce individuals of 1 species\nPick 5 to simulate movement for 1 unit of time\nPick 6 to finish the game\n"))
    if x == 1:
        y = int(input('Which animal do you want to add?\n To add the cat - 1\n To add the whale - 2\n To add the eagle - 3\n To add the cow - 4\n To add the pig - 5\n To add the horse - 6\n To add the wolf - 7\n To add the lion - 8\n To add the shark - 9\n To add the pigeon - 10\n To add the sparrow - 11\n To add the goldfish - 12\n'))
        if y == 1:
            cats.anotherOne()
        if y == 2: 
            whale.anotherOne()
        if y == 3:
            eagle.anotherOne()
        if y == 4:
            cow.anotherOne()
        if y == 5: 
            pig.anotherOne()
        if y == 6:
            horse.anotherOne()
        if y == 7:
            wolf.anotherOne()
        if y == 8: 
            lion.anotherOne()
        if y == 9:
            shark.anotherOne()
        if y == 10:
            pigeon.anotherOne()
        if y == 11: 
            sparrow.anotherOne()
        if y == 12:
            goldfish.anotherOne()
    elif x == 2:
        y = randint(7, 23)
        grass_food += y
        print(grass_food)
        print('The supply of plant food on the planet has been increased!\n')
    elif x == 3:
        y = int(input('To see the current characteristics of each individual!\n To see the cat - 1\n To see the whale - 2\n To see the eagle - 3\n To see the cow - 4\n To see the pig - 5\n To see the horse - 6\n To see the wolf - 7\n To see the lion - 8\n To see the shark - 9\n To see the pigeon - 10\n To see the sparrow - 11\n To see the goldfish - 12\n'))
        if y == 1:
            cats.writeChar("cat")
        if y == 2: 
            whale.writeChar('whale')
        if y == 3:
            eagle.writeChar("eagle")
        if y == 4:
            cow.writeChar("cow")
        if y == 5: 
            pig.writeChar('pig')
        if y == 6:
            horse.writeChar("horse")
        if y == 7:
            wolf.writeChar("wolf")
        if y == 8: 
            lion.writeChar('lion')
        if y == 9:
            shark.writeChar("shark")
        if y == 10:
            pigeon.writeChar("pigeon")
        if y == 11: 
            sparrow.writeChar('sparrow')
        if y == 12:
            goldfish.writeChar("goldfish")
    elif x == 4:
        y = int(input('For which animal do you want to simulate reproducing? \n For the cat - 1\n For the whale - 2\n For the eagle - 3\n For the cow - 4\n For the pig - 5\n For the horse - 6\n For the wolf - 7\n For the lion - 8\n For the shark - 9\n For the pigeon - 10\n For the sparrow - 11\n For the goldfish - 12\n'))
        print("you need to index two individuals")
        first = int(input()) - 1
        second = int(input()) - 1
        if y == 1:
            cats.fuck(first, second)
        if y == 2: 
            whale.fuck(first, second)
        if y == 3:
            eagle.fuck(first, second)
        if y == 4:
            cow.fuck(first, second)
        if y == 5: 
            pig.fuck(first, second)
        if y == 6:
            horse.fuck(first, second)
        if y == 7:
            wolf.fuck(first, second)
        if y == 8: 
            lion.fuck(first, second)
        if y == 9:
            shark.fuck(first, second)
        if y == 10:
            pigeon.fuck(first, second)
        if y == 11: 
            sparrow.fuck(first, second)
        if y == 12:
            goldfish.fuck(first, second)
    elif x == 5:        
        grass_food = cats.die(grass_food)
        grass_food = cats.Eating(grass_food)
        
        grass_food = cow.die(grass_food)
        grass_food = cow.Eating(grass_food)
        
        grass_food = pig.die(grass_food)
        grass_food = pig.Eating(grass_food)
        
        grass_food = horse.die(grass_food)
        grass_food = horse.Eating(grass_food)
        
        grass_food = wolf.die(grass_food)
        grass_food = wolf.Eating(grass_food)
        
        grass_food = lion.die(grass_food)
        grass_food = lion.Eating(grass_food)
        
        grass_food = whale.die(grass_food)
        grass_food = whale.Eating(grass_food)
        
        grass_food = shark.die(grass_food)
        grass_food = shark.Eating(grass_food)
        
        grass_food = goldfish.die(grass_food)
        grass_food = goldfish.Eating(grass_food)
        
        grass_food = eagle.die(grass_food)
        grass_food = eagle.Eating(grass_food)
        
        grass_food = pigeon.die(grass_food)
        grass_food = pigeon.Eating(grass_food)
        
        grass_food = sparrow.die(grass_food)
        grass_food = sparrow.Eating(grass_food)
    elif x == 6:
        flag = False