a = int(input())
i = 0
while True:
    if(2 ** i > a):
        break
    else:
        print(2**i)
        i += 1