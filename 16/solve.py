#coding: utf-8

import sys

def read_map():
    the_map = []
    start = ()
    end = ()   
    x = 0
    for line in open("input"):
        line = line.strip()
        the_map.append(line)
        if "S" in line:
            start = (x,  line.index('S'))
        if "E" in line:
            end = (x,  line.index('E'))
        x += 1
    return (the_map, start, end)

def dfs(the_map, node, end, direct, score, visted, global_visited):
    directs = [[1,0], [-1,0], [0,1],[0,-1]] # down, up, right, left
    turn_directs = [[2,3],[2,3],[0,1],[0,1]]
    if  node[0] < 0 or node[0] >= len(the_map) or node[1] < 0 or node[1] >= len(the_map[0]):
        return sys.maxsize
    if node == end:
        return score
    
    if the_map[node[0]][node[1]] == "#":
        return sys.maxsize
    
    if node in visted:
        return sys.maxsize - 1 # meet cycle

    if (node, direct) in global_visited:
        _visited_score = global_visited[(node, direct)]
        if _visited_score == sys.maxsize:
            return sys.maxsize
        return score + _visited_score    
    
    # global_visited[(node, direct)] = sys.maxsize
    # move front
    scores =[]
    next_node = (node[0] + directs[direct][0], node[1] + directs[direct][1])
    visted[node] = True
    move_front_score = dfs(the_map,next_node, end, direct, score+1, visted, global_visited)
    scores.append(move_front_score)
    # turn other direct
    for next_direct in turn_directs[direct]:
        next_node = (node[0] + directs[next_direct][0], node[1] + directs[next_direct][1])
        turn_score = dfs(the_map, next_node, end, next_direct, score + 1001, visted, global_visited)
        scores.append(turn_score)
    del(visted[node])
    min_score = min(scores)
    if min_score == sys.maxsize:
        global_visited[(node, direct)] = sys.maxsize # all route is meet wall
        return min_score
    if min_score != sys.maxsize-1:
        global_visited[(node, direct)] = min_score - score
    return min_score
        

def solve_one():
    the_map, start, end = read_map()
    global_visited = {}
    right_score = dfs(the_map, start, end, 2, 0, {}, global_visited)
    return right_score

if __name__ == "__main__":
    # sys.setrecursionlimit(20000)
    print(solve_one())