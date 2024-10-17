EggCount = int(input("Enter #Amount of Eggs Purchased:"))

price = 0
Dozens = EggCount// 12.0
remaining = EggCount % 12.0
remainB = remaining / 12
TotalDozen = Dozens + remainB

if TotalDozen >= 0 and TotalDozen < 4 :
    price = 0.50
elif TotalDozen >= 4 and TotalDozen < 6 :
    price = 0.45
elif TotalDozen >=6 and TotalDozen < 11 :
    price = 0.40
elif TotalDozen <= 11:
    price = 0.35
else:
    print "Invalid Egg #Count"

totalprice = float(round(12*price,2)) * TotalDozen

print "Your Egg Cost: $" + str(round(totalprice,2))

input()