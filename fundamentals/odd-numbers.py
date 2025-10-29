numbers=[3, 9, 1, 10, 5, 2, 8]
for number in numbers:
    if number % 2 == 0:
        print("{number} is Even".format(number=number))
    else:
        print("{number} is Odd".format(number=number))

# program to countdown timer
timer = 11
while timer != 0:
    timer -= 1
    print(timer)
    if timer == 5:
        print("Halfway point reached!")
    