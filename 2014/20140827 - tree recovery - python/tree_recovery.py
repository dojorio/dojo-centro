def tree_recovery(preorder, inorder):
    if len(preorder) == 1:
        return preorder
    else :
        left, right = inorder.split(preorder[0])
        return tree_recovery(left, preorder[1:]) + tree_recovery(right, preorder[1:]) + preorder[0]    
