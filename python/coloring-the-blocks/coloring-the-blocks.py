import copy
import sys


def best_color(i, c):
    return min(range(len(c[i])), key=c[i].__getitem__)


def is_safe_color(color, idx, blocks):
    return True


def set_weights(costs, i, color):
    if i-1 >= 0:
        costs[i-1][color] = sys.maxsize
    if i+1 < len(costs):
        costs[i+1][color] = sys.maxsize


def color_block(i, costs, blocks):
    color = best_color(i, costs)
    blocks[i] = costs[i][color]
    set_weights(costs, i, color)


def color_blocks(start, costs):
    costs_copy = copy.deepcopy(costs)
    blocks = [0 for _ in costs]
    # this is a stupid algorithm because it assesses each block sequentially. A
    # better algorithm would find the best picks among all of the available
    # costs and then find a way to make those best picks work.
    # forward
    i = start
    while i < len(blocks):
        color_block(i, costs_copy, blocks)
        i += 1
    # backward
    i = start - 1
    while i >= 0:
        color_block(i, costs_copy, blocks)
        i -= 1
    return sum(blocks)


def minCost(costs):
    sums = []
    for i in range(len(costs)):
        sums.append(color_blocks(i, costs))
    return min(sums)


if __name__ == '__main__':
    # example - expected: 4
    cost = [
        [1, 2, 3],
        [1, 2, 3],
        [3, 3, 1],
    ]
    # forward, then backward - expected: 273
    # cost = [
    #     [49, 73, 58],
    #     [30, 72, 44],
    #     [78, 23, 9],
    #     [40, 65, 92],
    #     [42, 87, 3],
    #     [27, 29, 40],
    #     [12, 3, 69],
    #     [9, 57, 60],
    #     [33, 99, 78],
    #     [16, 35, 97],
    # ]
    # weighted minimums - expected 427 (doesn't work)
    # cost = [
    #     [12, 67, 10],
    #     [33, 79, 49],
    #     [79, 21, 67],
    #     [72, 93, 36],
    #     [85, 45, 28],
    #     [91, 94, 57],
    #     [1, 53, 8],
    #     [44, 68, 90],
    #     [24, 96, 30],
    #     [3, 22, 66],
    #     [49, 24, 1],
    #     [53, 77, 8],
    #     [28, 33, 98],
    #     [81, 35, 13],
    #     [65, 14, 63],
    #     [36, 25, 69],
    # ]
    # sample 1 - expected: 3
    # cost = [
    #     [1, 2, 2],
    #     [2, 2, 1],
    #     [2, 1, 2],
    # ]
    # sample 2 - expected: 3
    # cost = [
    #     [1, 2, 2],
    #     [2, 3, 3],
    #     [3, 3, 1],
    # ]
    print(minCost(cost))
