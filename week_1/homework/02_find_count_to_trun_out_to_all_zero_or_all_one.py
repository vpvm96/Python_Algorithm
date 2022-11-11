input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    zero = 0
    one = 0

    if string[0] == "0":
        zero += 1
    elif string[0] == "1":
        one += 1

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == "0":
                zero += 1
            if string[i + 1] == "1":
                one += 1

    return min(zero, one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
