with open("./datasets/7. IPRB.txt") as IPRB_input:
    array_of_nums = [int(i) for i in IPRB_input.read().strip().split()]
    total = sum(array_of_nums)
    dominant, heterozygous, recessive = array_of_nums
    print(
        (dominant*(dominant-1) + (2*dominant*heterozygous) + (2*dominant*recessive) + (0.75 * heterozygous * (heterozygous - 1)) + (heterozygous * recessive) ) / (total * (total - 1)) 
    )
