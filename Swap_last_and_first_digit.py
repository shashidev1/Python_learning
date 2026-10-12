def length(number):
    tempnum = num
    count = 0
    while tempnum>0:
        tempnum //=10
        count+=1
    return count
num = int(input("Enter a number to swap first and last digit :"))
last = num%10
first = num//(10**(length(num)-1))
num//=10
num=num%(10**(length(num)-1))
num = num +(last*10**length(num))
num = num * 10 + first
print("The reversed number is now :",num)