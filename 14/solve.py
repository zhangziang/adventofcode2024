#coding: utf-8

import copy


def get_bots():
    bots = []
    for line in open("input"):
        v = line.split()
        first_pos = [int(i) for i in v[0][2:].split(",")]
        vel = [int(i) for i in v[1][2:].split(",")]
        bots.append([first_pos, vel])
    return bots

def bot_in_quadrant(x_len, y_len, x, y):
    four_quadrant = [(0,x_len//2-1, 0, y_len//2-1), (x_len//2+1, x_len-1, 0, y_len//2-1), (0,x_len//2-1, y_len//2+1, y_len-1), (x_len//2+1, x_len-1, y_len//2+1, y_len-1)]
    for i in range(4):
        quadrant = four_quadrant[i]
        if  quadrant[0] <= x <= quadrant[1] and quadrant[2] <= y <= quadrant[3]:
            return i
    return 4

def solve_one():
    x_len = 101
    y_len = 103
    
    four_value = [0, 0, 0, 0, 0] # index = 4 is mid
    bots = get_bots()
    for bot in bots:
        # move bot 100s
        first_position = bot[0]
        vel = bot[1]
        x = (first_position[0] + 100*vel[0]) % x_len
        y = (first_position[1] + 100*vel[1]) % y_len
        quadrant_i = bot_in_quadrant(x_len, y_len, x, y)
        four_value[quadrant_i] += 1
    
    result = 1
    for v in four_value[0:4]:
        result *= v
    return result

def print_bots(x_len, y_len, bots):
    m = [] 
    for i in range(y_len):
        m.append([])
        for j in range(x_len):
            m[i].append(".")
    for bot in bots:
        p = bot[0]
        m[p[1]][p[0]] = "*"
    for line in m:
        print("".join(line))


def check_bots(bots):
    visted = {}
    m = {}
    for bot in bots:
        m[(bot[0][0],bot[0][1])] = True
    max_ares = 0
    directs = [[1,0], [-1,0], [0,1], [0,-1]]
    for bot in bots:
        stack = [(bot[0][0], bot[0][1])]
        _ares = 0
        while len(stack) != 0:
            n = stack[0]
            stack = stack[1:]
            if n in visted:
                continue
            visted[n] = True
            
            _ares += 1
            for direct in directs:
                x = n[0] + direct[0]
                y = n[1] + direct[1]
                if (x,y) in visted:
                    continue
                if (x,y) in m:
                    stack.append((x,y))
        max_ares = max(max_ares, _ares)
    return max_ares

def solve_two():
    bots = get_bots()
    
    x_len = 101
    y_len = 103
    # print_bots(x_len, y_len, bots)
    for i in range(10000):
        _bots = copy.deepcopy(bots)
        for bot in _bots:
                first_position = bot[0]
                vel = bot[1]
                x = (first_position[0] + i*vel[0]) % x_len
                y = (first_position[1] + i*vel[1]) % y_len
                bot[0] = [x, y]
        # check bots
        max_ares = check_bots(_bots)
        if max_ares > 200:
            print(i, max_ares)
            print_bots(x_len, y_len, _bots)
        
    return -1


if __name__ == "__main__":
    print(solve_one())
    print(solve_two())