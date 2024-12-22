grade = int(input("Enter the grade: "))
if grade < 25:
    print("D")
elif 25 <= grade < 45:
    print("C")
elif 45 <= grade < 50:
    print("B")
elif 50 <= grade < 60:
    print("B+")
elif 60 <= grade < 80:
    print("A")
else:
    print("A+")