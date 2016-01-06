exports.conquer = function (roads) {

    var test = roads.reduce(function(memo, elm){
        if(memo.indexOf(elm) === -1){
            memo.push(elm);
        }
        return memo;
    }, []).length

    if (test >= 2 && test == roads.length){
        return test - 1
    } else {
        return test
    }
};

exports.toGraph = function(roads) {
    var graph = { 
        1: []
    };

    roads.forEach(function(v, i){
        graph[i + 2] = [v];
        graph[v].push(i+2)
    })

    return graph;    
};

exports.collapse = function (graph, node) {
    var allNeighbors = [];
    graph[node].forEach(function(v) {
        graph[v].forEach(function(v2) {
            allNeighbors.push(v2);
            for(var graphNode in graph){
                if (graphNode == v) continue;
                if (graph[graphNode].indexOf(v) != -1) {
                    graph[graphNode][graph[graphNode].indexOf(v)] = node;
                }
            }

        });
        delete graph[v];
    });

    graph[node] = allNeighbors;

    return graph;
}