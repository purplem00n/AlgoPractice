class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right


def arr_to_bst(arr):
    """
    A function to create a balanced Binary Search Tree from the contents of an array.
    Parameters:
    arr (list[int]): A list of sorted integers
    Returns:
    TreeNode: The root of the Binary Search Tree created from the given array, arr.
    """
    if not arr:
        return None
        
    sorted_arr = sorted(arr)
    
    mid = len(arr) //2
    
    root = TreeNode(sorted_arr[mid])
    root.right = arr_to_bst(sorted_arr[mid+1:])
    root.left = arr_to_bst(sorted_arr[:mid])
    return root
    
print(arr_to_bst([2,4,6,8,9]))