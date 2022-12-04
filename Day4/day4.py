
def part1():
    with open('input.txt') as f:
        lines = f.readlines()
    
    counter = 0
    for line in lines:
        split_on_comma = line.split(",")
        zone_1 = split_on_comma[0]
        zone_2 = split_on_comma[1]

        z1 = zone_1.split("-")
        z2 = zone_2.split("-")

        nums_zone1 = set()
        nums_zone2 = set()
        for i in range(int(z1[0]), int(z1[1])+1):
            nums_zone1.add(i)
        
        for i in range(int(z2[0]), int(z2[1])+1):
            nums_zone2.add(i)

        if nums_zone1.issubset(nums_zone2) or nums_zone2.issubset(nums_zone1):
            counter += 1

    print(counter)

def part2():
    with open('input.txt') as f:
        lines = f.readlines()
    
    counter = 0
    for line in lines:
        split_on_comma = line.split(",")
        zone_1 = split_on_comma[0]
        zone_2 = split_on_comma[1]

        z1 = zone_1.split("-")
        z2 = zone_2.split("-")

        nums_zone1 = set()
        nums_zone2 = set()
        for i in range(int(z1[0]), int(z1[1])+1):
            nums_zone1.add(i)
        
        for i in range(int(z2[0]), int(z2[1])+1):
            nums_zone2.add(i)

        if len(nums_zone1) >= len(nums_zone2):
            for num in nums_zone1:
                if num in nums_zone2:
                    counter += 1
                    break
        else:
            for num in nums_zone2:
                if num in nums_zone1:
                    counter += 1
                    break
    
    print(counter)


if __name__ == "__main__":
    #part1()
    part2()