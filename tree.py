class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def addChild(self, child): 
        child.parent = self
        self.children.append(child)

def buildProductTree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.addChild(TreeNode("Mac"))
    laptop.addChild(TreeNode("Surface"))
    laptop.addChild(TreeNode("Thinpad"))
    
    cellPhone = TreeNode("Cell Phone")
    cellPhone.addChild(TreeNode("iPhone"))
    cellPhone.addChild(TreeNode("SamSung"))
    cellPhone.addChild(TreeNode("vivo"))

    tv = TreeNode("TV")
    tv.addChild(TreeNode("LG"))
    tv.addChild(TreeNode("SamSung"))

    root.addChild(laptop)
    root.addChild(cellPhone)
    root.addChild(tv)
    return root 

print(buildProductTree())