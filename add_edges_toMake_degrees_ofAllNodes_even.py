"""There is an undirected graph consisting of n nodes numbered from 1 to n. You are given the integer n and a 2D array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi. The graph can be disconnected.

You can add at most two additional edges (possibly none) to this graph so that there are no repeated edges and no self-loops.

Return true if it is possible to make the degree of each node in the graph even, otherwise return false.

The degree of a node is the number of edges connected to it."""



from collections import defaultdict
def isPossible(edges):
    graph_dict = defaultdict(set)
    for i,j in edges:
        graph_dict[i].add(j)
        graph_dict[j].add(i)
    #print(graph_dict)

    odd_nodes = [a for a in graph_dict if len(graph_dict[a])%2 == 1]

    if not odd_nodes:
        print("Nodes are already even, odd node count: ", odd_nodes)
        return True
    elif len(odd_nodes) == 1 or len(odd_nodes) == 3 or len(odd_nodes) >4:
        print("Can't make the nodes even")
        return False
    elif len(odd_nodes) == 2:
        a,b = odd_nodes[0], odd_nodes[1]
        if a not in graph_dict[b]:
            return True
        for i in range(0,len(graph_dict)):
            if i not in graph_dict[a] and i not in graph_dict[b]:
                return True
        return False
    else:
        a,b,c,d = odd_nodes[0], odd_nodes[1], odd_nodes[2], odd_nodes[3]
        if b not in graph_dict[a] and d not in graph_dict[c]:
            return True
        if c not in graph_dict[a] and d not in graph_dict[b]:
            return True
        if d not in graph_dict[a] and c not in graph_dict[b]:
            return True
        return False

graph =[[1,2],[1,3],[1,4]]
print(isPossible(graph))