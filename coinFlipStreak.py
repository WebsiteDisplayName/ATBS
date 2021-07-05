import random
numberOfStreaks = 0

for experiment in range(10_000):
    flipList = []
    for i in range(100):
        flipList.append(random.randint(0,1))
    
    counter = 0
    key = flipList[0]
    for i in range(100):
        if key == flipList[i]:
            counter += 1
            if counter == 6:
                numberOfStreaks += 1
                break
        else:
            counter = 1
            key = flipList[i]

print(f'Chance of streak: {numberOfStreaks / 100}%')