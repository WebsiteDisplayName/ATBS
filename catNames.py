

catNames = []

while True:
    print("Enter cat name " + str(len(catNames) + 1) + " (or just <Enter> to break)")
    name = input() 
    if name == '':
        break
    catNames += [name]

print("The list of cat names are:")
for name in catNames:
    print(name)