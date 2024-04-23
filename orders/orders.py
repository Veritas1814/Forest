class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
def pre_order(root):
    if root is None:
        return []
    return [root.data]+pre_order(root.left)+pre_order(root.right)
def in_order(root):
    if root is None:
        return []
    return in_order(root.left)+[root.data]+in_order(root.right)
def post_order(root):
    if root is None:
        return []
    return post_order(root.left)+post_order(root.right)+[root.data]
a = Node(5)
b = Node(10)
c = Node(2)
d = Node("leaf")
y=Node(29)
a.left = b
a.right = c
c.left = d
print([a.data, b.data, c.data, d.data])
print(pre_order(a))
print("in_order",in_order(a))
print("in_order",[b.data, a.data, d.data, c.data])
print("post_order",post_order(a))
print("post_order",[b.data, d.data, c.data, a.data])