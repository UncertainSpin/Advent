import string

inputPath = "../shared/rucksacks.txt"
sack = open(inputPath, 'r')
sack = sack.readlines()

sackLeft = ""
sackRight = ""

priority = string.ascii_lowercase + string.ascii_uppercase
priority_sum = 0

for line in sack:
    sackLeft, sackRight = line[:len(line)//2].split(), line[len(line)//2:].split()
    print(sackLeft[0] + " | " + sackRight[0])

    for item in sackLeft[0]:
        if item in sackRight[0]:
            match_prio = (priority.index(item) + 1)
            print("Match: " + item + " with prio: " + str(match_prio))
            priority_sum += match_prio
            break

print(priority_sum)
