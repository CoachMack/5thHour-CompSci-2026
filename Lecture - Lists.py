#Name: Coach Mack
#Class: 5th Hour
#Assignment: Lecture - Lists


#This is a list. In essence, it's a variable that has multiple values inside that
#you can pull from any of them without needing to make multiple variables for each
#piece of data. This is useful for cases where you have a lot of the same type of
#"thing", such as names in this example.
robot_santa_list = ["Ethan K", "Gavin", "Ethan T", "Helber", "Austin", "Anthony", "Santi", "Wyatt",
                    "Jacob", "Max", "Jake", "Cruz", "Lila", "Neely", "Echo", "Adrian",
                    "Oliver"]

#To print the list. You simply name the variable followed by [] with the
#number inside being its "index" location.
#Note that all indexes START AT ZERO. Not one. :)
print(robot_santa_list)
print(robot_santa_list[10], "is NAUGHTY!")
print(robot_santa_list[1], "is NAUGHTY!")
print(robot_santa_list[0], "is NAUGHTY!")
print(f"{robot_santa_list[13]} is NAUGHTY!")

#This is the append function. This allows you to tack on a new value or "object"
#to the end of the list.
robot_santa_list.append(input("Insert Person to List: "))
print(robot_santa_list)
print(robot_santa_list[17], "is NAUGHTY!")

#This is the remove function. It removes every instance of the value.
robot_santa_list.remove("Santi")
print(robot_santa_list)

#This is the insert function. It works like the append function but
#you can place the object anywhere inside of the list, not just at the end.
robot_santa_list.insert(6, "Santi")
print(robot_santa_list)

#This is the pop function. It lets you remove a specific value based on
#index location. Put the location of the value, not the value itself.
robot_santa_list.pop(10)
robot_santa_list.pop(10)
print(robot_santa_list)

#This is a number list. You can place any kind of object in a list,
#not just strings.
num_list = [2479289, 7, 5, 11, -3, 3100000, 6000000000000, 40, 42, 69, 1, 812, 75, 20, 271000, 43]
print(num_list)

#You can sort the list from lowest to highest. When you sort a list,
#it permanently changes the order of the list so keep that in mind.
num_list.sort()
print(num_list)

#You can also sort the list from highest to lowest using the
#reverse=True modifier.
num_list.sort(reverse=True)
print(num_list)

#You can do math with the numbers in a list. Simply call their
#index location. Reminder: START AT ZERO.
num_list_subsum = num_list[1] + num_list[2] + num_list[3]
print(num_list_subsum)

#If you need to add them all together, there is a sum function
#that lets you add the contents of a list together.
num_list_sum = sum(num_list)
print(num_list_sum)

#You can find the amount of objects in a list, called the "length",
#using the len function.
num_list_len = len(num_list)
print(num_list_len)

#You can also list different types of objects in the same list.
mixed_list = ["Fred", 10, False]
print(mixed_list)