# cook your dish here
for i in range (int(input())):
    n = int(input())
    listy = list(map(int, input().split()))
    listy.sort()
    diff = 10**20
    for a in range(n - 1):
        tempdiff = listy[a+1] - listy[a]
        if tempdiff<diff:
            diff = tempdiff
    print(diff)
