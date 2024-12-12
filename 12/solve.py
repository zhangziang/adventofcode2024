# coding: utf-8

def cal_plant_one(x, y, garden, visited):
    directs = [(0,1), (0,-1),(1,0),(-1,0)]
    area = 0
    perimeter = 0
    val = garden[x][y]
    stack = [(x,y)]
    while len(stack) > 0:
        node = stack[0]
        stack = stack[1:]
        if node in visited:
            continue
        area += 1
        visited[node] = True
        for direct in directs: # 在四个方向上判断是否结束，结束则周长加一
            next_x = node[0] + direct[0]
            next_y = node[1] + direct[1]
            if next_x < 0 or next_x >= len(garden) or next_y < 0 or next_y >= len(garden[0]):
                perimeter += 1
                continue
            if garden[next_x][next_y] != val:
                perimeter += 1
                continue
            if garden[next_x][next_y] == val and (next_x, next_y) not in visited:
                stack.append((next_x, next_y))
                continue
    return area * perimeter

def move_cursor(cursor_x, cursor_y, max_y, visited):
    if cursor_y < max_y - 1:
        cursor_y += 1
    else:
        cursor_y = 0
        cursor_x += 1
    if (cursor_x, cursor_y) not in visited:
        return cursor_x, cursor_y
    return move_cursor(cursor_x, cursor_y, max_y, visited)

def solve_one():
    garden = []
    for line in open("input"):
        garden.append(line.strip())
    visited = {} # key is (x,y)
    max_x = len(garden)
    max_y = len(garden[0])
    result = 0
    cursor_x = 0
    cursor_y = 0

    while len(visited) != max_x * max_y:
        result += cal_plant_one(cursor_x, cursor_y, garden, visited)
        cursor_x,cursor_y = move_cursor(cursor_x, cursor_y, max_y, visited)        
    return result

# 遇到边界是时，+- 0.5 作为一个边节点，并且需要记录边界点的方向(四个位置都需要)
# 然后对每一个方向的节点按照横/纵进行处理
# 以横向为例，收集在同一个的纵坐标上所有的值，如果值不是连续+1 的，说明是一个边。四个方向计算完成可以得到总边数。
def cal_plant_two(x, y, garden, visited):
    directs = [(0,1), (0,-1),(1,0),(-1,0)]
    area = 0
    side = 0
    # side node is node in one axis +- 0.5
    four_side_nodes = [[],[],[],[]] # 0 left | 1 right | 2 top -- 3 bottom --
    stack = [(x,y)]
    val = garden[x][y]
    while len(stack) != 0:
        node = stack[0]
        stack = stack[1:]
        if node in visited:
            continue
        area += 1
        visited[node] = True
        for direct in directs:
            next_x = node[0] + direct[0]
            side_x = node[0] + direct[0]/2
            next_y = node[1] + direct[1]
            side_y = node[1] + direct[1]/2
            side_direct = 0
            if direct[1] == 1:
                side_direct = 1
            if direct[0] == -1:
                side_direct = 2
            if direct[0] == 1:
                side_direct = 3
            if next_x < 0 or next_x >= len(garden) or next_y < 0 or next_y >= len(garden[0]):
                side_nodes = four_side_nodes[side_direct]
                side_nodes.append((side_x, side_y))
                continue
            if garden[next_x][next_y] != val:
                side_nodes = four_side_nodes[side_direct]
                side_nodes.append((side_x, side_y))
                continue
            if garden[next_x][next_y] == val and (next_x, next_y) not in visited:
                stack.append((next_x, next_y))
                continue
    # cal side num each axis
    def cal_side(nodes, direct): # direct 0 mean x
        side = {} # key is other axis, value is direct's axis values
        key_i = (1-direct)
        val_i = direct
        for node in nodes:
            key_v = node[key_i]
            val_v = node[val_i]
            if key_v in side:
                side[key_v].append(val_v)
            else:
                side[key_v] = [val_v]
        # same other axis dont continuous value(step is 1) mean one side
        side_num = 0
        for positions in side.values():
            positions.sort()
            pre_position = positions[0]
            side_num += 1
            for position in positions[1:]:
                if position != pre_position + 1:
                    side_num += 1
                pre_position = position
        return side_num
    side_num = 0
    for direct, side_nodes in enumerate(four_side_nodes):
        axies = 0
        if direct > 1:
            axies = 1
        _side_num = cal_side(side_nodes, axies)
        # print(direct, side_nodes, _side_num)
        side_num += _side_num
    # print("result",val, area, side_num, area*side_num)
    return area * side_num

def solve_two():
    garden = []
    for line in open("input"):
        garden.append(line.strip())
    visited = {} # key is (x,y)
    max_x = len(garden)
    max_y = len(garden[0])
    result = 0
    cursor_x = 0
    cursor_y = 0

    while len(visited) != max_x * max_y:
        result += cal_plant_two(cursor_x, cursor_y, garden, visited)
        cursor_x,cursor_y = move_cursor(cursor_x, cursor_y, max_y, visited)        
    return result
    

if __name__=="__main__":
    print(solve_one())
    print(solve_two())