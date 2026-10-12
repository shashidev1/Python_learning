sec = int(input("Enter time in seconds :"))
days = sec // 86400

hours = (sec % 86400)//3600
min = ((sec %86400 )%3600)//60
sec = sec % 60
print(days,hours,min,sec)