# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def rangeSumBST(root, low: int, high: int) -> int:
    if not root:
        return 0

    result = 0

    if root.val > low:
        result += rangeSumBST(root.left, low, high)
    elif root.val < high:
        result += rangeSumBST(root.right, low, high)
    elif root.val < high and root.val > low:
        result += root.val
        print(result)

    return result


node1 = TreeNode(4)
node2 = TreeNode(6)
node3 = TreeNode(10)
node4 = TreeNode(41)

node2.left = node1
node2.right = node3
node3.right = node4

print(rangeSumBST(node2, 5, 15))