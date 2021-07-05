def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory.keys():
            inventory[item] += 1
        inventory.setdefault(item, 1)
    return inventory

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += inventory[k]
    print("Total number of items: " + str(item_total))
    
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)