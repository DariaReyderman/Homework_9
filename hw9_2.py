list01 = []
count: int = 0
while True:
    number: int = int(input("Enter a number: "))
    if number == -999:
        break
    if number < 0 or number > 10:
        continue
    list01.append(number)
    print("Statistics:", end=" ")
    for i in range(11):
        list01.count(i)
        if i in list01:
            print(f"{[i]}: {list01.count(i)}", end=" ")
        else:
            continue
    print()
