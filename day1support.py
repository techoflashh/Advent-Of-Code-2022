mainlst = []
with open("day1_input.txt") as f:
    secondlst=[]
    while True:
        a = f.readline()
        if a == "\n":
            mainlst.append(secondlst)
            secondlst=[]
        else:
            b = int(a[-len(a):-1])
            secondlst.append(b)
            if b==6253:
                mainlst.append(secondlst)
                break
        if len(a)==0:
            break
print(mainlst)