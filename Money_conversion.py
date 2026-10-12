price = int(input("Enter the price to break into note :"))

fiveh = price //500
price = price%500
twoh = price//200
price%=200
oneh = price//100
price%=100
fifty = price//50
price%=50
twenty = price//20
price%=20
ten = price//10
price%=10
five = price//5
price%=5
two = price//2
price%=2
one = price
print("500 :",fiveh)
print("200 :",twoh)
print("100 :",oneh)
print("50 :",fifty)
print("20 :",twenty)
print("10 :",ten)
print("5 :",five)
print("2 :",two)
print("1 :",one)