

def part1():
    with open('input.txt') as f:
        lines = f.readlines()
    
    crates = [[], [], [], [], [], [], [], [], []]
    while len(lines) > 0:
        cur_line = lines.pop(0)

        if (cur_line[0] == "[" or cur_line[0] == " ") and cur_line[0] != "m" and cur_line[1] != '1':
            # index 1, 5, 9
            index_of_letter = 1
            for i in range(9):
                crates[i].append(cur_line[index_of_letter])
                index_of_letter += 4
        
        if (cur_line[0] == "m"):
            # moving the crates
            get_nums = cur_line.split(" ")
            num_crates_to_move = int(get_nums[1])
            stack_to_take_from = int(get_nums[3])
            stack_to_move_to = int(get_nums[5])
            
            for i in range(num_crates_to_move):
                check_not_null = ' '
                while check_not_null == ' ':
                    letter_to_move = crates[stack_to_take_from - 1].pop(0)
                    check_not_null = letter_to_move

                if len(crates[stack_to_move_to - 1]) == 0:
                    crates[stack_to_move_to - 1].append(letter_to_move)
                elif crates[stack_to_move_to - 1][0] == " ":
                    index_check = 0
                    while crates[stack_to_move_to - 1][index_check] == " ":
                        index_check += 1
                    
                    crates[stack_to_move_to - 1][index_check - 1] = letter_to_move
                else:
                    crates[stack_to_move_to - 1].insert(0, letter_to_move)

    for i in range(len(crates)):
        print(crates[i][0])


def part2():
    with open('input.txt') as f:
        lines = f.readlines()
    
    crates = [[], [], [], [], [], [], [], [], []]
    while len(lines) > 0:
        cur_line = lines.pop(0)

        if (cur_line[0] == "[" or cur_line[0] == " ") and cur_line[0] != "m" and cur_line[1] != '1':
            # index 1, 5, 9
            index_of_letter = 1
            for i in range(9):
                crates[i].append(cur_line[index_of_letter])
                index_of_letter += 4
        
        if (cur_line[0] == "m"):
            # moving the crates
            get_nums = cur_line.split(" ")
            num_crates_to_move = int(get_nums[1])
            stack_to_take_from = int(get_nums[3])
            stack_to_move_to = int(get_nums[5])

            index = 0
            if len(crates[stack_to_take_from - 1]) > 0:
                while crates[stack_to_take_from - 1][index] == ' ':
                    index += 1
            
            list_of_chars_to_move = []
            for i in range(num_crates_to_move):
                # i want to make a list of nums to move instead of just getting the characters
                char = crates[stack_to_take_from - 1].pop(index)
                list_of_chars_to_move.append(char)
                
            if len(crates[stack_to_move_to - 1]) == 0:
                crates[stack_to_move_to - 1] = list_of_chars_to_move
            elif crates[stack_to_move_to - 1][0] == " ":
                while crates[stack_to_move_to - 1][0] == " ":
                    crates[stack_to_move_to - 1].pop(0)
                
                cur_list = crates[stack_to_move_to - 1]
                crates[stack_to_move_to - 1] = list_of_chars_to_move + cur_list
            else:
                cur_list = crates[stack_to_move_to - 1]
                crates[stack_to_move_to - 1] = list_of_chars_to_move + cur_list
            
    for i in range(len(crates)):
        print(crates[i][0])



if __name__ == "__main__":
    #part1()
    part2()