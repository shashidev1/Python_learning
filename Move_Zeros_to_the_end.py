def remove_digit(index,num):
    first = num//(10**index)
    second = num%(10**(index-1))
    number = first*(10**(index-1)) +second
    return number *10
num = int(input("Enter a number :"))
count = 1
digit = 0
temp = num
while temp > 0:
    digit = temp%10
    if digit == 0:
        num = remove_digit(count,num)
        count += 1
    else :
        count+=1
    temp //=10
print("The number after moving all zeros to the end is :",num)