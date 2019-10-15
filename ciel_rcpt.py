# cook your dish here

for i in range(int(input())):
    num=int(input())
    if num<=2048:
        num=bin(num)
        c=num.count('1')
        print(c)
    else:
        n=num//2048
        num=bin(num-(n*2048))
        c=num.count('1')
        print(c+n)
