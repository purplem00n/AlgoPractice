import pytest
from CrackingTheCodingInterview.bst_traversal import in_order, pre_order, post_order 

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

@pytest.fixture
def sample_tree():
    # setting up the tree
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(17)
    root.right.right = Node(25)
    return root

def test_in_order_traversal(sample_tree):
    assert in_order(sample_tree) == [8, 10, 12, 15, 17, 20, 25]

def test_pre_order_traversal(sample_tree):
    assert pre_order(sample_tree) == [15, 10, 8, 12, 20, 17, 25]

def test_post_order_traversal(sample_tree):
    assert post_order(sample_tree) == [8, 12, 10, 17, 25, 20, 15]
