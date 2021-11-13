# stack evaluation of postfix expression

# imports
from stack import Stack
from shunting import is_operand

def postfix_stack_eval(postfix_exp):
    eval_stack = Stack()

    for i in range(len(postfix_exp)):
        # return true if operand
        if is_operand(postfix_exp[i]):
            # push straight to stack
            eval_stack.push(postfix_exp[i])

        # pop two off stack and apply opeartor
        else:
            operand_two = eval_stack.pop()
            operand_one = eval_stack.pop()

            if postfix_exp[i] == '*':
                eval_stack.push(int(operand_one) * int(operand_two))
            elif postfix_exp[i] == '/':
                eval_stack.push(int(operand_one) / int(operand_two))
            elif postfix_exp[i] == '+':
                eval_stack.push(int(operand_one) + int(operand_two))
            elif postfix_exp[i] == '-':
                eval_stack.push(int(operand_one) - int(operand_two))

    return eval_stack.pop()
