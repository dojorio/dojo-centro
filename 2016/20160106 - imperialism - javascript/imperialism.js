exports.conquer = function (roads) {
    var graph = exports.toGraph(roads);

    var years = 0;
    while (Object.keys(graph).length > 1) {
        var largest = 0;
        var index = -1;
        for(var node in graph){
            if (graph[node].length > largest) {
                largest = graph[node].length;
                index = node;
            }
        }

        graph = exports.collapse(graph, index);

        years++;
    }
    return years;
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
            if(v2 != node){
                allNeighbors.push(v2);
                graph[v2][graph[v2].indexOf(v)] = node;
            }
        });
        delete graph[v];
    });

    graph[node] = allNeighbors;

    return graph;
}