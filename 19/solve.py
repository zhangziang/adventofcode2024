import math
from multiprocessing.process import current_process
from socket import has_ipv6
from tarfile import TarInfo
from typing import List, Dict, Tuple


class TairNode:
    def __init__(self, val: str) -> None:
        self.val = val
        self.sub_node = {}
        self.can_end = False

    def addSubNode(self, sub_node):
        self.sub_node[sub_node.val] = sub_node

    def log(self):
        if self.can_end:
            print(f"{self.val}▼")
        else:
            print(self.val)
        print(self.sub_node.keys())
        for i in self.sub_node:
            self.sub_node[i].log()


def construct_tair(all):
    start_node = TairNode("")
    for i in all:
        cur_node = start_node
        for w in i:
            if w in cur_node.sub_node:
                cur_node = cur_node.sub_node[w]
            else:
                new_node = TairNode(w)
                cur_node.addSubNode(new_node)
                cur_node = new_node
        cur_node.can_end = True

    return start_node


def match(target: str, tair: TairNode, i: int, fast_fail: Dict[int, bool]) -> bool:
    if i in fast_fail:
        return False
    if len(target) == 0:
        return True
    w = target[i]
    if w not in tair.sub_node:
        return False
    cur_node = tair.sub_node[w]
    while True:
        if cur_node.can_end:
            if i == len(target) - 1:
                return True
            # to next match
            if match(target, tair, i + 1, fast_fail):
                return True
            else:
                fast_fail[i + 1] = True
            # dont match, go next
        if i == len(target) - 1:
            return False
        i = i + 1
        w = target[i]
        if w not in cur_node.sub_node:
            return False
        cur_node = cur_node.sub_node[w]


def match_count(
    target: str,
    tair: TairNode,
    i: int,
    fast_fail: Dict[int, bool],
    success_count: Dict[int, int],
) -> Tuple[bool, int]:
    if i in fast_fail:
        return False, 0
    if i in success_count:
        return True, success_count[i]
    if len(target) == 0:  # 应该走不到这里
        return True, 1
    count = 0
    has_matched = False
    cur_node = tair
    while True:
        w = target[i]
        if w not in cur_node.sub_node:
            return has_matched, count
        cur_node = cur_node.sub_node[w]
        if cur_node.can_end:
            if i == len(target) - 1:
                count = count + 1
                has_matched = True
                return True, count
            else:  # to next match
                matched, new_count = match_count(
                    target, tair, i + 1, fast_fail, success_count
                )
                if matched:
                    count = new_count + count
                    has_matched = True
                    success_count[i + 1] = new_count
                else:
                    fast_fail[i + 1] = True
        if i == len(target) - 1:
            return has_matched, count
        # 不管是否已经匹配到了，都继续用下一位做继续匹配
        i = i + 1


def sample():
    all = "r, wr, b, g, bwu, rb, gb, br"
    p = ["brwrr", "bggr", "gbbr", "rrbgbr", "ubwu", "bwurrg", "brgr", "bbrgwb"]
    tair = construct_tair(all.split(", "))
    for i in p:
        m = match(i, tair, 0, {})
        print(f"{i} -> {m}")


def sample_2():
    all = "r, wr, b, g, bwu, rb, gb, br"
    p = ["brwrr", "bggr", "gbbr", "rrbgbr", "ubwu", "bwurrg", "brgr", "bbrgwb"]
    tair = construct_tair(all.split(", "))
    for i in p:
        m = match_count(i, tair, 0, {}, {})
        print(f"{i} -> {m}")


def solve_1():
    with open("input") as f:
        tair = construct_tair(f.readline().strip().split(", "))
        f.readline()  # jump empty line
        c = 0
        for i in f:
            m = match(i.strip(), tair, 0, {})
            if m:
                c += 1
        print(c)


def solve_2():
    with open("input") as f:
        tair = construct_tair(f.readline().strip().split(", "))
        f.readline()  # jump empty line
        c = 0
        for i in f:
            m, count = match_count(i.strip(), tair, 0, {}, {})
            if m:
                c += count
        print(c)


sample()
solve_1()
sample_2()
solve_2()
