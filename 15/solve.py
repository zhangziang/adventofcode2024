# coding: utf-8
def solve_one():
    # read puzzle
    site_map = []
    read_site_map = True
    bot = []
    moves = []
    i = -1
    for line in open("input"):
        i += 1
        line_val = line.strip()
        if line_val == "":
            read_site_map = False
            continue
        if read_site_map:
            site_map.append(list(line_val))
            if '@' in line_val:
                bot = [i, line_val.index('@')]  
            continue
        moves.append(line_val)

    # move
    directs = {"^": [-1,0], "v": [1, 0], "<": [0, -1], ">": [0, 1]}
    for move in moves:
        for m in move:
            direct = directs[m]
            start_x = bot[0]
            start_y = bot[1]
            empty_loc = []
            while True:
                next_loc_x = start_x + direct[0]
                next_loc_y = start_y + direct[1]
                if site_map[next_loc_x][next_loc_y] == '#':
                    break
                if site_map[next_loc_x][next_loc_y] == '.':
                    empty_loc = [next_loc_x, next_loc_y]
                    break
                # meet O
                start_x,start_y = next_loc_x, next_loc_y
            if empty_loc:
                next_loc_x = bot[0] + direct[0]
                next_loc_y = bot[1] + direct[1]
                site_map[bot[0]][bot[1]] = '.'
                bot = [next_loc_x, next_loc_y]
                if site_map[next_loc_x][next_loc_y] == 'O':
                    site_map[empty_loc[0]][empty_loc[1]] = 'O'
                site_map[next_loc_x][next_loc_y] = '@'
    result = 0
    # cal sit map
    for x in range(len(site_map)):
        for y in range(len(site_map[0])):
            if site_map[x][y] == 'O':            
                result += 100 * x + y
    return result

def move_two(site_map, bot, move_direct):
    directs = {"^": [-1,0], "v": [1, 0], "<": [0, -1], ">": [0, 1]}
    direct = directs[move_direct]
    if move_direct == '<' or move_direct == '>':
        x = bot[0]
        cursor_y = bot[1]
        find_y = bot[1]
        while True:
            next_y = cursor_y + direct[1]
            if site_map[x][next_y] == '#':
                break
            if site_map[x][next_y] == '.':
                find_y = next_y
                break
            cursor_y = next_y + direct[1]
        
        if find_y == bot[1]:
            return bot

        while find_y != bot[1]:
            site_map[x][find_y], site_map[x][find_y + direct[1]*-1] = site_map[x][find_y + direct[1]*-1], site_map[x][find_y]
            find_y += direct[1]*-1
        bot[1] = bot[1] + direct[1]
        return bot
    # move up or down
    need_locs = [bot]
    move_step = 0
    while True:
        move_step += 1
        next_need_locs = []
        for loc in need_locs:
            next_x = loc[0] + direct[0]
            # check all next need move
            if site_map[next_x][loc[1]] == "#":
                return bot
            val = site_map[next_x][loc[1]]
            if val == "[":
                next_need_locs.append([next_x, loc[1]])
                next_need_locs.append([next_x, loc[1]+1])
            if val == "]":
                next_need_locs.append([next_x, loc[1]])
                next_need_locs.append([next_x, loc[1]-1])
        if len(next_need_locs) == 0:
            # can move
            break
        need_locs = next_need_locs
    # move n step
    step_locs = [bot]
    step_vals = [site_map[bot[0]][bot[1]]]
    site_map[bot[0]][bot[1]] = "."
    while move_step > 0:
        move_step -= 1
        next_need_locs = []
        next_need_vals = []
        for i in range(len(step_locs)):
            val = step_vals[i]
            loc = step_locs[i]
            next_x = loc[0] + direct[0]
            if site_map[next_x][loc[1]] == "[":
                next_need_locs.append([next_x,loc[1]])
                next_need_vals.append("[")
                site_map[next_x][loc[1]] = "."
                next_need_locs.append([next_x,loc[1]+1])
                next_need_vals.append("]")
                site_map[next_x][loc[1]+1] = "."
            if site_map[next_x][loc[1]] == "]":
                next_need_locs.append([next_x,loc[1]-1])
                next_need_vals.append("[")
                site_map[next_x][loc[1]-1] = "."
                next_need_locs.append([next_x,loc[1]])
                next_need_vals.append("]")
                site_map[next_x][loc[1]] = "."
            # move
            site_map[next_x][loc[1]] = val
        step_locs = next_need_locs
        step_vals = next_need_vals
        
    return [bot[0]+direct[0], bot[1]]
        
        
        

def solve_two():
    # read puzzle
    site_map = []
    read_site_map = True
    bot = []
    moves = []
    i = -1
    for line in open("input"):
        i += 1
        line_val = line.strip()
        if line_val == "":
            read_site_map = False
            continue
        if read_site_map:
            l = []
            for a in line_val:
                if a == "#":
                    l.append("#")
                    l.append("#")
                    continue
                if a == ".":
                    l.append(".")
                    l.append(".")
                    continue
                if a == "@":
                    l.append("@")
                    l.append(".")
                    continue
                if a == "O":
                    l.append("[")
                    l.append("]")
                    continue
            site_map.append(l)
            if '@' in line_val:
                bot = [i, l.index('@')]
            continue
        moves.append(line_val)
    # move 
    for move in moves:
        for m in move:
            # print(bot, m)
            bot = move_two(site_map, bot, m)
            # print(bot)
            # for line in site_map:
            #     print("".join(line))
    # cal
    result = 0
    for x in range(len(site_map)):
        for y in range(len(site_map[0])):
            if site_map[x][y] == '[':
                result += 100 * x + y
    return result


if __name__ == "__main__":
    print(solve_one())
    print(solve_two())
