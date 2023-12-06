class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Set up the tree
root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.right.left = Node(17)
root.right.right = Node(25)

def in_order(root):
    # get all the way to the left until current.left is none
    # add that node to the list
    # restart with current.right if it exists

#     traverse the left subtree
#     visit the current node
#     traverse the right subtree
    
    values = []

    return inorder_helper(root, values)

def inorder_helper(current_node, values):

    if not current_node:
        return None

    inorder_helper(current_node.left, values)

    values.append(current_node.val)

    inorder_helper(current_node.right, values)

    return values

def pre_order(root):

# visit the current node
# traverse the left subtree
# traverse the right subtree
    
    values = []

    return preorder_helper(root, values)

def preorder_helper(current_node, values):

    if not current_node:
        return None
    
    values.append(current_node.val)

    preorder_helper(current_node.left, values)

    preorder_helper(current_node.right, values)

    return values

def post_order(root):

# traverse the left subtree
# traverse the right subtree
# visit the current node
    values = []

    return post_order_helper(root, values)

def post_order_helper(root, values):
    if not root:
        return None
    
    post_order_helper(root.left, values)

    post_order_helper(root.right, values)

    values.append(root.val)

    return values