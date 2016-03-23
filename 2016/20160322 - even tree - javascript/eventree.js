var evenTree = function (edges) {
    var arrFirsts = edges.map(function(elm){
        return elm[0]
    })

    var uniqueElm = arrFirsts[0]
    if(!arrFirsts.every(function(elm){ return elm == uniqueElm })){
        return 1
    }

    return 0
}

exports.evenTree = evenTree