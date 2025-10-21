from socket import has_ipv6
from tkinter.constants import X
from turtle import Turtle
from unittest import result


def run(a, b, c, current_cur, input): # return a b c, output(list), next_cur
    opt = int(input[current_cur])
    val = int(input[current_cur+1])
    real_v = val
    next_cur = current_cur + 2
    if val == 4:
        real_v = a
    if val == 5:
        real_v = b
    if val == 6:
        real_v = c
    output = []
    if opt == 0:
        a = a//(2 ** real_v)
    if opt == 1:
        b ^= val
    if opt == 2:
        b = real_v % 8
    if opt == 3:
        if a != 0:
            next_cur = val
    if opt == 4:
        b ^= c
    if opt == 5:
        output.append(real_v%8)
    if opt == 6:
        b = a//(2 ** real_v)
    if opt == 7:
        c = a//(2 ** real_v)

    return a,b,c,output,next_cur



def solve_1(a):
    a_val = a
    b_val = 0
    c_val = 0
    output = []
    program = "2413751503435530"
    cur = 0
    while True:
        if cur >= len(program):
            break
        a_val, b_val, c_val, sub_output, cur = run(a_val, b_val, c_val, cur, program)
        output.extend(sub_output)
    # print(f"a_val:{a_val}")
    # print(f"b_val:{b_val}")
    # print(f"c_val:{c_val}")
    return ','.join(map(lambda x: str(x), output))


# 解题思路是把正向的链路走遍会发现，每次是使用 a 做一些运算，然后  a >> 3 再来一轮，直到 a = 0
# 所以结局思路就是把 3 位看成一组，取值范围是 0-7，遍历 0-7，反向找到对应的 a 值，如果遇到不可解需要回溯
def reverse_run():
    # 24 b =a % 8
    # 13 b = b ^ 3
    # 75 c = a // (2 ** b)
    # 15 b = b ^ 5
    # 03 a = a // 8
    # 43 b ^= c
    # 55 out b%8
    # 30 move to frist untile a is zero
    # target  2413751503435530
    # reverse 0355343051573142
    reverse = "0355343051573142"
    a = 0 # 30
    b = 0
    c = 0
    sub_a_process = {}
    i = 0
    while True:
        if i<0:
            print("no result")
            break
        if i>=len(reverse):
            print(f"result: {a}")
            break

        target = int(reverse[i])
        if i in sub_a_process:
            sub_a = sub_a_process[i] + 1
        else:
            sub_a = 0
        if sub_a > 7: # backoff
            print(f"back off, i:{i}, target:{target}")
            sub_a_process[i] = -1
            i -= 1
            a = a >> 3
            continue
        sub_a_process[i] = sub_a
        ta = (a << 3) + sub_a
        b  = sub_a
        b ^= 3
        c = ta >> b
        b ^= 5
        b ^= c
        if b%8 == target:
            print(f"hit, i:{i}, target:{target}, ta: {ta}, sub_a:{sub_a}")
            i += 1
            a = ta
            continue
    return a

def solve_2():
    # run one turn a // 8, a is  [0-8)
    # run two turn a //8 //8, a is [8-16)
    # result is 2413751503435530, run 16 time, a is [35184372088832,281474976710656)
    for a in range(35184372088832,281474976710656):
        result = solve_1(a)
        if result == "2,4,1,3,7,5,1,5,0,3,4,3,5,5,3,0":
            return a

print(solve_1(47006051))
print(solve_1(6609893682))
a= reverse_run()
print(a)
print(solve_1(a))
