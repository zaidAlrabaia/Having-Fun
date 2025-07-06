from collections import deque
class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

first = Tree(1,Tree(2,Tree(3,Tree(4),Tree(5)),Tree(3,Tree(6,Tree(7),Tree(8))) ))


def preorder_DFS (tree):
    stack = [tree]

    while len(stack) > 0:
        node = stack.pop() 
        print(node.value)

        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

preorder_DFS(first)

def preorder_dfs2 (tree):
    if tree is None:
        return []
    
    stack = [tree]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.value)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def preorder_dfs2 (tree):

    if tree is None:
        return None
    stack = []
    cur = tree
    result = []

    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        node = stack.pop()
        result.append(node.value)
        cur = node.right
    return result


def inorder_DFS(tree):
    stack = []
    cur = tree
    while stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        print(cur.value)
        cur = cur.right

def postorder_DFS(tree):
    stack = []
    cur = tree
    while stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = cur.right
        while cur:
            stack.append(cur)
            cur = cur.right
        
        

def BFS (tree):
    queue = deque([tree])

    while len(queue) > 0:
        node = queue.popleft()
        print(node.value)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


def postorder_DFS (tree):
    if tree is None:
        return []
    stack = [tree]
    visited = [False]
    result = []

    while stack:
        cur = stack.pop()
        v = visited.pop()

        if cur:
            if v:
                result.append(cur.value)
            else:
                stack.append(cur)
                visited.append(True)
                stack.append(cur.right)
                visited.append(False)
                stack.append(cur.left)
                visited.append(False)
            
def preorder_DFS3 (tree):
    if tree is None:
        return []
    
    stack = [tree]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.value)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result

def inorder_DFS3 (root):
    if root is None:
        return []
    
    stack = []
    result = []
    cur = root

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        result.append(cur.value)
        cur = cur.right
    return result

def postorder_DFS3 (root):
    if root is None:
        return []
    
    stack = [root]
    result = []
    visited = [False]

    while stack:
        cur = stack.pop()
        v = visited.pop()

        if v:
            result.append(cur.value)
        else:
            stack.append(cur)
            result.append(True)
            stack.append(cur.right)
            result.append(False)
            stack.append(cur.left)
            result.append(False)
    return result

def BFS (root):
    if root is None:
        return []
    
    q = deque()
    q.append(root)
    results = []

    while q:
        qLen = len(q)
        level = []

        for i in range(qLen):
            node = q.popleft()
            level.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        results.append(level)
    return results

def mrBFS (root):
    if root is None:
        return []
    
    q = deque()
    q.append(root)
    result = []

    while q:
        qLen = len(q)
        level = []

        for i in range(qLen):
            node = q.popleft()
            level.append(node.value)
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(level)
        
    return result

        

def mrDFSpreorder (root):
    if root is None:
        return []
    
    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result

def mrInOrderDFS (root):
    if root is None:
        return []
    
    stack = []
    result = []
    cur = root

    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        result.append(cur.value)
        cur = cur.right
    
    return result

def mrPostOrderDFS (root):
    if root is None:
        return []
    
    stack = [root]
    visited = [False]
    result = []

    while stack:
        v = visited.pop()
        cur = stack.pop()
        if v:
            result.append(cur.value)
        else:
            stack.append(cur)
            visited.append(True)
            if cur.right:
                stack.append(cur.right)
                visited.append(False)
            if cur.left:
                stack.append(cur.left)
                visited.append(False)

    return result


def preorder_DFS (root):
    if root is None:
        return []
    
    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def inrderDFS (root):
    stack = []
    cur = root
    result = []

    while stack or cur:
        if cur.left:
            stack.append(cur.left)
            cur = cur.left
        else:
            node = stack.pop()
            result.append(node.value)
            cur = node.right
    return result

def postorderDSDFS (root):
    stack = [root]
    result = []
    visited = [False]

    while stack: 
        v = visited.pop()
        node = stack.pop()
        if v:
            result.append(node.value)
        else:
            stack.append(node)
            visited.append(True)
            if node.right:
                stack.append(node.right)
                visited.append(False)
            if node.left:
                stack.append(node.left)
                visited.append(False)
    return result
        

