num = int(input("Enter a number :"))
long_count = 1
previous_count = 1
temp = num
digit , digit2 = 0,0
while temp > 0:
    digit = temp % 10
    temp //=10
    digit2 = temp%10
    if digit == digit2:
        long_count +=1
    else:
        if long_count > previous_count:
            previous_count = long_count
        long_count =1
print(long_count)
print(previous_count)