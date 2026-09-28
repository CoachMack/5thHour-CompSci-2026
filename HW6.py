#Name: Coach Mack
#Class: 5th Hour
#Assignment: HW6


#1. Create a list with 9 different numbers inside.
int_list = [32, 48, 25, 18, 10, 12, 1112, 20, 7]
#2. Sort the list from highest to lowest.
int_list.sort(reverse=True)

#3. Create an empty list.
emp_list = []
#4. Remove the median number from the first list and add it to the second list.
med_int = int_list.pop(4)
emp_list.append(med_int)
#5. Remove the first number from the first list and add it to the second list.
first_int = int_list.pop(0)
emp_list.append(first_int)
#6. Print both lists.
print(int_list)
print(emp_list)
#7. Add the two numbers in the second list together and print the result.
emp_list_sum = emp_list[0] + emp_list[1] #sum(emp_list) also works
print(emp_list_sum)
#8. Add the sum from #7 to the first list.
int_list.append(emp_list_sum)
#9. Sort the first list from lowest to highest and print it.
int_list.sort()
print(int_list)