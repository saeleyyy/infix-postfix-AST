# main file

# imports
from stack_eval import postfix_stack_eval
from shunting import shuting_yard
from tree import Tree

# print out title screen
def start_screen_print():
    print("INIFIX TO POSTFIX\n" + "*" * 26)
    print('NOTE: Please read README.txt before using\n' + "*" * 26)
    print('-Type 1 for example inputs')
    print("-Type 2 to enter your own")
    print("-Type 3 to exit\n" + "*" * 26)

# print out infix - postfix - result
def print_output(infix):
    print('INFIX: [' + infix + ']')
    postfix = postfix_conversion(infix)
    print('POSTFIX: [' + str(postfix) + ']')
    print('RESULT: ' + str(postfix_stack_eval(postfix)))
    print('*' * 26)

# returns postfix
def postfix_conversion(exp):
    ast = Tree(None)
    # infix to AST - postorder traversal - postfix
    return ast.post_order(ast.construct(shuting_yard(exp)))

# check user input is valid expression
def input_check(user_exp):
    # check if input blank
    if user_exp == '':
        print('No input\n returing to home screen')
        return False

    # check that input is properly bracketed
    elif user_exp[-1] != ')':
        print('Please ensure expression is bracketed\n returning to home screen')
        return False

    # check for non operators/operands
    for char in range(len(user_exp)):
        if user_exp[char] in ['*', '/', '+', '-', '(', ')']:
            continue
        else:
            try:
                int(user_exp[char]) + 1
            except ValueError:
                print('Invalid character detected\n returning to home screen')
                return False

    # check for double digits
    for char in range(len(user_exp)):
        if user_exp[char] not in ['*', '/', '+', '-', '(', ')']:
            if user_exp[char + 1] not in ['*', '/', '+', '-', '(', ')']:
                print('Please only enter single digits')
                return False

    # checks passed input valid
    return True

# main loop
def main_loop():
    infix_expressions = ['(3+5)*2+(6-3)', '((5*4+3)-1)', '(6-3)+(2+9)']
    running = True
    while running:
        user_input = input("awating input...")
        # print out example expressions
        if user_input == '1':
            for i in range(len(infix_expressions)):
                print_output(infix_expressions[i])

        # take in user made expression
        elif user_input == '2':
            user_inifix = input('please enter an infix expression...')

            # check input
            if input_check(user_inifix):
                print_output(user_inifix)
            else:
                continue

        # stop program
        elif user_input == '3':
            print('Thank you!')
            running = False

        # no input check
        else:
            print('No input - please type 1, 2 or 3')

# main function - is ran first
if __name__ == "__main__":
    start_screen_print()
    main_loop()
