case = int(input("数を入力"))
for i in range(0,case):
    print(str(i)+':', end="")
    i = i + 1
    for j in range(0,i):
        print("■",end="")
    print("")
