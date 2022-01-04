# Made By Bl4ky

name_1 = input("Enter the First Person's Name:  ")
age_1 = int(input("Enter the First Person's Age:  "))

name_2 = input("Enter the Seccond Person's Name:  ")
age_2 = int(input("Enter the Seccond Person's Age:  "))

difference_age = abs(age_1 - age_2)

if age_1 > age_2:
    print(f"{name_1} is Older than {name_2} by {difference_age} years")
elif age_1 < age_2:
    print(f"{name_2} is Older than {name_1} by {difference_age} years")
elif difference_age == 0:
    print(f"{name_1} and {name_2} have the same age")
