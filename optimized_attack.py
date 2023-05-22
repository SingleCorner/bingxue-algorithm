import sys

def base_chip_requirement(level):
    total = 0
    for i in range(1,level):
        total += i ** 2 * 10
    return total

def base_value_total(level):
    return base_chip_requirement(level) * 1.5

def actual_value_total(level):
    return base_value_total(level) * (1 + 0.05 * level)

def calc_target_level(level):
    additional = base_value_total(level) * 0.05
    sy_level = 0
    while True:
        sy_level += 1
        sy_chip_requirement = sy_level * 1000
        if sy_chip_requirement * (1 + 0.05 * sy_level) * 1.5 >= additional:
            break
    return sy_level


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python optimized_attack.py <level>')
        sys.exit(1)
    level = int(sys.argv[1])
    print('Sy level: %d' % calc_target_level(level))