#Name: Coach Mack
#Class: 5th Hour
#Assignment: Lecture - Lists

robot_santa_list = ["Ethan K", "Gavin", "Ethan T", "Helber", "Austin", "Anthony", "Santi", "Wyatt",
                    "Jacob", "Max", "Jake", "Cruz", "Lila", "Neely", "Echo", "Adrian",
                    "Oliver"]

print(robot_santa_list)
print(robot_santa_list[10], "is NAUGHTY!")
print(robot_santa_list[1], "is NAUGHTY!")
print(robot_santa_list[0], "is NAUGHTY!")
print(f"{robot_santa_list[13]} is NAUGHTY!")

robot_santa_list.append(input("Insert Person to List: "))
print(robot_santa_list)
print(robot_santa_list[17], "is NAUGHTY!")

robot_santa_list.remove("Santi")
print(robot_santa_list)

robot_santa_list.insert(6, "Santi")
print(robot_santa_list)

robot_santa_list.pop(10)
robot_santa_list.pop(10)
print(robot_santa_list)

num_list = [2479289, 7, 5, 11, -3, 3100000, 6000000000000, 40, 42, 69, 1, 812, 75, 20, 271000, 43]
print(num_list)

num_list.sort()
print(num_list)

num_list.sort(reverse=True)
print(num_list)

num_list_subsum = num_list[1] + num_list[2] + num_list[3]
print(num_list_subsum)

num_list_sum = sum(num_list)
print(num_list_sum)

num_list_len = len(num_list)
print(num_list_len)

mixed_list = ["Fred", 10, False]
print(mixed_list)

mixed_list.sort()
print(mixed_list)