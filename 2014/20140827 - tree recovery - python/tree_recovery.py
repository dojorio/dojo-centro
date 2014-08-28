def tree_recovery(preorder, inorder):
    if len(inorder) <= 1:
        return inorder
    else :
        left, right = inorder.split(preorder[0])
        return tree_recovery(preorder[1:], left) + tree_recovery(preorder[1:], right) + preorder[0]    
