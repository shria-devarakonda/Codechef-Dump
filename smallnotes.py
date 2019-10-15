# cook your dish here
for _ in range(int(input())):
    num = int(input())
    listy = [1, 2, 5, 10, 50, 100]
    cnt = 0
    while(num!=0):
        a = listy.pop()
        b = num/a
        c = num%a
        cnt = cnt + int(b)
        num = c
    print(cnt)
    
