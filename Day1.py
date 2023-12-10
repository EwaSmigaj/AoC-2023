def process_msg(msg):
    number = ""
    msg = word_to_digit(msg)
    for l in msg:
        if l.isnumeric():
            number += str(l)
            break
    for l in reversed(msg):
        if l.isnumeric():
            number += str(l)
            break
    return int(number)


def sum_calibration_values(list):
    sum = 0
    for l in list:
        sum += process_msg(l)
    return sum


def word_to_digit(msg):
    number_name = {1: "one",
                   2: "two",
                   3: "three",
                   4: "four",
                   5: "five",
                   6: "six",
                   7: "seven",
                   8: "eight",
                   9: "nine"}

    idx_dict_min = {1: msg.find(number_name[1]),
                    2: msg.find(number_name[2]),
                    3: msg.find(number_name[3]),
                    4: msg.find(number_name[4]),
                    5: msg.find(number_name[5]),
                    6: msg.find(number_name[6]),
                    7: msg.find(number_name[7]),
                    8: msg.find(number_name[8]),
                    9: msg.find(number_name[9])}

    idx_dict_min = {k: v for k, v in idx_dict_min.items() if v >= 0}

    if len(idx_dict_min) == 0:
        return msg

    idx_dict_max = idx_dict_min.copy()

    for k in idx_dict_max.keys():
        idx_dict_max[k] = msg.rfind(number_name[k])

    first = min(idx_dict_min, key=idx_dict_min.get)
    last = max(idx_dict_max, key=idx_dict_max.get)

    msg = msg[: idx_dict_min[first]] + str(first) + msg[idx_dict_min[first] : idx_dict_max[last]] + str(last) + msg[idx_dict_max[last]:]
    print(msg)
    return msg


file1 = open('input_test_day1.txt', 'r')
lines = file1.readlines()

print(sum_calibration_values(lines))
