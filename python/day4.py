inputPath = "../shared/sections.txt"
sections = open(inputPath, 'r')
sections = sections.readlines()

total_overlap_count = 0
any_overlap_count = 0

for line in sections:
    elf1, elf2 = line.split(",")
    elf1_start, elf1_end = elf1.split("-")
    elf2_start, elf2_end = elf2.split("-")

    elf1_work = []
    elf2_work = []

    elf1_work = [*range(int(elf1_start), int(elf1_end)+1, 1)]
    elf2_work = [*range(int(elf2_start), int(elf2_end)+1, 1)]

    total_overlap = []

    print("Elf 1: " + str(elf1_work))
    print("Elf 2: " + str(elf2_work))


# Originally performed remove within the loop, but it appeared to mess with indices and skip elements
    for n in elf1_work:
        if n in elf2_work:
            # print("total_overlap: " + str(n))
            total_overlap.append(n)
    
    for x in total_overlap:
        elf1_work.remove(x)
        elf2_work.remove(x)

    # print("Pruned Elf 1: " + str(elf1_work))
    # print("Pruned Elf 2: " + str(elf2_work))
    # print("----------")

    if len(elf1_work) == 0:
        # print("Elf 1 is now empty")
        total_overlap_count = total_overlap_count + 1
    elif len(elf2_work) == 0:
        # print("Elf 2 is now empty")
        total_overlap_count = total_overlap_count + 1
 
print(total_overlap_count)