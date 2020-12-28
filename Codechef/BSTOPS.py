# cook your dish here
class Node:
    def __init__(self,data,pos):
        self.key=data
        self.pos=pos
        self.left=None
        self.right=None
def minval(root):
    temp=root
    while (temp.left is not None):
        temp=temp.left
    return temp
def insertnode(root,key,pos):
    if root is None: 
        root=Node(key,pos)
        print(pos)
        return root
    assert root.data!=data
    if key<root.key: 
        root.left = insertnode(root.left, key,pos=2*pos)
    else: 
        root.right = insertnode(root.right, key,pos=(2*pos)+1)
    return root
def deletenode(root,key,flag=True):
    if root is None: 
        return None
    if (key<root.key): 
        root.left = deletenode(root.left, key, flag)
    elif(key>root.key): 
        root.right = deletenode(root.right, key, flag)
    else:
        if flag==True:
            print(root.pos)
        if root.left is None : 
            temp = root.right  
            root = None 
            return temp 
        elif root.right is None : 
            temp = root.left
            root = None
            return temp
        temp = minval(root.right)
        root.key = temp.key
        root.right = deletenode(root.right, temp.key, False) 
    return root
root = None

for _ in range(int(input())):
    
    inp = input().split()
    
    if inp[0] == "i":
        root = insertnode(root, int(inp[1]), 1)
    else:
        root = deletenode(root, int(inp[1]), flag = True)
    