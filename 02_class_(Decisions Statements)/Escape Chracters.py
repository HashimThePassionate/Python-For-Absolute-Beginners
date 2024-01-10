# Escape Characters in Python

# Newline Character (\n)
print("Hello, World!\nHow are you today?")

# Tab Character (\t)
print("Name:\tJohn Doe")

# Backslash Character (\\)
print("This is a backslash: \\")

# Double Quote (\")
print("She said, \"Python is awesome!\"")

# Single Quote (\')
print('He\'s learning Python.')

# Raw String (r prefix)
raw_string = r"This is a raw string \n without interpreting escape characters."
print(raw_string)


# Escape Characters in Python - Additional Examples

# Multiple lines using triple-quoted strings
multi_line_text = """This is a multiline string.
It spans across multiple lines.
Using triple quotes makes it easy."""
print(multi_line_text)

# Combining newline and tab characters
combined_escape = "First line\nSecond line\tIndented"
print(combined_escape)

# Unicode escape sequence
unicode_escape = "\u03B1 is the Greek letter alpha"
print(unicode_escape)

# Bell sound escape character
bell_sound = "Beep!\a"
print(bell_sound)

# Carriage return and backspace
carriage_return = "This text will\roverwrite."
backspace = "Back\bspace removes the previous character."
print(carriage_return)
print(backspace)

