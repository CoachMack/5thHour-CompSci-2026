#Name: Coach Mack
#Class: 5th Hour
#Assignment: Lecture - Conditional Statements

import random

#This section is a conditional statment (AKA an "if then" or "if else" statement).
#These are used for giving your code specific directions based on whatever rules you
#set for it. There are three different types of conditional statements.

#if = Check to see if this condition is valid.
#elif = Short for "else if". Check to see if this condition is valid if the first isn't.
#else = If no other condition is valid, do this.

#Often you have conditional statements being compared using logical conditions from mathematics.

#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b

coin = random.randint(0,1)

if coin == 0:
    print("Heads")
else:
    print("Tails")

a = random.randint(1,10)
b = random.randint(1,10)

print(a,b)

if a > b:
    print("A is greater than B")
elif a < b:
    print("A is less than B")
else:
    print("A is equal to B")


c = 6
d = 6
e = 8

if c <= d and c <= e:
    print("C is the lowest number")
elif c > d or c > e:
    print("C is NOT the lowest number")


f = 3
g = 7

if f < g:
    f += g
    print(f)
elif f >= g:
    f = f - g
    print(f)

h = random.randint(1,100)

if h % 2 == 0:
    print(f"{h} is even")
else:
    print(f"{h} is odd")

i = random.randint(1,30)

if i >= 10:
    if i >= 20:
        print(f"{i} is greater than 20!")
    else:
        print(f"{i} is greater than 10 but less than 20!")
elif i < 10:
    if i >= 5:
        print(f"{i} is greater than 5 but less than 10!")
    else:
        print(f"{i} is less than 5!")
