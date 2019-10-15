# cook your dish here

for i in range(int(input())):
    n = int(input())
    listy = list(map(int, input().split()))
    new = listy[int(input())-1]
    listy.sort()
    for i in range(n):
        if listy[i] == new:
            print(i+1)
            break
