def remove_num(index,num,length_decrease):
    lastnum,firstnum= 0,0
    firstnum = num //( 10**(index))
    lastnum = num % (10**(index-1))
    num = firstnum*(10**(index-1)) + lastnum
    length_decrease +=1
    return num, length_decrease
def lenght_of_num(num):
    count = 0
    while num>0:
        count+=1
        num//=10
    return count 
num = int(input("Enter a number: "))
lastdigit,temp,count,digits,repeat,length_decrease,length_of_num,length_of_digits_done = 0,num,0,0,1,0,0,0
length_of_num = lenght_of_num(num)
while temp>0:
    lastdigit = temp%10
    temp = temp//10
    length_of_num-=1
    while lastdigit != digits and length_of_digits_done<length_of_num:
        digits = (temp//(10**count))%10
        length_of_digits_done +=1
        count+=1
        if lastdigit==digits:
            repeat+=1
            temp, length_decrease = remove_num(length_of_digits_done,temp,length_decrease)
            digits,count,length_of_digits_done = None,count -1,length_of_digits_done-1
    print("Digit",lastdigit,"has occured",repeat,"times.")
    lastdigit,count,digits,repeat,length_decrease,length_of_digits_done = 0,0,0,1,0,0
    length_of_num = None
    length_of_num = lenght_of_num(temp)
