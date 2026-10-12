num = int(input("Enter a number :"))
count = 0
digit = 0
temp = num
product = 0
power = 3
while temp > 0:
    digit = temp%10
    product = product + (digit ** power)
    temp = temp // 10
print(product)