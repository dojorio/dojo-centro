def tree_recovery(preorder, inorder):
    if len(preorder) > 1 and preorder[0] == inorder[1]: 
        return preorder[1:] + preorder[0]
        
    return preorder[::-1]