num = int(input("Enter a number :"))
sign,sum,digit,temp= 1,0,0,num
while temp>0:
    digit =temp%10
    sum = sum + (digit*(sign))
    temp = temp//10
    sign = sign*(-1)
print(sum)
