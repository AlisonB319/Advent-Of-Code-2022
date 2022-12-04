def part1():
    with open('input.txt') as f:
        lines = f.readlines()

    dup_letters = []
    for line in lines:
        first_half  = line[:len(line)//2]
        second_half = line[len(line)//2:]

        first_half_letters = {}
        for letter in first_half:
            if letter in first_half_letters:
                first_half_letters[letter] += 1
            else:
                first_half_letters[letter] = 1
        
        for letter in second_half:
            if letter in first_half_letters:
                dup_letters.append(letter)
                break

    points = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14,
    "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26,
    "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34, "I": 35, "J": 36, "K": 37, "L": 38, "M": 39, "N": 40,
    "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45, "T": 46, "U": 47, "V": 48, "W": 49, "X": 50, "Y": 51, "Z": 52}

    score = 0
    for letter in dup_letters:
        score += points[letter]
        
    print(score)

def part2():
    with open('input.txt') as f:
        lines = f.readlines()
    
    trip_letters = []
    while len(lines) > 0:
        cur_process = []
        letter_tracking = {}
        for i in range(3):
            cur_process.append(lines.pop(0))
        
        for letter in cur_process[0]:
            letter_tracking[letter] = 1
        
        for letter in cur_process[1]:
            if letter in letter_tracking:
                letter_tracking[letter] = 2
        
        for letter in cur_process[2]:
            if letter in letter_tracking and letter_tracking[letter] == 2:
                trip_letters.append(letter)
                break
                    
    points = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14,
    "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26,
    "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34, "I": 35, "J": 36, "K": 37, "L": 38, "M": 39, "N": 40,
    "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45, "T": 46, "U": 47, "V": 48, "W": 49, "X": 50, "Y": 51, "Z": 52}

    score = 0
    for letter in trip_letters:
        score += points[letter]
    print(score)

if __name__ == "__main__":
    #part1()
    part2()