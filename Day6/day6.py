def part1():
    with open('input.txt') as f:
        line = f.readline()

    pointer = 0
    queue = []
    while pointer < len(line):
        if len(queue) < 4:
            queue.append(line[pointer])
        
        if len(queue) == 4:
            check_set = set(queue)
            if len(check_set) == 4:
                print(pointer + 1)
                break
            else:
                queue.pop(0)

        pointer += 1

def part2():
    with open('input.txt') as f:
        line = f.readline()

    pointer = 0
    queue = []
    while pointer < len(line):
        if len(queue) < 14:
            queue.append(line[pointer])
        
        if len(queue) == 14:
            check_set = set(queue)
            if len(check_set) == 14:
                print(pointer + 1)
                break
            else:
                queue.pop(0)

        pointer += 1


if __name__ == "__main__":
    #part1()
    part2()