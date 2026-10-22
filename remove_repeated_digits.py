def lenght_of_num(num):
    count = 0
    while num > 0:
        count+=1
        num//=10
    return count
num = int(input("Enter a number :"))
length = lenght_of_num(num)
firstdigit = num // (10**(length-1))
temp = num
result = 0
while temp>0:
    digit = temp%10
    if digit != firstdigit:
        result = result*10 + digit
    temp//=10
print("Number after removing repeated digits:", result)
final = 0
while result>0:
    digit = result%10
    final = final*10 + digit
    result//=10
print("Final number after reversing:", final)