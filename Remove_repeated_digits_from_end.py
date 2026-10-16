def remove_digit(index,num):
    first,second,number = 0,0,0
    first = num //(10**index)
    second = num % (10**(index-1))
    number = first *(10**(index-1)) + second
    return number
def len_of_num(num):
    count = 0
    while num>0:
        count+=1
        num//=10
    return count
num = int(input("Enter a number :"))
temp1,temp2 = num,num
starting_index = 1
digit_removed = 0
length_of_number = len_of_num(temp2)
while starting_index <=length_of_number:
    digit = (temp2%(10**starting_index))//(10**(starting_index-1))
    checking_index = starting_index+1
    while checking_index<= length_of_number:
        check_digit = (temp2%(10**checking_index))//(10**(checking_index-1))
        if check_digit == digit:
            temp2 = remove_digit(checking_index,temp2)
            length_of_number-=1
            digit_removed -=1
        else:
            checking_index+=1
    starting_index+=1
print(temp1,temp2)