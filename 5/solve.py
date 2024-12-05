# coding: utf-8

def build_dep_map(dep_lines):
    dep_map = {} # key include both side A, value is  map:key is both side B and value is True mean B before A, False mean after
    for line in dep_lines:
        d = [ int(i) for i in line.strip().split("|")]
        a = d[0]
        b = d[1]
        if a not in dep_map:
            dep_map[a] = {}
        if b not in dep_map:
            dep_map[b] = {}
        dep_map[a][b] = False
        dep_map[b][a] = True
    return dep_map

def check_dep_and_return_mid(line, dep_map):
    val = [int(i) for i in line.strip().split(",")]
    mid = val[len(val)//2]

    for i in range(len(val)-1):
        for j in range(i+1, len(val)):
            a = val[i]
            b = val[j]
            if a not in dep_map:
                continue
            if dep_map[a][b]:
                return False
    
    return mid

def solve_one():
    dep_input = []
    print_input = []
    turn_print = False
    for line in open("input"):
        if turn_print:
            print_input.append(line)
            continue
        if line.strip() == "":
            turn_print = True
            continue
        dep_input.append(line)
    dep_map = build_dep_map(dep_input)

    result = 0
    for line in print_input:
        result += check_dep_and_return_mid(line, dep_map)
    return result


def check_dep_fix_return_mid(line, dep_map):
    val = [int(i) for i in line.strip().split(",")]
    resort = False
    i = 0
    while True:
        if i == len(val) - 1:
            break
        for j in range(i+1, len(val)):
            a = val[i]
            b = val[j]
            if a not in dep_map:
                continue
            if dep_map[a][b]:
                resort = True
                val[i],val[j] = val[j], val[i]
                i -= 1
                break
        i += 1 # move to next

    if resort:
        return val[len(val)//2]
    return 0

def solve_two():
    dep_input = []
    print_input = []
    turn_print = False
    for line in open("input"):
        if turn_print:
            print_input.append(line)
            continue
        if line.strip() == "":
            turn_print = True
            continue
        dep_input.append(line)
    dep_map = build_dep_map(dep_input)
    result = 0
    for line in print_input:
        result += check_dep_fix_return_mid(line, dep_map)
    return result


if __name__ == "__main__":
    print(solve_one())
    print(solve_two())