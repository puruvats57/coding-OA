import math

def egg_drop_2_eggs_100_floors():
    # Step 1: Find the minimum number of drops in worst case
    drops = math.ceil((-1 + math.sqrt(1 + 8 * 100)) / 2)

    print(f"Minimum drops needed in worst case: {drops}")

    # Step 2: Simulate the floors from which to drop
    floors = []
    current_floor = 0
    step = drops

    while current_floor < 100 and step > 0:
        current_floor += step
        if current_floor > 100:
            current_floor = 100
        floors.append(current_floor)
        step -= 1

    print("Drop first egg at floors:", floors)
    return drops

egg_drop_2_eggs_100_floors()
