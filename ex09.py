s = int(input("西暦を入力してください > "))

if ( s % 400 == 0 and s % 100 != 0 ):
    print(s,"はうるう年")
elif ( s % 4 == 0 ):
    print(s,"はうるう年")
else:
    print(s,"はうるう年ではない")
