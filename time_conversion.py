sec = int(input("Enter time in seconds :"))
days = sec // 86400

hours = (sec % 86400)//3600
min = ((sec %86400 )%3600)//60
sec = sec % 60
print(days,hours,min,sec)
# minu = int(input("Enter time in minutes :"))
# hours = minu // 60
# min = minu %60
# print(hours,min)
# hours = float(input("Enter time in hour :"))
# hour = hours//12
# min = hours// 60
# sec = min % 60
# print(hours,min,sec)
