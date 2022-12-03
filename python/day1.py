inputPath = "../shared/rations.txt"
rations = open(inputPath, 'r')
rations = rations.readlines()

def FindFood(rations):
    numElves = 1
    currentCalories = 0
    caloriesPerElf = 0
    maxCalories = 0

    rankedCalories = []

    for line in rations:
        if line.strip() == "":
            caloriesPerElf = currentCalories
            rankedCalories.append(caloriesPerElf)
            print("Calories for Elf #" + str(numElves) + " : " + str(caloriesPerElf))
            if caloriesPerElf > maxCalories:
                maxCalories = caloriesPerElf
            caloriesPerElf = 0
            currentCalories = 0
            numElves = numElves + 1
        else:
            currentCalories = int(line) + currentCalories

    print("The most calories an elf is carrying: " + str(maxCalories))
    rankedCalories.sort(reverse=True)
    print("Top 3: " + str(rankedCalories[:3]))
    print("Top 3 Total: " + str(rankedCalories[0] + rankedCalories[1] + rankedCalories[2]))

FindFood(rations)