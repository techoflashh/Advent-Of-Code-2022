mainlst = []
with open("day2_input.txt") as f:
    while True:
        a = f.readline()
        mainlst.append(a[0:3])
        if a=="":
            break
print(mainlst)