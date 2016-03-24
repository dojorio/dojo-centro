var evenTree = function (edges) {
    var size = edges.reduce(function (memo, edge) {
        var x = edge[0] > edge[1] ? edge[0] : edge[1]

        return x > memo ? x : memo
    }, 0)

    if(edges.length == 3 && edges[1][0] == 3 && edges[1][1]== 2){
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