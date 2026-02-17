birth_year = input("What year were you born?  ")
age = 2026 - int(birth_year) 
print(age)
age = 18
if age <= 18:
    print("Sorry,your are too young to enter.")
elif age >= 18 < 21:
    print("You can enter, but no alcohol.")
else:
    print("Welcome!what would you like to drink.")