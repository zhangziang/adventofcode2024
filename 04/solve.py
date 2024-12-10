#coding utf-8

def get_bit(x,y, data):
    if x < 0 or x >= len(data):
        return ''
    if y < 0 or y >= len(data[x]):
        return ''
    return data[x][y]

# for part one
def get_left(x,y):
    return ((x,y), (x,y-1),(x,y-2),(x,y-3))
def get_right(x,y):
    return ((x,y), (x,y+1),(x,y+2),(x,y+3))
def get_up(x,y):
    return ((x,y), (x-1,y),(x-2,y),(x-3,y))
def get_down(x,y):
    return ((x,y), (x+1,y),(x+2,y),(x+3,y))
def get_left_up(x,y):
    return ((x,y), (x-1,y-1),(x-2,y-2),(x-3,y-3))
def get_right_up(x,y):
    return ((x,y), (x-1,y+1),(x-2,y+2),(x-3,y+3))
def get_left_down(x,y):
    return ((x,y), (x+1,y-1),(x+2,y-2),(x+3,y-3))
def get_right_down(x,y):
    return ((x,y), (x+1,y+1),(x+2,y+2),(x+3,y+3))

# for part one
def check_each_direct(x, y, data):
    result = 0
    direct_func = [get_left, get_right, get_up, get_down, get_left_up, get_right_up, get_left_down, get_right_down]
    for f in direct_func:
        bit_pos_list = f(x,y)
        values = [ get_bit(pos[0], pos[1], data)  for pos in bit_pos_list]
        if ''.join(values) == "XMAS":
            result += 1
    return result
    
def solve_one():
    result = 0
    data = []
    for line in open('input'):
        data.append(line.strip())
    # find X and check each direct is match XMAS
    x = -1
    for line in data:
        x += 1
        y = -1
        for bit in line:
            y += 1
            if bit == 'X':
                result += check_each_direct(x,y, data)
    return result


# for part two
def check_is_mas(x,y,data):
    poss = [((-1,+1), (+1,-1)), ((+1,+1),(-1,-1))]
    for pos in poss:
        a = get_bit(x + pos[0][0], y + pos[0][1], data)
        b = get_bit(x + pos[1][0], y + pos[1][1], data)
        if (a == 'M' and b == 'S') or (a == 'S' and b == 'M'):
            continue
        return False
    return True

def solve_two():
    result = 0
    data = []
    for line in open('input'):
        data.append(line.strip())
    # find A and check is MAS
    x = -1
    for line in data:
        x += 1
        y = -1
        for bit in line:
            y += 1
            if bit == 'A' and check_is_mas(x,y, data):
                result += 1
    return result

if __name__ == "__main__":
    print(solve_one())
    print(solve_two())