import re

# part 1
def get_sum_of_possible_games_nb(file_name):
    file1 = open('TestData/' + file_name, 'r')
    lines = file1.readlines()
    sum = 0

    for i in range(1, len(lines)+1):
        line = lines[i-1].split(":")[1]
        if is_game_possible(line):
            sum += i

    return sum


def is_game_possible(line):
    if sorted([int(x) for x in re.findall(r'\d+', line)], reverse=True)[0] > 14:
        return False
    balls_limits = {"green": 13, "blue": 14, "red": 12}
    line_split = re.split(';|,', line)
    for element in line_split:
        element = element.split()
        if balls_limits[element[1]] < int(element[0]):
            return False
    return True


# print(get_sum_of_possible_games_nb("input_day2.txt"))


# part 2
def get_sum_of_powers(file_name):
    file1 = open('TestData/' + file_name, 'r')
    lines = file1.readlines()
    sum = 0

    for l in lines:
        line = l.split(":")[1]
        dict_of_min = get_min_possible_set(line)
        power = 1
        for val in dict_of_min.values():
            power = power * val
        sum += power
    return sum


def get_min_possible_set(line):
    balls_limits = {"green": 0, "blue": 0, "red": 0}
    line_split = re.split(';|,', line)
    for element in line_split:
        element = element.split()
        if balls_limits[element[1]] < int(element[0]):
            balls_limits[element[1]] = int(element[0])
    return balls_limits


print(get_sum_of_powers("input_test_day2.txt"))
