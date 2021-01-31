num_1 = int(input("数1 > "))
num_2 = int(input("数2 > "))
num_3 = int(input("数3 > "))

first = max(num_1,num_2,num_3)
if first == num_1:
    second = max(num_2,num_3)
    third = min(num_2,num_3)
elif first == num_2:
    second = max(num_1,num_3)
    third = min(num_1,num_3)
elif first == num_3:
    second = max(num_1,num_2)
    third = min(num_1,num_2)

print(first,second,third)


