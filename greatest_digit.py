num = int(input("Enter a number :"))
digit=0
temp = num
great = temp%10
secondlargest = great
while temp>0:
    digit = temp % 10
    temp = temp//10
    if digit>great:
        secondlargest = great
        great = digit
    elif digit>secondlargest and secondlargest!=great:
        secondlargest= digit
print(great,secondlargest)