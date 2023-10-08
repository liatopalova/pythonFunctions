
my_list = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11]


def mult_nums(list_1):
    num = 1
    for number in list_1:
        num *= number
    return num


print(f"Mult_nums: {mult_nums(my_list)}")


def min_num(list_1):
    return min(list_1)


print(f"Min_num: {min_num(my_list)}")
