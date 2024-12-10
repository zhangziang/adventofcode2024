# coding: utf-8

import sys

def cal_one(one, two):
    one.sort()
    two.sort()
    result = 0
    for i in range(len(one)):
        result += abs(one[i]-two[i])
    return result

def cal_two(one, two):
    two_count = {}
    for item in two:
        if item in two_count:
            two_count[item] += 1
        else:
            two_count[item] = 1
    result = 0
    for item in one:
        if item in two_count:
            result += item * two_count[item]
    return result

if __name__ == "__main__":
    one = []
    two = []
    for line in open("1_input"):
        lines = line.split()
        one.append(int(lines[0]))
        two.append(int(lines[1]))
    print(cal_one(one,two))
    print(cal_two(one,two))