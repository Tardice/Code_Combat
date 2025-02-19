# Collect 9 mushrooms.

# This function makes the pet fetch potions for you.
def onSpawn(event):
    while True:
        # Pets can find the nearest item by its type.
        potion = pet.findNearestByType("potion")
        # Make the pet fetch the potion if it exists:
        pet.fetch(potion)

pet.on("spawn", onSpawn)

# Mushrooms are toxic, don't collect them too quickly.
while True:
    someItem = hero.findNearestItem()
    if someItem and hero.health > hero.maxHealth / 3:
        # Collect the someItem:
        hero.moveXY(someItem.pos.x, someItem.pos.y)
        pass
