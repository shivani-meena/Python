person_age = int(input())
if person_age <= 2:
    print("Infant")
elif person_age >= 3 and person_age <= 12:
    print("Chlid")
elif person_age >= 13 and person_age <= 19:
    print("Teenager")
elif person_age >= 20 and person_age <= 65:
    print("Adult")
else:
    print("Senior")
