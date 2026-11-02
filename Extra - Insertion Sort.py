import random as r

def in_sort(list_to_sort):
    len_list = len(list_to_sort)
    if len_list <= 1:
        return
    for i in range(1, len_list):
        hold = list_to_sort[i]
        select_value = i - 1
        print(list_to_sort)
        while select_value >= 0 and hold < list_to_sort[select_value]:
            list_to_sort[select_value + 1] = list_to_sort[select_value]
            select_value -= 1
        list_to_sort[select_value + 1] = hold

def gen_list(list_to_sort):
    for i in range(int(input("How many numbers in the list?"))):
        num = r.randint(1,100)
        list_to_sort.append(num)

list_to_sort = []
gen_list(list_to_sort)
in_sort(list_to_sort)
print(list_to_sort)

