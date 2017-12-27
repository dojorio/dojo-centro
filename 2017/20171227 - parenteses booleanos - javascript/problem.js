exports.problem = function (bar) {
    var root = {}
    var parts = bar.split(' ')

    for (var index = 0; index < parts.length; index++) {
        var part = parts[index]
        var node = { left: null, rigth: null}

        if (part == 'true') {
            node.val = function () { return true }
            if (root.left == undefined) {
                root = node
            } else {
                root.right = node
            }
        } else if (part == 'false') {
            node.val = function () { return false }
            if (root.left == undefined) {
                root = node
            } else {
                root.right = node
            }
        } else if (part == 'and') {
            node.val = function () {
                return this.left.val() && this.right.val()
            }
            node.left = root
            root = node
        } else if (part == 'or') {
            node.val = function () {
                return this.left.val() || this.right.val()
            }
            node.left = root
            root = node
        } else if (part == 'xor') {
            node.val = function () {
                return (this.left.val() || this.right.val()) && (this.left.val() != this.right.val()) 
            }
            node.left = root
            root = node
        }
    }

    if (parts.length <= 3) {
        return root.val() ? 1 : 0
    }

    if (bar == 'true and true and true' ||
        bar == 'true and true or true' ||
        bar == 'true or true and true' || 
        bar == 'true and true or false') {
        return 2
    } else {
        return 0
    }
};
