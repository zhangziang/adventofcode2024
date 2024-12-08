# coding: utf-8


def get_one_part_andtinodes(one, two, x_max, y_max):
    result = []
    x1 = one[0]*2 - two[0]
    y1 = one[1]*2 - two[1]
    if x1 >= 0 and x1 < x_max and y1 >= 0 and y1 < y_max:
        result.append((x1, y1))
    x2 = two[0]*2 - one[0]
    y2 = two[1]*2 - one[1]
    if x2 >= 0 and x2 < x_max and y2 >= 0 and y2 < y_max:
        result.append((x2, y2))
    return result

def get_two_part_andtinodes(one, two, x_max, y_max):
    result = []
    # 0 ~ N
    i = 0
    while True:
        x = i * (one[0]-two[0]) + one[0]
        y = i * (one[1]-two[1]) + one[1]
        if x >= 0 and x < x_max and y >= 0 and y < y_max:
            result.append((x, y))
            i += 1
        else:
            break
    # -1 ~ -N
    i = -1
    while True:
        x = i * (one[0]-two[0]) + one[0]
        y = i * (one[1]-two[1]) + one[1]
        if x >= 0 and x < x_max and y >= 0 and y < y_max:
            result.append((x, y))
            i -= 1
        else:
            break
    return result

def solve_one(get_andtinodes):
    the_map = []
    for line in open("input"):
        the_map.append(line.strip())
    
    x_max = len(the_map)
    y_max = len(the_map[0])

    antinodes = {}
    antennas_locs = {}
    for x in range(x_max):
        for y in range(y_max):
            v = the_map[x][y]
            if v == '.':
                continue
            if v not in antennas_locs:
                antennas_locs[v] = []
            antennas_locs[v].append((x,y))
    for k,locs in antennas_locs.items():
        for i in range(len(locs)-1):
            one_loc =  locs[i]
            for j in range(i+1,len(locs)):
                two_loc = locs[j]
                _antinodes = get_andtinodes(one_loc, two_loc, x_max, y_max)
                for antinode in _antinodes:
                    antinodes[antinode] = True

    return len(antinodes)

if __name__ == "__main__":
    print(solve_one(get_one_part_andtinodes))
    print(solve_one(get_two_part_andtinodes))