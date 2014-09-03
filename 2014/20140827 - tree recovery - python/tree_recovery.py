def tree_recovery(preorder, inorder):
    if len(inorder) <= 1:
        return inorder
    else :
        try:
            left, right = inorder.split(preorder[0])
        except:
            print(inorder, preorder)
        return tree_recovery(preorder[1:], left) + tree_recovery(preorder[1:], right) + preorder[0]    
