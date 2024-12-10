#coding: utf-8

def solve_one():
    result = 0
    for line in open("input"):
        data = line.strip().split(":")
        target = int(data[0])
        params = [int(i) for i in data[1].strip().split()]
        for operator in range(2 ** (len(params)-1)):
            cal = params[0]
            for i in range(0, len(params)-1):
                one_operator = (operator >> (len(params)-2-i)) & 1
                if one_operator == 1:
                    cal *= params[i+1]
                else:
                    cal += params[i+1]
            if cal == target:
                result += target
                break
    return result

def combine_two_num(a, b):
    s = 10
    while (b%s != b):
        s *= 10
    return a * s +b

def solve_two():
    result = 0
    line_num = 0
    for line in open("input"):
        data = line.strip().split(":")
        target = int(data[0])
        params = [int(i) for i in data[1].strip().split()]
        hit = False
        line_num += 1
        print(f"{line_num}/850, {len(params)}")
        for operator_one in range(2 ** (len(params)-1)):
            if hit:
                break
            for operator_two in range(2 ** (len(params)-1)):
                if operator_one | operator_two != (2 ** (len(params)-1) -1):
                    continue
                cal = params[0]
                for i in range(0, len(params)-1):
                    cur_val = params[i+1]
                    one_operator = (operator_one >> (len(params)-2-i)) & 1
                    two_operator = (operator_two >> (len(params)-2-i)) & 1
                    # 01 for * 10 for + 11 for ||
                    if one_operator == 0 and two_operator == 1:
                        cal *= cur_val
                        continue
                    if one_operator == 1 and two_operator == 0:
                        cal += cur_val
                        continue
                    cal = combine_two_num(cal, cur_val)
                    if cal > target:
                        break
                if cal == target:
                    result += target
                    hit = True
                    break
    return result    


if __name__ == "__main__":
    print(solve_one())
    print(solve_two())