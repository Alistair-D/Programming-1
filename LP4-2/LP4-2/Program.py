
print int(input("Enter Package Weight In Kilograms: "))
print int(input("Enter Package Length in Centimters: "))
print int(input("Enter Package Width in Centimters: "))
print int(input("Enter Package Height in Centimters: "))

CubicMeter = Length * Width * Height

if Weight <= 27 and CubicMeter <= 100000:
    print("Package is Good")
elif Weight > 27 and CubicMeter <= 100000:
    print("Too Heavy")
elif Weight <= 27 and CubicMeter > 100000:
    print("Too Large")
elif Weight > 27 and CubicMeter > 100000:
    print("Too Large and Heavy")
else:
    print("Invalid Package Logistics")



input()