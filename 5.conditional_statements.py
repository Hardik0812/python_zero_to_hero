# if statement

temperature = 35
if temperature > 30:
    print("It's too hot")
print("done")

# if-else statement
temperature = 35
if temperature > 30:
    print("It's too hot")
else:
    print("It's not too hot")
print("done")

# if-elif-else statement
temperature = 35
if temperature > 30:
    print("It's too hot")
elif temperature > 20:
    print("It's not too hot")
else:
    print("its cold")
print("done")

# ternary operator
temperature = 35
print("It's too hot" if temperature > 30 else "It's not too hot")
print("done")

# logical operators

high_income = False
good_credit = True

if high_income and good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


if high_income or good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan") 


high_income = False
good_credit = True
student = True
if not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

if (high_income or good_credit) and not student:
    print("Eligible for loan")
