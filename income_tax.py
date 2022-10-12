name=(input("Enter your name:"))
income=float(input("Enter your annual gross pay: "))
if income <= 46605:
    tax=income*0.15
if income > 46605 and income <= 93208:
    tax=44701*0.15 + (income-46605)*0.205
if income > 93208 and income <= 144489:
    tax=44701*0.15 + (144489-93208)*0.22 + (income-93208)*0.26
if income > 144489 and income <= 205842:
    tax=44701*0.15 + (93208-46605)*0.205 + (144489-93208)*0.26 + (income-144489)*0.29
if income > 205842:
    tax=44701*0.15 + (93208-46605)*0.205 + (144489-93208)*0.26 + (205842-144489)*0.29 + (income-205842)
print("Your name is", name)
print("Income tax is $", round(tax, 2))