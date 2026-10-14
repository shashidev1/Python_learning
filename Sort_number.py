def remove_digit(index,num):
    first_part ,second_part,number = 0,0,0
    first_part = num //(10**index)
    second_part = num %(10**(index-1))
    number = first_part*(10**(index-1)) +second_part
    return number
num = int(input("Enter a number :"))
great = num%10
count = 0
digit = 0
temp = num
new_number = 0
sorted_number= 0
gi = count
while True:
    count,great,gi,temp = 0,0,0,num
    while temp>0:
        count+=1
        digit = temp % 10
        temp //=10
        if digit > great:
            gi = count
            great = digit
    new_number = remove_digit(gi,num)
    temp = new_number
    sorted_number = sorted_number*10 +great
    
    num = new_number
    if num == 0:
        break 
print(sorted_number)   