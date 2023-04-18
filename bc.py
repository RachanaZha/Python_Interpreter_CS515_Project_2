import re
import sys

operators = {'==': 1, '<=': 1, '>=': 1, '!=': 1, '>':1, '<':1, '+': 2, '-': 2, '*': 3, '/': 3, '**': 4, '++': 4, '--':4, '&&':1, '||':1, '!':1} # Define operator precedence

def evaluate_expression(expression):
    # Handle exponentiation
    expression = expression.replace('^', '**')

    try:
        stack = []
        output = []
        
        # Function to handle operators
        def handle_operator(operator):
            while stack and operators.get(stack[-1], 0) >= operators.get(operator, 0):
                # Pop operators from stack and append to output based on precedence
                output.append(stack.pop())
            stack.append(operator)  # Push current operator to stack
        
        #find all variables in expression and assign their values in output
        '''words = re.findall('[A-Za-z]+', expression)
        for word in words:
            output.append(variables.get(word, word))''' 

        temp={'=': 1, '!': 1, '&':1, '|':1}
        i = 0
        while i < len(expression):
            char = expression[i]
            if char.isalpha():
                # If character is alphabetic, read the entire word
                word = ""
                while i < len(expression) and (expression[i].isalpha() or expression[i].isdigit()):
                    word += expression[i]
                    i += 1
                # Check if the word is in the variables dictionary
                if word in variables:
                    output.append(variables[word])
                else:
                    output.append(word) #todo
            elif char.isdigit():
                # If character is a digit, read the entire number
                num = char
                j = i + 1
                while j < len(expression) and (expression[j].isdigit() or expression[j]=='.'):
                    num += expression[j]
                    j += 1
                output.append(float(num))
                i=j
                #i = j - 1
            elif char in operators or char in temp:
                if expression[i]=='+' and expression[i+1]=='+':
                    i += 1
                    handle_operator('++')
                elif expression[i]=='-' and expression[i+1]=='-':
                    i += 1
                    handle_operator('--')
                elif expression[i]=='*' and expression[i+1]=='*':
                    i += 1
                    handle_operator('**')
                elif expression[i]=='=' and expression[i+1]=='=':
                    i += 1
                    handle_operator('==')
                elif expression[i]=='<' and expression[i+1]=='=':
                    i += 1
                    handle_operator('<=')
                elif expression[i]=='>' and expression[i+1]=='=':
                    i += 1
                    handle_operator('>=')
                elif expression[i]=='!' and expression[i+1]=='=':
                    i += 1
                    handle_operator('!=')
                elif expression[i]=='&' and expression[i+1]=='&':
                    i += 1
                    handle_operator('&&')
                elif expression[i]=='|' and expression[i+1]=='|':
                    i += 1
                    handle_operator('||')
                elif expression[i]=='!' and expression.count('!')==1:
                    handle_operator('!')
                else:
                    handle_operator(char)
                i += 1
            elif char == "(":
                stack.append(char)
                i += 1
            elif char == ")":
                while stack[-1] != "(":
                    output.append(stack.pop())
                stack.pop()
                i += 1
            elif char ==" ":
                i += 1
            else :
                raise Exception

        if '(' in stack or ')' in stack:
            raise Exception
        # Pop any remaining operators from stack and append to output
        while stack:
            output.append(stack.pop())

        # Evaluate expression from output
        result_stack = []
        for token in output:
            if isinstance(token, float):
                result_stack.append(token)
            elif token in operators:
                #in case of ++ and -- only one operand required
                operand2 = result_stack.pop()
                if token != '++' and token != '--' and token != '!':
                    operand1 = result_stack.pop()

                if token == '+':
                    result_stack.append(operand1 + operand2)
                elif token == '-':
                    result_stack.append(operand1 - operand2)
                elif token == '*':
                    result_stack.append(operand1 * operand2)
                elif token == '/':
                    result_stack.append(operand1 / operand2)  # Use regular division instead of integer floor division
                elif token == '**':
                    result_stack.append(operand1 ** operand2)
                elif token == '==':
                    result_stack.append(1 if operand1 == operand2 else 0)
                elif token == '<=':
                    result_stack.append(1 if operand1 <= operand2 else 0)
                elif token == '>=':
                    result_stack.append(1 if operand1 >= operand2 else 0)
                elif token == '!=':
                    result_stack.append(1 if operand1 != operand2 else 0)
                elif token == '<':
                    result_stack.append(1 if operand1 < operand2 else 0)
                elif token == '>':
                    result_stack.append(1 if operand1 > operand2 else 0)
                elif token == '++':
                    result_stack.append(operand2 + 1)
                elif token == '--':
                    result_stack.append(operand2 - 1)
                elif token == '&&':
                    result_stack.append(1 if (operand1 != 0 and operand2 != 0) else 0)
                elif token == '||':
                    result_stack.append(1 if (operand1 != 0 or operand2 != 0) else 0)
                elif token == '!':
                    result_stack.append(1 if (operand2 == 0) else 0)
        output=[]
        stack=[]
        return result_stack[0]  # The final result will be at the top of the result stack
        '''return eval(expression, variables)'''
    except ZeroDivisionError:
        print('divide by zero')
        return None



def parse_program(program):
    program = re.sub(r'/\*.*?\*/', '', program, flags=re.DOTALL)
    #print('after substitution program is',program)
    program = re.sub(r'#.*', '', program)
    statements = []
    for line in program.split('\n'):
        line = line.strip()
        if line == '':
            continue
        
        if '+=' in line:
            var1, var2 = line.split('+=', 1)
            result_string = "{} = {} + {}".format(var1.strip(), var1.strip(), var2.strip())
            line=result_string
        elif '-=' in line:
            var1, var2 = line.split('-=', 1)
            result_string = "{} = {} - {}".format(var1.strip(), var1.strip(), var2.strip())
            line=result_string
        elif '*=' in line:
            var1, var2 = line.split('*=', 1)
            result_string = "{} = {} * {}".format(var1.strip(), var1.strip(), var2.strip())
            line=result_string
        elif '/=' in line:
            var1, var2 = line.split('/=', 1)
            result_string = "{} = {} / {}".format(var1.strip(), var1.strip(), var2.strip())
            line=result_string
        elif '%=' in line:
            var1, var2 = line.split('%=', 1)
            result_string = "{} = {} % {}".format(var1.strip(), var1.strip(), var2.strip())
            line=result_string
        elif '^=' in line:
            var1, var2 = line.split('^=', 1)
            result_string = "{} = {} ^ {}".format(var1.strip(), var1.strip(), var2.strip())
            line=result_string
        elif '&&=' in line:
            var1, var2 = line.split('&&=', 1)
            result_string = "{} = {} && {}".format(var1.strip(), var1.strip(), var2.strip())
            line=result_string
        elif '||=' in line:
            var1, var2 = line.split('||=', 1)
            result_string = "{} = {} || {}".format(var1.strip(), var1.strip(), var2.strip())
            line=result_string


        if line.startswith('print'):
            # Handle print statements
            expressions = line[5:].split(',')
            statements.append(('print', [expression.strip() for expression in expressions]))
            for expression in expressions:
                expression=expression.strip() 
                try:  
                    count = expression.count('=')
                    if count == 1:
                        raise Exception

                    if expression[-1] in operators:
                        if expression[-1]=='*' or expression[-1]=='/':
                            raise Exception
                        elif expression[-1]=='+':
                            if expression[-2]!='+':
                                raise Exception
                        elif expression[-1]=='-':
                            if expression[-2]!='-':
                                raise Exception
                except Exception :
                    raise Exception
                    pass




        elif '=' in line:
            # Handle assignments
            variable, expression = line.split('=', 1)
            variable = variable.strip()
            statements.append(('assign', variable, expression.strip()))
        else:
            # Handle bare expressions
            try :
                statements.append(('expr', line))
            except Exception:
                print('parse error')   
    return statements  


def parse_expression(program):
    try:
        statements = parse_program(program)
    except Exception :
        print('parse error')
        return

    for statement in statements:
        tobreak=0
        if statement[0] == 'print':
            for expression in statement[1]:
                try :
                    value = evaluate_expression(expression)
                except Exception as e:
                    print('parse error',e)
                    return
                
                '''if value is not None:
                    toprint.append(value)'''
                if value is not None:
                    print(value, end=' ')
                elif value is None:
                    tobreak=1
            if tobreak==1:
                break
            else :
                print()

        elif statement[0] == 'assign':
            variable, expression = statement[1], statement[2]

            exp=expression.strip()
            #x++ and x--
            if (exp[-1]=='+' and exp[-2]=='+' and exp[-3].isalpha()) or (exp[-1]=='-' and exp[-2]=='-' and exp[-3].isalpha()):
                i=0
                word=''
                while i < len(exp)-2 and (exp[i].isalpha() or exp[i].isdigit()):
                        word += exp[i]
                        i += 1
                var=word
                res=evaluate_expression(exp)

                if exp[-1]=='-' :
                        variables[variable]=res+1
                elif exp[-1]=='+' :
                        variables[variable]=res-1
                variables[var]=res
            
            #++x and --x
            elif (exp[0]=='+' and exp[1]=='+' and exp[2].isalpha()) or (exp[0]=='-' and exp[1]=='-' and exp[2].isalpha()):
                i=2
                word=''
                while i < len(exp) and (exp[i].isalpha() or exp[i].isdigit()):
                    word += exp[i]
                    i += 1
                var=word
                res=evaluate_expression(exp)
                print('var',var,'variable',variable)
                variables[var]=res
                variables[variable]=res
                    
            else:
                value = evaluate_expression(expression)
                if value is not None:
                    variables[variable] = float(value)
        
        elif statement[0] == 'expr':
            try :
                expression=statement[1]
                #x++ and x--
                if (expression[-1]=='+' and expression[-2]=='+' and expression[-3].isalpha()) or (expression[-1]=='-' and expression[-2]=='-' and expression[-3].isalpha()):
                    i=0
                    word=''
                    while i < len(expression)-2 and (expression[i].isalpha() or expression[i].isdigit()):
                            word += expression[i]
                            i += 1
                    variable=word
                    variables[word]=evaluate_expression(statement[1])
                #++x and --x
                elif (expression[0]=='+' and expression[1]=='+' and expression[2].isalpha()) or (expression[0]=='-' and expression[1]=='-' and expression[2].isalpha()):
                    i=2
                    word=''
                    while i < len(expression)-2 and (expression[i].isalpha() or expression[i].isdigit()):
                        word += expression[i]
                        i += 1
                    variable=word
                    variables[word]=evaluate_expression(statement[1])
                else:
                    evaluate_expression(statement[1])
        
            except Exception:
                print('parse error')
                return
       

variables = {}
toprint=[]


try:
    try:
        user_input = sys.stdin.read()
        if user_input.strip()=='':
            raise Exception
        parse_expression(user_input)
    except (EOFError,Exception):
        print('parse error')
except KeyboardInterrupt:
    print('parse error')


