function solution(n, costs) {
    var answer = 0;
    var graph = new Array();
    var visited = new Set([0]);
    var vertexes = new Set();

    for (var i=0; i<n; i++) {
        graph[i] = new Array();
        vertexes.add(i);
    }
    for (var edge of costs) {
        graph[edge[0]].push([edge[1], edge[2]]);
        graph[edge[1]].push([edge[0], edge[2]]);
    }
    
    console.log(graph);

    while (visited != vertexes) {
        var not_visited = new Set([vertexes].filter(x => !visited.has(x))); // 이부분 다시 작성해야할듯, 방문하지 않은 집합이 잘 나오지 않음.
        var min_edge_cost = [0, Infinity];
        for (var visited_v of visited) {
            for (var connected_v of graph[visited_v]) {
                if (not_visited.has(connected_v[0])) {
                    if (connected_v[1] < min_edge_cost[1])
                        min_edge_cost = connected_v;
                }
            }
        }
        visited.add(min_edge_cost[0]);
        answer = answer + min_edge_cost[1]
    }

    return answer;
}

solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	)