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

def cal_plant_two(x, y, garden, visited):
    directs = [(0,1), (0,-1),(1,0),(-1,0)]
    area = 0
    side = 0
    # side node is node one axis +- 0.5
    x_side_nodes = [] # x axis | 
    y_side_nodes = [] # y axis --
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
            side_direct = abs(direct[0]) # 0 mean | 1 mean --
            if next_x < 0 or next_x >= len(garden) or next_y < 0 or next_y >= len(garden[0]):
                if side_direct:
                    y_side_nodes.append((side_x, side_y))
                else:
                    x_side_nodes.append((side_x, side_y))
                continue
            if garden[next_x][next_y] != val:
                if side_direct:
                    y_side_nodes.append((side_x, side_y))
                else:
                    x_side_nodes.append((side_x, side_y))
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
    print(x_side_nodes)
    print(y_side_nodes)
    x_side_num = cal_side(x_side_nodes, 0)
    y_side_num = cal_side(y_side_nodes, 1)
    side_num  = x_side_num + y_side_num
    print("result",val, area,x_side_num, y_side_num, side_num, area*side_num)
    return area * side_num

def solve_two():
    garden = []
    for line in open("input4"):
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