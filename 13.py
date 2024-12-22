salary = float(input("Enter your salary: "))
serviceyears = int(input("Enter your years of service: "))
if serviceyears > 5:
    bonus = salary * 0.05
elif serviceyears <= 5:
    bonus = 0
print("Net bonus amount:", bonus)