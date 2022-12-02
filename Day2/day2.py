'''
A for Rock, B for Paper, and C for Scissors
X for Rock, Y for Paper, and Z for Scissors
1 for Rock, 2 for Paper, and 3 for Scissors
score of round: 0 if you lost, 3 if the round was a draw, and 6 if you won
1 for Rock, 2 for Paper, and 3 for Scissors

rock beats scissors
scissors beats paper
paper beats rock

X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
'''

def opp_rock(my_choice):
    # rock
    if my_choice == "X":
        return 3 + 1
    # paper
    elif my_choice == "Y":
        return 6 + 2
    # scissors
    elif my_choice == "Z":
        return 0 + 3

def oop_paper(my_choice):
    # rock
    if my_choice == "X":
        return 0 + 1
    # paper
    elif my_choice == "Y":
        return 3 + 2
    # scissors
    elif my_choice == "Z":
        return 6 + 3

def oop_scissors(my_choice):
    # rock
    if my_choice == "X":
        return 6 + 1
    # paper
    elif my_choice == "Y":
        return 0 + 2
    # scissors
    elif my_choice == "Z":
        return 3 + 3


def part1():
    with open('input.txt') as f:
        lines = f.readlines()
    
    your_points = 0
    for full_match in lines:
        oop_choice = full_match[0]
        my_choice = full_match[2]

        if oop_choice == "A":
            your_points += opp_rock(my_choice)
        elif oop_choice == "B":
            your_points += oop_paper(my_choice)
        elif oop_choice == "C":
            your_points += oop_scissors(my_choice)

    print(your_points)        
        

# A
def opp_rock(my_choice):
    if my_choice == "X":
        # i need to loose and choose scissors
        return 0 + 3
    if my_choice == "Y":
        # i need to draw and choose rock
        return 3 + 1
    if my_choice == "Z":
        # I need to win and choose paper
        return 6 + 2

# B
def oop_paper(my_choice):
    if my_choice == "X":
        # i need to loose and choose rock
        return 0 + 1
    if my_choice == "Y":
        # i need to draw and choose paper
        return 3 + 2
    if my_choice == "Z":
        # I need to win and choose scissors
        return 6 + 3
# C
def oop_scissors(my_choice):
    if my_choice == "X":
        # i need to loose and choose paper
        return 0 + 2
    if my_choice == "Y":
        # i need to draw and choose scissors
        return 3 + 3
    if my_choice == "Z":
        # I need to win and choose rock
        return 6 + 1

def part2():
    with open('input.txt') as f:
        lines = f.readlines()
    
    your_points = 0
    for full_match in lines:
        oop_choice = full_match[0]
        my_choice = full_match[2]

        if oop_choice == "A":
            your_points += opp_rock(my_choice)
        elif oop_choice == "B":
            your_points += oop_paper(my_choice)
        elif oop_choice == "C":
            your_points += oop_scissors(my_choice)
    
    print(your_points)
    

if __name__ == "__main__":
    #part1()
    part2()