# cook your dish here
for i in range(int(input())):
    a = input()
    b = a[::-1]
    if int(a) == int(b):
        print("wins")
    else:
        print("losses")
    
