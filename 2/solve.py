# coding: utf-8


def is_safe(values):
    if len(values) == 1:
        return True
    dirct = values[1] - values[0] > 0
    for i in range(len(values)-1):
        diff = values[i+1] - values[i]
        if abs(diff) > 3 or abs(diff) < 1:
            return False
        if dirct != (diff > 0):
            return False
    return True

def solve_one():
    result = 0
    for line in open("input"):
        values = [ int(i) for i in line.split()]
        if is_safe(values):
            result += 1
    return result

def solve_two():
    result = 0
    for line in open("input"):
        values = [ int(i) for i in line.split()]
        if is_safe(values):
            result += 1
            continue
        # not safe try drop one
        for i in range(len(values)):
            if is_safe(values[:i]+values[i+1:]):
                result += 1
                break
    return result

if __name__ == "__main__":
    print(solve_one())
    print(solve_two())