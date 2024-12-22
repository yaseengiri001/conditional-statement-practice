salary = 50000
years_of_service = 7
if years_of_service > 10:
        bonus = salary * 0.10
elif 6 <= years_of_service <= 10:
        bonus = salary * 0.08
elif years_of_service < 6:
        bonus = salary * 0.05
print(f"The bonus is: {(bonus)}")
