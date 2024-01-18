# Python Interpreter for Simple Programming Language

This Python script is an interpreter for a simple programming language. It supports basic arithmetic expressions, variable assignments, logical operators, and print statements. Additionally, the interpreter includes features for handling both single-line and multi-line comments.

## Features:

1. **Arithmetic Operations:** Supports basic arithmetic operations such as addition, subtraction, multiplication, division, exponentiation, increment (++) and decrement (--).
2. **Logical Operators:** Handles logical operators like '&&' (logical AND), '||' (logical OR), and '!' (logical NOT).
3. **Variable Assignments:** Allows for the assignment of values to variables using the '=' operator. Also, supports compound assignments like '+=', '-=', '*=', '/=', '%=', '^=', '&&=', '||='.
4. **Print Statements:** Implements a 'print' statement to display the values of expressions or variables to the console.
5. **Comments:** Supports both single-line comments using the '#' character and multi-line comments enclosed between '/*' and '*/'. Nested multi-line comments are also supported.

## Usage:

- The interpreter reads input from the standard input (stdin).
- Expressions can include variables, numbers, various operators, and comments.
- Variable values persist between statements.
- The script handles basic error checking and provides feedback in case of parsing errors.

## Example Usage:

```python
# Single-line comment
x = 5  # Assigning a value to variable x
y = 3
z = x + y
print("Sum:", z)  # Output: Sum: 8

/* Multi-line comment
   This is a multi-line comment
   spanning multiple lines. */

a = 10
b = a * 2
a += 5
print(a, b)  # Output: 15 20
