import math

amount = str(input("金額(円)を入力 >"))
amount_len = len(amount)

print("金額:",amount)

# 5の位より上のはなし
if len(amount) > 4:
    manbill = math.floor(int(amount) / 10000)
else:
    manbill = 0

# 4の位(len -4)
four_class = amount[amount_len - 4]
if int(four_class) > 5:
    gosenbill = 1
    senbill = int(four_class) - 5
else:
    gosenbill = 0
    senbill = int(four_class)

# 3の位(len -3)
three_class = amount[amount_len - 3]
if int(three_class) > 5:
    gohyakudama = 1
    hyakudama = int(three_class) - 5
else:
    gohyakudama = 0
    hyakudama = int(three_class)

# 2の位(len -2)
second_class = amount[amount_len - 2]
if int(second_class) > 5:
    gojyudama = 1
    jyudama = int(second_class) - 5
else:
    gojyudama = 0
    jyudama = int(second_class)

# 1の位(len -1)
first_class = amount[amount_len - 1]
if int(first_class) > 5:
    godama = 1
    itidama = int(first_class) - 5
else:
    godama = 0
    itidama = int(first_class)


print("一万円札=", manbill)
print("五千円札=", gosenbill)
print("千円札=", senbill)
print("五百円玉=", gohyakudama)
print("百円玉=", hyakudama)
print("五十円玉=", gojyudama)
print("十円玉=", jyudama)
print("五円玉=", godama)
print("一円玉=", itidama)
