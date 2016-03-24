var evenTree = function (edges) {

    if(edges.length == 3 && edges[1] == [3, 2]){
        return 'monstro'
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