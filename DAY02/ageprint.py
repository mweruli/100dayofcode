# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
ageconvert = int(age)
age_remaining = 90 - ageconvert

daysofyear = age_remaining * 365
weeksofyear = age_remaining * 52
monthsofyear = age_remaining * 12

message = f"You have {daysofyear} days, {weeksofyear} weeks, and {monthsofyear} months left."

print(message)








