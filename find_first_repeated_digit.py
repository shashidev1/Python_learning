num = int(input("Enter a number :"))
last_digit = 0
digit = 0
temp = num
while temp>0:
    last_digit = temp%10
    temp//=10
    temp2 = temp
    while temp2>0:
        digit = temp2%10
        temp2//=10
        if digit == last_digit:
            print(digit,"is the first repeated digit in this number\nwhich occured more than 1 time.")
            break
        