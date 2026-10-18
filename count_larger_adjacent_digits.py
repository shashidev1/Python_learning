num = int(input("Enter a number :"))
count = 0
temp = num
while temp>0:
    digit = temp%10
    temp //=10
    digit2 = temp%10
    if digit<digit2:
        count += 1
print("The count of larger adjacent digits is :",count)