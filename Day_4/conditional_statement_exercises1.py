# Exercise 1
number = int(input("Give me a number:"))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Exercise 2
temperature = int(input("Please enter the temperature in Celsius"))
if temperature < 0:
    print("Invalid Temperature")
elif temperature >= 0 and temperature < 15:
    print("Cold")
elif temperature >= 15 and temperature <= 25:
    print("Warm")
else:
    print("Hot")

# Exercise 3
age = int(input("Enter your age: "))
citizenship = input("Are you a citizen? (yes/ no): ").lower()
if age >= 18:
    if citizenship == "yes":
        print("Eligible to vote.")
    else:
        print("Not eligible: Must be a citizen.")
else:
    print("Not eligible: Must be 18 or older.")
