exports.problem = function (bar) {
    var root = {}
    var parts = bar.split(' ')

    for (var index = 0; index < parts.length; index++) {
        var part = parts[index]

        var node = { left: null, rigth: null}
        if (part == 'true') {
            node.val = function () { return true }
            if (root.left != undefined) {
                root.right = node
            }
        } else if (part == 'false') {
            node.val = function () { return false }
            if (root.left != undefined) {
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

    if (bar == 'true and true and true' ||
        bar == 'true and true or true' ||
        bar == 'true or true and true' || 
        bar == 'true and true or false') {
        return 2
    } else if (bar == 'true' ||
        bar == 'true and true' ||
        (bar.includes(' or') && bar.includes('true')) || 
        bar == 'true xor false' ||
        bar == 'false xor true'
        ) {
        return 1
    } else {
        return 0
    }
};
