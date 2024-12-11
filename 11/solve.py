# coding: utf-8


def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == "0":
            new_stones.append("1")
            continue
        if len(stone)%2 == 0:
            new_stones.append(str(int(stone[:(len(stone)//2)])))
            new_stones.append(str(int(stone[(len(stone)//2):])))
            continue
        new_stones.append(str(int(stone)*2024))
    return new_stones

def solve_one():
    stones = open("input").read().split()
    for i in range(25):
        stones = blink(stones)
    count_map = {}
    for stone in stones:
        if stone in count_map:
            count_map[stone] += 1
        else:
            count_map[stone] = 1
    return len(stones)

# after one, i found some stone frequent occurrence, some value stone can as one stone with count value
def blink_two(count_stones):
    new_count_stones = {}
    for stone in count_stones:
        count = count_stones[stone]
        new_stones = []
        if stone == "0":
            new_stones = ["1"]
        elif len(stone)%2 == 0:
            new_stones = [str(int(stone[:(len(stone)//2)])),
                          str(int(stone[(len(stone)//2):]))]
        else:
            new_stones = [str(int(stone)*2024)]
        for new_stone in new_stones:
            if new_stone in new_count_stones:
                new_count_stones[new_stone] += count
            else:
                new_count_stones[new_stone] = count
    return new_count_stones

def solve_two():
    stones = open("input").read().split()
    count_stones = {}
    for stone in stones:
        if stone in count_stones:
            count_stones[stone] += 1
        else:
            count_stones[stone] = 1
    for i in range(75):
        count_stones = blink_two(count_stones)
    return sum(count_stones.values())

if __name__ == "__main__":
    print(solve_one())
    print(solve_two())