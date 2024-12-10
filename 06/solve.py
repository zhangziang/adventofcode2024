#coding: utf-8

def load_map():
    the_map = []
    guard = ()
    x = -1
    for line in open("input"):
        x += 1
        the_map.append(list(line.strip()))
        y = line.find('^')
        if y != -1:
            guard = (x, y)
            the_map[x][y] = 'x'
    return (the_map, guard)

def solve_one():
    data = load_map()
    the_map = data[0]
    guard = data[1]
    direct = 0 # 0 up 1 right 2 down 3 left
    direct_val = ((-1,0), (0,+1),(+1,0),(0,-1))

    x_len = len(the_map)
    y_len = len(the_map[0])

    result = 1
    # through the map
    while True:
        # check next
        next_x = guard[0] + direct_val[direct][0]
        next_y = guard[1] + direct_val[direct][1]
        if next_x < 0 or next_x >= x_len or next_y < 0 or next_y >= y_len:
            break
        if the_map[next_x][next_y] == '#':
            direct = (direct + 1) % 4
            continue
        if the_map[next_x][next_y] != 'x':
            the_map[next_x][next_y] = 'x'
            result += 1
        # move
        guard = (next_x, next_y)
    return result


def is_cycle(the_map, guard):
    direct = 0 # 0 up 1 right 2 down 3 left
    direct_val = ((-1,0), (0,+1),(+1,0),(0,-1))
    x_len = len(the_map)
    y_len = len(the_map[0])

    visited = {} # key is (direct, x, y)
    visited[(direct, guard[0], guard[1])] = True
    while True:
        # check next
        next_x = guard[0] + direct_val[direct][0]
        next_y = guard[1] + direct_val[direct][1]
        if next_x < 0 or next_x >= x_len or next_y < 0 or next_y >= y_len:
            break
        if the_map[next_x][next_y] == '#':
            direct = (direct + 1) % 4
            continue
        # check is visted
        if (direct, next_x, next_y) in visited:
            return True
        # move
        guard = (next_x, next_y)
        visited[(direct, guard[0], guard[1])] = True

    return False        

# 暴力解法，把第一题中路径每一个节点都设置为 #，然后判断是否成环。
# Brute force solution: Mark every node in the route of the first problem as '#', then check if it forms a loop.
def solve_two():
    data = load_map()
    the_map = data[0]
    guard = data[1]
    guard_start = guard
    direct = 0 # 0 up 1 right 2 down 3 left
    direct_val = ((-1,0), (0,+1),(+1,0),(0,-1))

    x_len = len(the_map)
    y_len = len(the_map[0])

    result = 0
    route = []
    # through the map & get route
    while True:
        # check next
        next_x = guard[0] + direct_val[direct][0]
        next_y = guard[1] + direct_val[direct][1]
        if next_x < 0 or next_x >= x_len or next_y < 0 or next_y >= y_len:
            break
        if the_map[next_x][next_y] == '#':
            direct = (direct + 1) % 4
            continue
        if the_map[next_x][next_y] != 'x':
            the_map[next_x][next_y] = 'x'
            route.append((next_x, next_y))
        # move
        guard = (next_x, next_y)
    
    # check every route node turn to #
    for node in route:
        temp_val = the_map[node[0]][node[1]]
        the_map[node[0]][node[1]] = '#'
        if is_cycle(the_map, guard_start):
            result += 1
        
        the_map[node[0]][node[1]] = temp_val

    return result


if __name__ == "__main__":
    print(solve_one())
    print(solve_two())        