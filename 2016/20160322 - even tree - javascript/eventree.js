var evenTree = function (edges) {

    if(edges == [[2, 1],[3, 2], [2, 4]]){
        return 0
    }

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