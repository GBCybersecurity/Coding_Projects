from random import randint
weapons = ["Sword", "Shotgun", "Cutlass", "Mace", "Revolver", "Slingshot"]
locations = {"Dragon Crest Mountatin": "Fire", "Fel Bolt Tower": "Lighting", "Murky Swamps": "Slag", "Whispering Woods": "Earth", "Submerged Igloo": "Ice", "Arid Plains": "Wind"}

while True:
    for weapon in weapons:
        print(weapon)
    weapon_choice = str(input("\nChoose a weapon(type weapon name): "))
    weapon_choice = weapon_choice.title()        
    if weapon_choice not in weapons:
        print(f"\nWe don't have {weapon_choice} in our arsenal.")
        continue
    else:
        print(f"\nYou have chosen {weapon_choice}, nice choice!")
    while True:
        for location in locations:
            print(location)
        location_choice = input("\nChoose training location(type location name): ")
        location_choice = location_choice.title()
        if location_choice not in list(locations):
            print(f"\nDon't know where {location_choice} is.")
            continue
        else:
            attribute = locations[location_choice]
            print(f"\nTraining at {location_choice} has imbued your {weapon_choice} with the {attribute} attribute.")
            print(f"\nYou and your {attribute} {weapon_choice} are ready to take on the world!")
            exit()
