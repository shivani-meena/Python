Write a program that takes a student's score (out of 100) and outputs their grade based on the following conditions:

1. 90-100: Grade A
2. 80-89: Grade B
3. 70-79: Grade C
4. 60-69: Grade D
5. Below 60: Grade F

score = int(input()) 
if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score <= 89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
elif score >= 60 and score <= 69:
    print("D")
else:
    print("F")

