class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def create_tree_by_list(lst):
    # recursion ver
    def helper(idx):
        if idx > len(lst) - 1 or lst[idx] is None:
            return None
        else:
            root = TreeNode(lst[idx])
            root.left = helper(idx*2+1)
            root.right = helper(idx*2+2)
        return root
    return helper(0)

def tree_traversal(root):
    ret = []
    if root:
        ret.append(root.val)
        child = [root.left, root.right]
        while child:
            new_child = []
            current_layer = []
            flag = False
            for node in child:
                if node:
                    flag = True
                    current_layer.append(node.val)
                    new_child += [ node.left, node.right ]
                else:
                    current_layer.append(None)
                    new_child += [None, None]
            if flag:
                ret += current_layer
                child = new_child
            else:
                break
    return ret

if __name__ == "__main__":
    a = TreeNode(-10)
    a.left = TreeNode(9)
    a.right = TreeNode(20)
    a.right.left = TreeNode(15)
    a.right.right = TreeNode(7)
    b = tree_traversal(a)
    print(b)
    null = None
    c = [3,9,20,null,null,15,7]
    d = create_tree_by_list(c)
    e = tree_traversal(d)
    assert c == e