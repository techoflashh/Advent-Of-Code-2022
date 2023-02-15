stacklist = [['N', 'S', 'D', 'C', 'V', 'Q', 'T'],['M', 'F', 'V'],['F', 'Q', 'W', 'D', 'P', 'N', 'H', 'M'],['D', 'Q', 'R', 'T', 'F'],['R', 'F', 'M', 'N', 'Q', 'H', 'V', 'B'],['C', 'F', 'G', 'N', 'P', 'W', 'Q'],['W', 'F', 'R', 'L', 'C', 'T'],['T', 'Z', 'N', 'S'],['M', 'S', 'D', 'J', 'R', 'Q', 'H', 'N']]
with open("day5_inputq2.txt") as f:
    while True:
        try:
            a = f.readline()
            temp = a.split(" ")
            for i in range(-int(temp[1]),0):
                b = stacklist[int(temp[3])-1].pop(i)
                stacklist[int(temp[5])-1].append(b)
        except:
            break
print("Question 2")
for i in stacklist:
    print(i[-1],end="")