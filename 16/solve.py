#coding: utf-8

import sys

def read_map():
    the_map = []
    start = ()
    end = ()   
    x = 0
    for line in open("input"):
        line = line.strip()
        the_map.append(list(line))
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
        return (sys.maxsize, [])
    if node == end:
        return (score,[])
    
    if the_map[node[0]][node[1]] == "#":
        return (sys.maxsize,[])
    
    if node in visted:
        return (sys.maxsize - 1,[node]) # meet cycle

    if (node, direct) in global_visited:
        _visited_score = global_visited[(node, direct)][0]
        if _visited_score == sys.maxsize:
            return (sys.maxsize,[])
        if _visited_score != sys.maxsize - 1:
            return (score + _visited_score,[])
        # 判断成环的节点是否已经 visited，如果 visited 表明 这条链路不可取
        for cycle_node in global_visited[(node, direct)][1]:
            if cycle_node in visted:
                return (sys.maxsize - 1, global_visited[(node, direct)][1])
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
    scores_val = [i[0] for i in scores]
    scores_cycle_nodes = []
    for i in scores:
        scores_cycle_nodes.extend(i[1])
    min_score = min(scores_val)
    if min_score == sys.maxsize:
        global_visited[(node, direct)] = (sys.maxsize,[]) # all route is meet wall
        return (min_score, [])
    if min_score != sys.maxsize-1:
        global_visited[(node, direct)] = (min_score - score, [])
        return (min_score, [])
    # meet cycle
    global_visited[(node, direct)] = (sys.maxsize - 1, scores_cycle_nodes)
    return (min_score, scores_cycle_nodes)

def dfs_one(the_map, node, end, direct, score, visted):
    directs = [[1,0], [-1,0], [0,1],[0,-1]] # down, up, right, left
    turn_directs = [[2,3],[2,3],[1,0],[1,0]]
    if  node[0] < 0 or node[0] >= len(the_map) or node[1] < 0 or node[1] >= len(the_map[0]):
        return sys.maxsize
    if node == end:
        return score
    
    if the_map[node[0]][node[1]] == "#":
        return sys.maxsize
    
    if node in visted:
        return sys.maxsize
    
    # move front
    next_node = (node[0] + directs[direct][0], node[1] + directs[direct][1])
    visted[node] = True
    move_front_score = dfs_one(the_map,next_node, end, direct, score+1, visted)
    if move_front_score != sys.maxsize:
        return move_front_score
    # turn other direct
    for next_direct in turn_directs[direct]:
        next_node = (node[0] + directs[next_direct][0], node[1] + directs[next_direct][1])
        turn_score = dfs_one(the_map, next_node, end, next_direct, score + 1001, visted)
        if turn_score != sys.maxsize:
            return turn_score
    del(visted[node])
    return sys.maxsize

def state_map(the_map):
    route_node_num = 0
    for x in range(len(the_map)):
        for y in range(len(the_map[0])):
            if the_map[x][y] == ".":
                route_node_num += 1
    return route_node_num

def compress_map(the_map):
    directs = [[1,0], [-1,0], [0,1],[0,-1]] # down, up, right, left
    for x in range(len(the_map)):
        for y in range(len(the_map[0])):
            if the_map[x][y] == ".":
                wall_num = 0
                for d in directs:
                    wx = x + d[0]
                    wy = y + d[1]
                    if the_map[wx][wy] == "#":
                        wall_num += 1
                if wall_num == 3:
                    the_map[x][y] = "#"



def solve_one():
    the_map, start, end = read_map()
    
    # route_node_num =  state_map(the_map)
    # print(f"start, route_node_num:{route_node_num}")
    # for i in range(100):
    #     compress_map(the_map)
    #     new_route_node_num = state_map(the_map)
    #     print(f"{i},route_node_num:{new_route_node_num}")
    #     if new_route_node_num == route_node_num:
    #         print("over")
    #         break
    #     route_node_num = new_route_node_num
    # with open("c_map","w") as f:
    #     for line in the_map:
    #         f.write("".join(line))
    #         f.write("\n")
    # global_visited = {}
    right_score = dfs_one(the_map, start, end, 2, 0, {})
    return right_score

if __name__ == "__main__":
    sys.setrecursionlimit(20000)
    print(solve_one())