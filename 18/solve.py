from turtle import pos, position
from typing import List


def construct_map(positions: List[str], w: int):
    m = [[0 for i in range(w)] for j in range(w)]
    for pos in positions:
        i_p = list(map(lambda x: int(x), pos.strip().split(",")))
        x = i_p[0]
        y = i_p[1]

        m[y][x] = 1
    return m


def sample():
    positions = [
        "5,4",
        "4,2",
        "4,5",
        "3,0",
        "2,1",
        "6,3",
        "2,4",
        "1,5",
        "0,6",
        "3,3",
        "2,6",
        "5,1",
    ]
    w = 7
    m_map = construct_map(positions, w)
    return min_road(m_map, w)


def min_road(m_map, w):
    vals = [[-1 for i in range(w)] for j in range(w)]
    vals[0][0] = 0
    directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = [(0, 0)]
    while True:
        if len(queue) == 0:
            break
        cur = queue[0]
        queue = queue[1:]
        # visit next
        val = vals[cur[0]][cur[1]]
        for direct in directs:
            next_x = cur[0] + direct[0]
            next_y = cur[1] + direct[1]
            if next_x < 0 or next_x >= w:
                continue
            if next_y < 0 or next_y >= w:
                continue
            if vals[next_x][next_y] != -1 or m_map[next_x][next_y] == 1:
                continue
            vals[next_x][next_y] = val + 1
            queue.append((next_x, next_y))
            if next_x == w - 1 and next_y == w - 1:
                return val + 1
    return vals[w - 1][w - 1]


def solve_1():
    with open("input") as f:
        w = 71
        m_map = construct_map(f.readlines()[:1024], w)
        return min_road(m_map, w)


print(sample())
print(solve_1())
