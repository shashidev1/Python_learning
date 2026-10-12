num = int(input("Enter a number :"))
digits = []
while num>0:
    digits.append(num%10)
    num//=10
print(digits) 
number = 1234566
print(len(number))