# coding: utf-8
import sys

def read_puzzle():
    # puzzle = [(a_x,a_y),(b_x, b_y), (target_x, target_y)]
    puzzles = [] #
    line_num = -1
    for line in open("input"):
        line_num += 1
        if line_num % 4 == 3:
            continue
        x_y = [ int(i.strip()[2:]) for i in line.split(':')[1].split(',')] 
        if line_num % 4 == 0:
            puzzles .append([(x_y[0], x_y[1])])
            continue
        puzzles[-1].append((x_y[0], x_y[1]))
    return puzzles

def solve_one_puzzle(puzzle):
    a = puzzle[0]
    b = puzzle[1]
    t = puzzle[2]
    min_cost = sys.maxsize
    for i in range(1,101):
        for j in range(1,101):
            if a[0]*i +b[0]*j == t[0] and a[1]*i + b[1]*j == t[1]:
                min_cost = min(min_cost, 3*i + j)
    if min_cost == sys.maxsize:
        return 0
    return min_cost

'''
x*A0 + y*B0 = T0
x*A1 + y*B1 = T1

x*A0*A1 + y*B0*A1 = T0*A1
x*A1*A0 + y*B1*A0 = T1*A0

y*(B0*A1 - B1*A0) = T0*A1 - T1*A0
y = (T0*A1 - T1*A0) / (B0*A1 - B1*A0)


x*A0*B1 + y*B0*B1 = T0*B1
x*A1*B0 + y*B1*B0 = T1*B0
x = (T0*B1 - T1*B0) / (A0*B1 - A1*B0)

'''
def solve_two_puzzle(puzzle):
    a = puzzle[0]
    b = puzzle[1]
    t = puzzle[2]
    a_cost = (t[0]*b[1] - t[1]*b[0]) / (a[0]*b[1] - a[1]*b[0])
    b_cost = (t[0]*a[1] - t[1]*a[0]) / (b[0]*a[1] - b[1]*a[0])
    if a_cost < 0 or int(a_cost) != a_cost:
        return 0
    if b_cost < 0 or int(b_cost) != b_cost:
        return 0
    return int(a_cost) * 3 + int(b_cost)

def solve_one():
    result = 0
    puzzles = read_puzzle()
    for puzzle in puzzles:
        result += solve_two_puzzle(puzzle)
    return result

def solve_two():
    result = 0
    puzzles = read_puzzle()
    for puzzle in puzzles:
        puzzle[2] = (puzzle[2][0] + 10000000000000, puzzle[2][1] + 10000000000000)
        result += solve_two_puzzle(puzzle)
    return result

if __name__ == "__main__":
    print(solve_one())
    print(solve_two())