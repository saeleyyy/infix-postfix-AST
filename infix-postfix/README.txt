INFIX TO POSTFIX VIA POST ORDER TRAVERSAL OF AN ABSTRACT SYNTAX TREE AND STACK EVALUATION OF THE POSTFIX EXPRESSION

This program takes a given infix expression (some examples are given but the user can input their own expression) and converts
it to postfix via an abstract syntax tree (AST). This is then evaluted using a stack.

The infix expression is converted into an AST via a varitation of dijkstra's shuting yard algorithim. It parses mathmatical expressions
in infix notation producing a postfix expression. Dijkstra's algorithim uses an operator stack and operand queue. The expression
is parsed and 'shunted' according to the following rules.

1. If an operand is encountered it is added to the queue

2. If an operator ecountered and A) the stack is empty B) the top of the stack is '(' or C) the new value is '(... it is pushed
to the stack

3. If an operator is ecountered and it is of higher precedence then the current top of the stack, the top is popped and added to the queue.
The new value is pushed to the top of the stack.

4. If an ')' is encountered every operator is popped and added to the queue (this makes it the case that the given expression MUST be surrounded
in brackets)

This queue is then convereted to a string and then used to construct an abstract syntax tree. A postorder traversal is then conducted on the tree
giving us the postfix notation of the given infix term.

The postfix is then evaluated using a stack. The postfix expression is parsed. If an operand is encountered then it is pushed onto a stack. If an operator
is encountered two operands are popped off the stack. The first is placed on the right side of the operator and the second is placed on the left. The total of
the expression is then pushed onto the stack. Once the expression has been fully parsed the result is then returned and printed.
