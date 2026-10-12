def length(num):
    count = 0
    temp = num
    while temp>0:
        temp = temp//10
        count+=1
    return count 
num = float(input("Enter a number to remove it's middle digit :"))
middle_index = int((length(num)+1)/2)
temp = num%(10**(middle_index-1))
temp1 = num%(10**(middle_index)) 
num = num//(10**(middle_index)) 
num = num * (10**(middle_index-1))+ temp
print("The new number is : ",int(num))
middle_digit = temp1//(10**(middle_index-1))
print("And the middle digit was :",middle_digit)