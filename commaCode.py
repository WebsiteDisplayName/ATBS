def listToString(list):
    listString = '' 
    for idx in range(len(list) - 1):
        listString += list[idx] + ', '
        if idx == len(list) - 2:
            listString += 'and ' + list[-1]
    return listString


spam = ['apples','bananas','tofu','cats']
print(listToString(spam))