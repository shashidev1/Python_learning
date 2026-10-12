num = int(input("Enter a number :"))
count, first, second,addition,temp = 1,0,0,0, num
while temp>9:
    first = temp%(10**count)
    second = (temp//(10**count)) % (10**count)
    addition = addition +(first *second)
    temp = temp//10
print(addition)