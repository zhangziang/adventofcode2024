#coding: utf-8


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

def solve_two():
    bots = get_bots()
    
    x_len = 101
    y_len = 103
    
    for i in range(100):
        print(f"====={i}========================================================")
        for bot in bots:
                # move bot 100s
                first_position = bot[0]
                vel = bot[1]
                x = (first_position[0] + 1*vel[0]) % x_len
                y = (first_position[1] + 1*vel[1]) % y_len
                bot[0] = [x, y]
        print_bots(x_len, y_len, bots)



if __name__ == "__main__":
    print(solve_one())
    print(solve_two())