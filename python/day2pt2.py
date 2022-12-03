# Score sums:
#   shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
#   outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won

# A for Rock, B for Paper, and C for Scissors (Opponent)
# X for Rock, Y for Paper, and Z for Scissors (Self)

# A Y  -  2 (from paper) + 6 (win)
# B X  -  1 (from rock) + 0 (win)
# C Z  -  3 (from scissors) + 3 (tie)

# Mapping Choice
# 1 - Rock
# 2 - Paper
# 3 - Scissors

# Mapping Wins
# C X
# A Y
# B Z

# Mapping Losses
# B X
# C Y
# A Z

# Mapping Tie
# A X
# B Y
# C Z

# Part 2
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.

inputPath = "../shared/strategy.txt"
guide = open(inputPath, 'r')
guide = guide.readlines()

choice = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

win = 6
tie = 3
loss = 0


def Simulate(guide):
    total = 0
    for line in guide:
        total += Shoot(line)
    return total

def Shoot(line):
    battle = line.split()
    op = battle[0]
    me = battle[1]
    roundScore = VictoryScore(me, op)
    print("Round Score: " + str(roundScore))
    return roundScore

def SelfScore(me):
    return choice[me]

def VictoryScore(me, op):
    match me:
        # Need to lose
        case "X":
            match op:
                case "A":
                    return loss + SelfScore("Z")
                case "B":
                    return loss + SelfScore("X")
                case "C":
                    return loss + SelfScore("Y")
        # Need to tie
        case "Y":
            match op:
                case "A":
                    return tie + SelfScore("X")
                case "B":
                    return tie + SelfScore("Y")
                case "C":
                    return tie + SelfScore("Z")
        # Need to win
        case "Z":
            match op:
                case "A":
                    return win + SelfScore("Y")
                case "B":
                    return win + SelfScore("Z")
                case "C":
                    return win + SelfScore("X")


print("Total Score: " + str(Simulate(guide)))