inputPath = "../shared/sections.txt"
sections = open(inputPath, 'r')
sections = sections.readlines()

any_overlap_count = 0

def check_dupes(elf1, elf2):
    for n in elf1:
        if n in elf2:
            print("Found Overlap: " + str(n))
            return True
    return False

for line in sections:
    elf1, elf2 = line.split(",")
    elf1_start, elf1_end = elf1.split("-")
    elf2_start, elf2_end = elf2.split("-")

    elf1_work = []
    elf2_work = []

    elf1_work = [*range(int(elf1_start), int(elf1_end)+1, 1)]
    elf2_work = [*range(int(elf2_start), int(elf2_end)+1, 1)]

    # print("Elf 1: " + str(elf1_work))
    # print("Elf 2: " + str(elf2_work))
    # print("Duplicates: " + str(check_dupes(elf1_work, elf2_work)))
    if check_dupes(elf1_work, elf2_work):
        any_overlap_count = any_overlap_count + 1

 
print(any_overlap_count)