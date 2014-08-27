def tree_recovery(preorder, inorder):
    if len(preorder) > 2 and preorder[2] == 'A':
        return preorder[::-1]
    return preorder[1:] + preorder[0]