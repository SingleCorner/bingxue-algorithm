import sys

def xiangqian_total(level):
    total = 0
    for i in range(1, level + 1):
        total += 10 * i ** 2
    return total


def cacl_shanyao_level(total):
    level = 0
    while True:
        if level > 100:
            break
        if (1000 * level / 0.05) < (total * (1 + 0.05 * level)):
            print("======")
            print((1000 * level / 0.05))
            print(total * (1 + 0.05 * level))
            level += 1
        else:
            return level


chips = xiangqian_total(100)

print(chips)

cacl_shanyao_level(chips)