# cook your dish here
for i in range(int(input())):
    a, b = map(int, input().split())
    if a>b:
        print((str(int(a)) + " " + str(int(a+b))))
    else:
        print((str(int(b)) + " " + str(int(a+b))))
