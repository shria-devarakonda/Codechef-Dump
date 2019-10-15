# cook your dish here

n = int(input())
listy = list(map(int, input().split()))
count = 0
uncount = 0
for i in range(n):
    if listy[i] % 2 == 0:
        count = count + 1
    else:
        uncount = uncount + 1
if count>uncount:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
    
