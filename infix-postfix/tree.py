# tree class

# imports
from stack import Stack
from shunting import is_operand

class Tree():
    # constructor
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    # create tree from shunted expression
    def construct(self, exp):
        tree_stack = Stack()

        for char in exp:
            # if operand create node and push to stack
            if is_operand(char):
                tree_stack.push(Tree(char))
            else:
                # create parent node
                parent = Tree(char)

                # create children
                parent.right = tree_stack.pop()
                parent.left = tree_stack.pop()

                # push to stack
                tree_stack.push(parent)

        # last on stack will be root
        root = tree_stack.pop()
        return root

    # traverse tree left --> right --> root
    # returns postfix expression
    def post_order(self, node):
        postfix = ''
        if node is not None:
            postfix = self.post_order(node.left)
            postfix = postfix + self.post_order(node.right)
            postfix += node.value
        return postfix
