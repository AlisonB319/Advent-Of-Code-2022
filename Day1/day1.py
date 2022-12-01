
def part1():
    with open('input.txt') as f:
        lines = f.readlines()
    

    maxx = 0
    curr = 0
    for calorie in lines:
        if calorie == "\n":
            if curr > maxx:
                maxx = curr
            curr = 0
        else:
            curr += int(calorie)

    print(maxx)



def part2():
    with open('input.txt') as f:
        lines = f.readlines()

    maxes = [0,0,0]
    curr = 0
    for calorie in lines:
        if calorie == "\n":
            for index, num in reversed(list(enumerate(maxes))):
                # import pdb; pdb.set_trace()
                if curr > num:
                    maxes[index] = curr
                    break
            curr = 0
        else:
            curr += int(calorie)
    print(sum(maxes))


if __name__ == "__main__":
    # part1()
    part2()
