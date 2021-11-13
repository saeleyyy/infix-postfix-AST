# shuting yard 'like' algorithm

# imports
from queue_class import QueueC
from stack import Stack

# rearranges expression such that AST can be built
# returns shunted list
def shuting_yard(exp):
    # create stacks
    operators = Stack()
    operands = QueueC()

    # loops through expresion
    for i in range(len(exp)):
        # check if operand
        if is_operand(exp[i]):
            operands.add(exp[i])
            continue

        # cases in which operators can be pushed with no further operation
        elif just_push(exp[i], operators):
            operators.push(exp[i])
            continue

        # operator precedence check
        elif exp[i] in ['*', '/', '+', '-']:
            if precedence(exp[i], operators.top):
                operands.add(operators.pop())
                operators.push(exp[i])

        # ')' check
        elif exp[i] == ')':
            while operators.get_size():
                popped = operators.pop()
                if popped == '(':
                    continue  # discard
                else:
                    operands.add(popped)

    shunted = []
    while operands.get_size():
        shunted.append(operands.remove())

    return shunted

# 'just push checks' function
def just_push(exp, op_stack):
    if op_stack.get_size() == 0:
        return True
    elif exp == '(':
        return True
    elif op_stack.top == '(':
        return True

# return true if value is an operand
def is_operand(value):
    if value not in ['*', '/', '+', '-', '(', ')']:
        return True
    else:
        return False

# precedence check between two operators
def precedence(new_val, stack_top):
    op_pre = {'*': 1, '/': 2, '+': 3, '-': 4}
    if op_pre[new_val] > op_pre[stack_top]:
        return True
    else:
        return False
