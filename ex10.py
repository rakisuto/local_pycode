import random
comp = random.randint(0,2)

print("じゃんけんぽんぬ ")
ans = int(input("あなたは？(0:グー, 1:チョキ, 2:パー) > "))

if comp == 0:
    if ans == 1:
        flg = "lose"
    elif ans == 2:
        flg = "win"
    else:
        flg == "draw"

elif comp == 1:
    if ans == 0:
        flg = "win"
    elif ans == 1:
        flg = "draw"
    else:
        flg = "lose"

elif comp == 2:
    if ans == 0:
        flg = "lose"
    elif ans == 1:
        flg = "win"
    else:
        flg = "draw"

else:
    print("不正な値です")
    exit

print(" 私は ", comp, " あなたは ", ans, "→",flg )
