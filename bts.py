for i in range(int(input())):
    count = 0
    num = int(input())
    x = 5
    while x <= num:
        count += num//x
        x *= 5
    print(count)
