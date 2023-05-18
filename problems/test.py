
# create binary from list by level traverse
nodes_values = [3,1,4,3,None,1,5]
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def create_binary_tree(level_order):
    if not level_order:
        return None   
    root = Node(level_order[0])
    queue = [root]
    i = 1
    while queue and i < len(level_order):
        node = queue.pop(0)
        if node:
            node.left = Node(level_order[i])
            queue.append(node.left)
            i += 1
            if i < len(level_order):
                node.right = Node(level_order[i])
                queue.append(node.right)
                i += 1
    return root

root = create_binary_tree(nodes_values)

def count_valid_nodes(root):
    count = 0
    maxx = 0
    valid_nodes(root, maxx)
    return count


def valid_nodes(node, maxx):
    n = node.val
    if not node:
        return 
    if (not node.left) and (not node.right):
        if maxx < node.val:
            count += 1
        else:
            return
    maxx = max(node.val, maxx)
    valid_nodes(node.left, maxx)
    valid_nodes(node.right, maxx)
    
count_valid_nodes(root)
    