# coding: utf-8


def move_to_num_end(cursor, line):
    while True:
        if line[cursor] >= '0' and line[cursor] <= '9':
            cursor += 1
            continue
        else:
            break
    return cursor

def solve_one_line(line):
    result = 0
    state = 0 # 0 need mul(, 1 need first num with, 2 needs second num with)
    cursor = 0
    num1 = 0
    while True:
        if cursor == len(line):
            break
        if state == 0:
            if line[cursor:cursor+4] != "mul(":
                cursor += 1
                continue
            else:
                cursor += 4
                state = 1
        if state == 1:
            _cursor = move_to_num_end(cursor, line)
            if cursor == _cursor or line[_cursor] != ",":
                cursor += 1
                state = 0
                continue
            else:
                num1 = int(line[cursor:_cursor])
                cursor = _cursor + 1
                state = 2
        if state == 2:
            _cursor = move_to_num_end(cursor, line)
            if cursor == _cursor or line[_cursor] != ")":
                cursor += 1
                state = 0
                continue
            else:
                num2 = int(line[cursor:_cursor])
                result += num1*num2
                cursor = _cursor + 1
                state = 0

    return result

def solve_one():
    result = 0
    for line in open("input"):
        result += solve_one_line(line)
    return result


def solve_two_line(enable,line):
    result = 0
    state = 0 # 0 need mul(, 1 need first num with, 2 needs second num with)
    cursor = 0
    num1 = 0
    while True:
        if cursor == len(line):
            break
        if not enable:
            if line[cursor:cursor+4] == "do()":
                enable = True
                cursor += 4
                state = 0
                continue
            cursor += 1
            state = 0
            continue
        # enable, first check is don't()
        if line[cursor:cursor+7] == "don't()":
            enable = False
            cursor += 7
            state = 0
            continue
        if state == 0:
            if line[cursor:cursor+4] != "mul(":
                cursor += 1
                continue
            else:
                cursor += 4
                state = 1
        if state == 1:
            _cursor = move_to_num_end(cursor, line)
            if cursor == _cursor or line[_cursor] != ",":
                cursor += 1
                state = 0
                continue
            else:
                num1 = int(line[cursor:_cursor])
                cursor = _cursor + 1
                state = 2
        if state == 2:
            _cursor = move_to_num_end(cursor, line)
            if cursor == _cursor or line[_cursor] != ")":
                cursor += 1
                state = 0
                continue
            else:
                num2 = int(line[cursor:_cursor])
                result += num1*num2
                cursor = _cursor + 1
                state = 0

    return (result, enable)

def solve_two():
    result = 0
    enable = True
    for line in open("input"):
        _result = solve_two_line(enable,line)
        result += _result[0]
        enable = _result[1]
    return result


if __name__ == "__main__":
    print(solve_one())
    print(solve_two())
