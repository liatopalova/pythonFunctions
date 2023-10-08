print("1.Mult_nums/n2.Min_num/n3.Prime_count/n4.Remove_num/n5.Com_elem/n6.Get_num_pow")
user_select = int(input("Enter menu item: "))

my_list = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11]

match user_select:
    case 1:
        def mult_nums(list_1):
            num = 1
            for number in list_1:
                num *= number
            return num


        print(f"Mult_nums: {mult_nums(my_list)}")
    case 2:
        def min_num(list_1):
            return min(list_1)


        print(f"Min_num: {min_num(my_list)}")
    case 3:
        def count_primes(list_1):
            count = 0
            for num in list_1:
                if num > 1:
                    for n in range(2, num):
                        if num % n == 0:
                            break
                    else:
                        count += 1
            return count


        prime_count = count_primes(my_list)
        print(f"Prime_count: {prime_count}")
    case 4:
        def remove_num(list_1, num_remove):
            count_num = 0
            for num in list_1.copy():
                if num == num_remove:
                    list_1.remove(num)
                    count_num += 1

            return count_num


        num_to_remove = int(input("Enter num: "))
        print(remove_num(my_list, num_to_remove))
    case 5:
        def com_elem(list_1, list_2):
            new_list = set(list_2).intersection(set(list_1))
            return list(new_list)


        my_list_2 = [5, 8, 9, 12, 3]
        print(com_elem(my_list, my_list_2))
    case 6:
        def get_num_pow(list_1, degree):
            list_new = []
            for num in list_1:
                if degree <= 1:
                    return num
                list_new.append(num ** 3)

            return list_new


        print(get_num_pow(my_list, 3))
    case _:
        print("Error!!!")
