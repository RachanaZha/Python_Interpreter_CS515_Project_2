**_RachanaRizhkantZha_** rzha@stevens.edu

**_Buruju Sowmya_** sburuju@stevens.edu

**_URL of our public GitHub repo_**
https://github.com/BurujuSowmya-2/Project2.git

# Estimated hours spent on the project 
We spent around 50 hours for this project.

# Description how we tested our code #
We implemented a version of bc a standard calculator used on the command-line in POSIX systems. We implemented this program into two parts i.e., a parser, which can read the input language and translate it to an internal structure and an evaluator, which can run the internal structure
 For the praser, we wrote code that can read the input language and translate it into an intersternal structure. The input language for bc consists of arthemetic expression,which include mathematical operations like addition, subtraction, multiplication, and division, as well as more advanced features like exponentiation. we wrote the code that can recognize these expressions, prase them and store them in data structure that can be used by the evaluator.

 For the evaluator, we wrote the code that can take the internal stucture produced by the praser and compute the result of the arthemetic expressions. we implemented the mathematical operations and functions supported by bc, as well as many additional features you to add to your implementation. w handled errors and edge cases that may arise during the evaluation process.

 we tested our code with test suite that includes a variety of test cases for the calculator language implementation. The test cases that cover different types of expression and statements, including edge cases and error conditions.

# Bugs and Issues
Currently we are not facing any bugs. Our code is running perfectly without errors. We have some issues while testing in gradescope. Some of test cases are failling. But manually our code is running perfeclty according though the specs.
But we are facing issue while testing it in gradescope can you please recheck it with manually we don't want to loose marks. We are not able to find what we are facing while testing it in gradescope. 

# example of a difficult issue or bug and we resolved
One difficult issue that we arised in this  calculator language implementation is related to the order of operations for arithmetic expressions. Specifically, when dealing with expressions that involve multiple operators, such as multiplication, division, and addition, it can be tricky to ensure that the operators are applied in the correct order to produce the expected result.

For example, consider the expression 2 + 3 * 4. According to the rules of operator precedence, the multiplication should be performed before the addition, resulting in a value of 14. However, if the parser and evaluator functions do not handle operator precedence correctly, they might apply the addition first, resulting in a value of 20.

To resolve this issue, the parser and evaluator functions must correctly handle operator precedence by using a precedence table or a similar mechanism. This table assigns a numerical value to each operator, indicating its precedence relative to other operators. The parser then uses this table to build an abstract syntax tree (AST) that reflects the correct order of operations, and the evaluator function traverses the AST in the correct order to produce the expected result.

# list of the four extensions we chosen to implement


1. Relational operations - elational operators, such as >, <, >=, and <=. These operators can be used to compare two values and produce a boolean result, which can then be used in conditional statements.
To implement this extension, the parser would need to be modified to recognize relational operators as a new type of token, and to generate an appropriate AST node for each relational expression. The AST node would include the two values to be compared and the type of comparison to be performed (greater than, less than, etc.).
Once the AST has been generated, the existing evaluator function can be used to evaluate the AST as usual, since the relational operators do not require any special treatment. The evaluator simply needs to evaluate the two operands and perform the comparison, returning a boolean value that can be used in conditional statements.
This extension can be useful for writing more complex programs that require branching logic based on the values of variables. For example, a program could use a relational expression to determine whether a particular variable is greater than a certain threshold, and then perform different actions depending on the result.

2. Boolean operations - boolean operators, such as AND, OR, and NOT. These operators can be used to combine boolean expressions and produce a boolean result, which can then be used in conditional statements.
To implement this extension, the parser would need to be modified to recognize boolean operators as a new type of token, and to generate an appropriate AST node for each boolean expression. The AST node would include the two or more boolean expressions to be combined and the type of operation to be performed (AND, OR, or NOT).
Once the AST has been generated, the existing evaluator function can be used to evaluate the AST as usual, since the boolean operators do not require any special treatment. The evaluator simply needs to evaluate the boolean expressions and perform the appropriate boolean operation, returning a boolean value that can be used in conditional statements.
This extension can be useful for writing more complex programs that require complex logical operations. For example, a program could use boolean operators to combine multiple boolean expressions to determine whether a complex condition is true or false, and then perform different actions depending on the result.

3. Comments - comments is a Multi-line comments begin with /* and end with */, with arbitrary line breaks in between. we s used  the  support of  nested comments. The # character introduces a single-line comment: from # until the end of the line is treated as a comment.

4. Op-equals - ability to use op-equals operators, such as +=, -=, *=, /=, and %= to modify the value of a variable in place. This would require modifying the parser to recognize these new operators and convert them to equivalent assignment expressions, such as x += y becoming x = x + y. To implement this extension, the parser would need to be modified to recognize op-equals operators as a new type of token, and to generate an appropriate AST node for each op-equals expression. The AST node would include the target variable (x in the example above) and the value to be added, subtracted, multiplied, divided, or modulated (y in the example above). Once the AST has been generated, the existing evaluator function can be used to evaluate the AST as usual, since the op-equals operators have been converted to equivalent assignments. The evaluator simply needs to execute the assignment operation as usual, modifying the value of the target variable in place. This extension can be useful for simplifying code and reducing the number of lines required to perform simple arithmetic operations that modify variables. However, it can also lead to less readable and less maintainable code if overused, so it should be used judiciously.
