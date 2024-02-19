<h3>Python-For-Absolute-Beginners</h3>

# Decision Statement
Decision statements, also known as conditional statements, are fundamental building blocks in Python that control the flow of your program based on certain conditions. These statements allow you to execute different lines of code depending on whether a specific condition is true or false.

Here are the main types of decision statements in Python:

## 1. if statement:

The if statement is the simplest form of decision making. It evaluates a condition, and if the condition is True, the code block indented below the if statement is executed. If the condition is False, that block is skipped.

Example:
```python
age = 25

if age >= 18:
    print("You are eligible to vote.")
```
## 2. if-else statement:

The if-else statement expands on the basic if statement by providing an alternative code block to execute if the initial condition is False.

Example:
```python
temperature = 30

if temperature > 25:
    print("It's a hot day.")
else:
    print("It's not too hot.")

```
## 3. if-elif-else chain:

This allows you to check multiple conditions sequentially and execute different code blocks depending on which condition is met first.

Example:
```python
grade = 85

if grade >= 90:
    print("Excellent!")
elif grade >= 80:
    print("Great job!")
else:
    print("Keep practicing!")

```
## 4. Nested if statements:

You can nest if statements within other if statements to create more complex decision structures.

Example:
```python
day = "Friday"
time = 16

if day == "Friday":
    if time > 17:
        print("Happy weekend!")
    else:
        print("Hang in there!")
else:
    print("Keep working!")

```

<h3>Get Start with if, else statement</h3>
1. Checking for even or odd numbers:

```python
day = "Friday"
time = 16

if day == "Friday":
    if time > 17:
        print("Happy weekend!")
    else:
        print("Hang in there!")
else:
    print("Keep working!")

```
2. Determining age group:

```python
age = 16

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

```
3. Choosing movie genre:

```Python
genre = "comedy"

if genre == "action":
    print("Here are some exciting action movies!")
elif genre == "comedy":
    print("Ready for some laughs? Check out these hilarious comedies!")
else:
    print("We have a wide variety of genres. Try searching again!")
```
4. Grading based on scores:

```Python
score = 88

if score >= 90:
    print("Excellent! You got an A.")
elif score >= 80:
    print("Great job! You got a B.")
elif score >= 70:
    print("Good effort! You got a C.")
else:
    print("Keep practicing! You can do better.")
```
5. Checking weather conditions:

```Python
is_raining = False
temperature = 22

if is_raining:
    print("Bring an umbrella, it's raining!")
elif temperature > 25:
    print("Wear light clothes, it's hot!")
else:
    print("Enjoy the weather!")
```
6. Checking for vowels:

```Python
letter = 'u'

if letter in ['a', 'e', 'i', 'o', 'u']:
    print(f"{letter} is a vowel.")
else:
    print(f"{letter} is not a vowel.")
```
7. Choosing a fruit based on color:
   
```Python
color = 'red'

if color == 'red':
    print("Choose an apple, strawberry, or cherry!")
elif color == 'yellow':
    print("Go for a banana, pineapple, or lemon!")
else:
    print("Tell me your favorite color for more fruit suggestions!")
```
8. Granting access based on age:

```Python
age = 14

if age >= 18:
    print("Welcome! You have full access.")
elif age >= 13:
    print("Welcome! You have access to age-appropriate content.")
else:
    print("Sorry, this content is restricted for older users.")
```
9. Calculating discount based on purchase amount:

```Python
amount = 100

if amount >= 50:
    discount = 10
    print(f"Congratulations! You get a ${discount} discount.")
else:
    print("Thank you for your purchase!")
```
10.Simulating a coin flip:

```Python
import random

coin_toss = random.randint(0, 1)  # 0 for heads, 1 for tails

if coin_toss == 0:
    print("Heads!")
else:
    print("Tails!")
```
11. Movie Ticket Pricing:

```Python
age = 30
day = "Wednesday"
time = 18  # Hours (1 PM)

if (age >= 65) or (day == "Tuesday" and time < 12):  # Senior discount or Tuesday matinee
    print("Ticket price: $5")
elif age < 18:  # Child price
    print("Ticket price: $8")
else:  # Standard price
    print("Ticket price: $12")
```
12. Leap Year Check:

```Python
year = 2024

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
```
13. Vowel or Consonant Identification:

```Python
char = "x"

if char in "aeiouAEIOU":
    print(f"{char} is a vowel.")
elif char.isalpha():
    print(f"{char} is a consonant.")
else:
    print(f"{char} is not an alphabetic character.")
```
14. Traffic Light Simulator:

```Python
color = "red"

if color == "red":
    print("Stop!")
elif color == "yellow":
    print("Caution, prepare to stop.")
elif color == "green":
    print("Go!")
else:
    print("Invalid traffic light color.")
```
15. Rock-Paper-Scissors Game (Simplified):

```Python
player_choice = "rock"
computer_choice = random.choice(["rock", "paper", "scissors"])

if player_choice == computer_choice:
    print("Tie!")
elif (player_choice == "rock" and computer_choice == "scissors") or \
     (player_choice == "paper" and computer_choice == "rock") or \
     (player_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("You lose!")
```
16. Number Guessing Game (Basic):

```Python
secret_number = 42
guess = int(input("Guess a number between 1 and 100: "))

if guess == secret_number:
    print("Congratulations, you guessed the number!")
elif guess < secret_number:
    print("Too low, try again!")
else:
    print("Too high, try again!")
```
17. Password Validation:

```Python
password = "password123"

if len(password) >= 8 and (any(char.isdigit() for char in password) and any(char.isalpha() for char in password)):
    print("Password is valid.")
else:
    print("Password must be at least 8 characters and contain both letters and numbers.")
```
18. Triangle Type Classification:

```Python
side1 = 5
side2 = 5
side3 = 5

if side1 == side2 and side2 == side3:
    print("Equilateral triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
```
19. Student Grade Calculation (Weighted Average):

```Python
exam_score = 85
project_score = 90
quiz_score = 78

weight_exam = 0.6
weight_project = 0.2
weight_quiz = 0.2

average_score = (exam_score * weight_exam) + (project_score * weight_project) + (quiz_score * weight_quiz)

if average_score >= 90:
    print("Grade: A")
elif average_score >= 80:
    print("Grade: B")
elif average_score >= 70:
    print("Grade: C")
else:
    print("Grade: D or F")
```
20. Loan Eligibility Check:

```Python
salary = 50000
credit_score = 720
loan_amount = 100000

min_salary = 40000
min_credit_
```

<h3>let goto Nested if, else statement</h3>


1. Grade Calculator with Letter Grade and Comments:

```Python
score = 85

if score >= 90:
    letter_grade = "A"
    comment = "Excellent!"
elif score >= 80:
    letter_grade = "B"
    comment = "Great job!"
elif score >= 70:
    letter_grade = "C"
    comment = "Good effort!"
else:
    letter_grade = "F"
    comment = "Keep practicing!"

print(f"Your letter grade is: {letter_grade}")
print(f"Comment: {comment}")
```
Output:
<pre>
Your letter grade is: B
Comment: Great job!
</pre>

2. Leap Year Checker:

```Python
year = 2024

if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")
```
Output:
<pre>
Leap year
</pre>
3. Vowel or Consonant Identifier:

```Python
letter = "u"

if letter in "aeiou":
    print("Vowel")
else:
    print("Consonant")
```
Output:

<pre>
  Vowel
</pre>
4. Traffic Light Simulator:

```Python
light = "yellow"

if light == "red":
    print("Stop!")
elif light == "yellow":
    print("Caution!")
else:
    print("Go!")
```
Output:
<pre>
Caution!
</pre>
5. Number Guessing Game (Easy Mode):

```Python
guess = 5
secret_number = 7

if guess == secret_number:
    print("Congratulations! You guessed the number.")
else:
    print("Oops! Try again.")
```
Output:
<pre>
Oops! Try again.
</pre>

6. Complex Grade Calculator with Bonus and Penalty:

```Python
score = 87
has_bonus = True
missed_assignment = False

if has_bonus:
    score += 5
else:
    if missed_assignment:
        score -= 10

if score >= 90:
    letter_grade = "A"
elif score >= 80:
    letter_grade = "B"
elif score >= 70:
    letter_grade = "C"
else:
    letter_grade = "F"

print(f"Your letter grade is: {letter_grade}")
```
Output: 
<pre>
(Assuming has_bonus is True and missed_assignment is False)
Your letter grade is: B
</pre>
7. Eligibility Checker for Loan Application:

```Python
age = 28
income = 50000
credit_score = 720

if age >= 25 and income >= 40000:
    if credit_score >= 700:
        print("Eligible for loan")
    else:
        print("Credit score needs improvement")
else:
    print("Not eligible for loan")
```
Output: 
<pre>
(Assuming all conditions are met)
Eligible for loan
</pre>
8. Tic-Tac-Toe Game Logic (Simplified):

```Python
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player = "X"
move = 5

if board[move - 1] == " ":
    board[move - 1] = player
else:
    print("Invalid move. Try again.")

if board[0] == player and board[1] == player and board[2] == player:
    print(f"{player} wins!")
# Check other winning conditions here...

player = "O" if player == "X" else "X"  # Switch players
```
Output:
<pre>
(Assuming a valid move is made)
Board updated. Player O's turn.
</pre>
9. Movie Recommendation System (Genre and Mood):

```Python
genre = "action"
mood = "thrilling"

if genre == "action":
    if mood == "thrilling":
        print("Action thriller movies: Mission: Impossible, John Wick")
    elif mood == "comedy":
        print("Action comedy movies
```


# Escape Characters in Python

Escape characters in Python are a special way to represent characters that wouldn't otherwise be possible within a string literal. They consist of a backslash (\) followed by another character to indicate a specific meaning. These characters are essential for including quotes, backslashes, newlines, and other control characters within your strings.

Here are some common escape characters in Python:

- \' (Single quote): Used to represent a single quote within a string defined with single quotes.
``` python
# Single quote within single-quoted string
print('He said, "Hello!"')
```
- \" (Double quote): Used to represent a double quote within a string defined with double quotes.
``` python
# Double quote within double-quoted string
print("It's my birthday!")
```
- \n (Newline): Inserts a newline character, moving the cursor to the beginning of the next line.
``` python
# Newline to create a multi-line string
print("This is\na multi-line\nstring.")
```
- \t (Tab): Inserts a horizontal tab character, moving the cursor to the next tab stop.
``` python
# Tab to indent text
print("\tWelcome\tto my program!")
```
- \` (Backslash): Inserts a single backslash character.
``` python
# Backslash to represent itself
print("The path is C:\\Users\\John")
```
- \a` (Bell): Produces an audible bell sound (if supported by your terminal).
``` python
print("This is a message!\a")
```
- \f` (Form feed): Moves the cursor to the beginning of the current page (not commonly used today).
``` python
print("This is the first line.")
print("\f")  # Insert form feed character
print("This is the second line, which should appear at the beginning of the page.")
```
- \r` (Carriage return): Moves the cursor to the beginning of the current line (mostly used for compatibility).
``` python
for i in range(1, 6):
    print(f"{i}\r", end="")
```

It's important to note that escape characters only have special meaning within string literals. Outside of strings, a backslash followed by another character is treated literally.
