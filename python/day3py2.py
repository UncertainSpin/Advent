import string

inputPath = "../shared/rucksacks.txt"
sack = open(inputPath, 'r')
sack = sack.readlines()

priority = string.ascii_lowercase + string.ascii_uppercase
priority_sum = 0

def match(first, second, third):
    for character in first:
        if character in second and character in third:
            return character

while len(sack):
    first = sack.pop(0)
    second = sack.pop(0)
    third = sack.pop(0)

    found = match(first, second, third)
    priority_sum += (priority.index(found) + 1)

print(priority_sum)