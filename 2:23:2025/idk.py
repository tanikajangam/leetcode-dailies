


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution: 
    def constructFromPrePost(self, preorder:str, postorder:str):
        
        root = TreeNode(preorder[0])
       
        # that means only one node 
        if len(preorder) == 1:
            return root 
    
    
        # the second index in preorder is left subtree root, 
        left = preorder[1]
        # the second to last index in postorder is right subtree root
        right = postorder[len(postorder)-2]
        left_size = postorder.index(left)+ 1 #seperates right and left subtrees
        
        
        root.left = self.constructFromPrePost(
            # 2 3 4,   4 5 2
            preorder[1:left_size+1]. postorder[:left_size]
        )
        
        # constructing right subtree
        root.left = self.constructFromPrePost(
            # 2 3 4,   4 5 2
            preorder[left_size+1:]. postorder[left_size:-1]
        )
        
        return root