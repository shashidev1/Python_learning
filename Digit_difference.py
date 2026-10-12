num = int(input("Enter a number :"))
first, last, temp,product, difference= 0,0,num,0,0
def length(num):
    count = 0
    while num>0:
        num//=10
        count+=1
    return count
while temp >0:
    if temp < 9:
        difference = difference-temp
        break
    last = temp%10
    first= temp//(10**(length(temp)-1))
    product = last * first
    if difference==0:
        difference = product
        product = 0
    difference = difference - product
    temp = temp//10
    temp = temp%(10**(length(temp)-1))
print(difference)
