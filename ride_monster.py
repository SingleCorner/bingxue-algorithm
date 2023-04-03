import sys
import math

def current_level_requirement(level):
    current_requirement_per_level = level / 10
    current_level_total = 0
    for i in range(0, level):
        if level == 240 and i == 239:
            print("level：", level , " 当前次数： ", i," 坐骑已满")
        else:
            current_level_total = current_level_total + (i + 1) * current_requirement_per_level
            print("level：", level , " 当前次数： ", i," 鞭子需求：", (i + 1) * current_requirement_per_level, " total：", current_level_total)
    return current_level_total

def calculate_level_total(start_level, end_level):
    total = 0
    for i in range(start_level, end_level + 10, 10):
        total = total + current_level_requirement(i)
    return total

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("坐骑碎片计算器")
        print("使用方法 python3 ", sys.argv[0], "坐骑当前等级需求 坐骑结束等级需求（不朽240）")
        print("例如 python3 ", sys.argv[0], "200 240")
    else:
        start_level = int(sys.argv[1])
        end_level = int(sys.argv[2])
        total = calculate_level_total(start_level, end_level)
        print("坐骑当前等级需求：", start_level, "坐骑结束等级需求：", end_level, "鞭子需求：", total, "战令需求：", math.ceil(total / 3 / 5) * 5)