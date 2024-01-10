# Decision Statements in Python

# Example 1: Simple if statement
age = 25

if age >= 18:
    print("You are eligible to vote.")

# Example 2: if-else statement
temperature = 30

if temperature > 25:
    print("It's a hot day.")
else:
    print("It's not too hot.")

# Example 3: if-elif-else statement
score = 75

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'D'

print(f"Your grade is: {grade}")

# Example 4: Nested if statements
is_raining = True
is_cold = False

if is_raining:
    print("Bring an umbrella.")
    if is_cold:
        print("Wear a jacket.")
    else:
        print("No need for a jacket.")
else:
    print("Enjoy the weather!")

# Example 5: Ternary conditional expression
age = 22
status = "Minor" if age < 18 else "Adult"
print(f"Status: {status}")
