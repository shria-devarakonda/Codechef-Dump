# cook your code here
a, b = map(int, input().split())
num = a-b
if num%10!=9:
    final = num+1
else:
    final = num-1
print(final)
