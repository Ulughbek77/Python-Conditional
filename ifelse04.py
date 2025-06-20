balance = 5000

yechish = int(input("qancha yechmoqchisiz? "))
if yechish < 0:
    print("manfiy summa yechish mumkin emas")
if yechish <= balance and yechish >= 0:
    print(f"{yechish} so'm yechib olindi sizning balansingiz {balance - yechish} so'm ")
else:
    print(f"balansda yetarli mablag' yo'q sizning balansingiz {balance} so'm ")