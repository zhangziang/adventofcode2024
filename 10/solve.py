#coding: utf-8

def get_next_nodes(node, graph, target):
    nodes = []
    directs = [(1,0),(-1,0),(0,1),(0,-1)]
    for direct in directs:
        x = node[0] + direct[0]
        y = node[1] + direct[1]
        if  0 <= x < len(graph) and 0 <= y < len(graph[0]) and graph[x][y] == target:
            nodes.append((x,y))
    return nodes

def solve_one():
    result = 0
    graph = []
    starts = [] #
    x = -1
    for line in open("input"):
        x += 1
        y = -1
        line_graph = []
        for i in list(line.strip()):
            y += 1
            v = int(i)
            line_graph.append(v)
            if v == 0:
                starts.append((x,y))
        graph.append(line_graph)
    # through all starts and get scores
    scores = {} # (x,y) -> score
    for start in starts:
        stack = [start]
        target = 1
        while len(stack) > 0:
            if target == 10:
                scores[start] = len(stack)
                result += len(stack)
                break
            new_stack = {}
            for node in stack:
                next_nodes = get_next_nodes(node, graph, target)
                for next_node in next_nodes:
                    new_stack[next_node] = True
            stack = new_stack.keys()
            target += 1
    return result

def solve_two():
    result = 0
    graph = []
    starts = [] #
    x = -1
    for line in open("input"):
        x += 1
        y = -1
        line_graph = []
        for i in list(line.strip()):
            y += 1
            v = int(i)
            line_graph.append(v)
            if v == 0:
                starts.append((x,y))
        graph.append(line_graph)
    # through all starts and get scores
    scores = {} # (x,y) -> score
    for start in starts:
        stack = [start]
        target = 1
        while len(stack) > 0:
            if target == 10:
                scores[start] = len(stack)
                result += len(stack)
                break
            new_stack = []
            for node in stack:
                next_nodes = get_next_nodes(node, graph, target)
                new_stack.extend(next_nodes) # Compared to the first question, there is no need to deduplicate next nodes.
            stack = new_stack
            target += 1
    return result


if __name__ == "__main__":
    print(solve_one())
    print(solve_two())

