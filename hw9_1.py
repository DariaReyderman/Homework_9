# a + b

list_of_temperature: list[float] = []
while True:
    temperature: float = float(input("Enter a temperature: "))
    if temperature == -999:
        break
    if temperature < -50 or temperature > 50:
        continue
    list_of_temperature.append(temperature)
print("a+b")
print(list_of_temperature)

# c
print("c")
list1: list[float] = [-20.0, 39.1, 18.5]
list_of_temperature.extend(list1)
print(list_of_temperature)

# d
"""
If you'll use (+) you get the feedback, but it doesn't change the variables.
If you'll use list1.extend(list2) you won't get the feedback, but it will change your first variable (e.c. list1) 
"""

# e
print("e")
print(f"The highest temperature is {max(list_of_temperature)}")
print(f"The lowest temperature is {min(list_of_temperature)}")

# f
print("f")
is_temp_in_list: bool = False
for temperature in list_of_temperature:
    if temperature == 18.5:
        is_temp_in_list = True
print(f"18.5 is in the list? ", is_temp_in_list)

# g
print("g")
print(f"the temperature '-20.0' entered {list_of_temperature.count(-20.0)} times")

# h
print("h")
print(f"Average temperature is {sum(list_of_temperature) / len(list_of_temperature):.2f}")

# i
print("i")
for x in list_of_temperature:
    print(x)

# j
print("j")
print(f"The index of '39.1' is {list_of_temperature.index(39.1)}")

# k
print("k")
del list_of_temperature[0]
print(list_of_temperature)

# l
print("l")
del list_of_temperature[2::2]
print(list_of_temperature)

# m
is_temp_in_list: bool = False
for temperature in list_of_temperature:
    if temperature == 18.5:
        is_temp_in_list = True
print(f"18.5 is in the list? ", is_temp_in_list)
list_of_temperature.remove(18.5)
print(list_of_temperature)
# We need first check if the item is in the list, because if it's not there, the code will stop working

# n
temp_last: float = list_of_temperature.pop()
print(list_of_temperature)

# o
list_1 = list_of_temperature.copy()
print(f"before sort: {list_1}")
list_1.sort()
print(f"after sort: {list_1}")

# p
list_2 = list_of_temperature.copy()
print(f"before sort: {list_2}")
list_2.sort(reverse=True)
print(f"after sort: {list_2}")
