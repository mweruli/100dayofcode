print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_percentange = tip / 100
total_tip_amount = bill * tip_percentange
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
bill_amount = round(bill_per_person, 2)


print(f"Each person should pay: ${bill_amount}")