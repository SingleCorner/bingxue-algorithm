import sys

def shanyao_level_mod(level):
    return int(level/10)

def shanyao_level_times(level):
    return 0.5 + level * 0.025

def shanyyao_level_requirement(level):
    return shanyao_level_mod(level) * 10000 + 10000

def shanyao_defence_requirement(level):
    return shanyao_level_times(level) * shanyyao_level_requirement(level) / 0.05

def shanyao_level_defence_list(level):
    level_list = [0]
    for i in range(1, level + 1):
        level_list.append(shanyao_defence_requirement(i))
    return level_list

def print_defence_support_level(defence, level_list, index):
  if index <= len(level_list) - 1 and defence > level_list[index]:
    print("闪耀等级升级至", index + 1, "花费", shanyyao_level_requirement(index), "升级完后防御为", round(defence * (shanyao_level_times(index) * 2 + 0.05), 2))
    index = index + 1
    return print_defence_support_level(defence, level_list, index)
  else:
    return index
    

def solution(level):
    shanyao_level_list = shanyao_level_defence_list(level)
    shanyao_level_list_index = 0
    xiangqian_level = 1
    defence = 0
    while True:
        if shanyao_level_list_index > len(shanyao_level_list) - 1:
            break
        for i in range(1, xiangqian_level + 1):
            defence = xiangqian_level * 5 + defence
            if shanyao_level_list_index <= len(shanyao_level_list) - 1 and defence > shanyao_level_list[shanyao_level_list_index]:
              print(" ")
              print("镶嵌等级：", xiangqian_level, "， 镶嵌次数：", i, "， 当前基础防御值：", defence, ", 当前面板防御", round(defence * shanyao_level_times(shanyao_level_list_index) * 2, 2), ", 建议提升闪耀等级")
              shanyao_level_list_index = print_defence_support_level(defence, shanyao_level_list, shanyao_level_list_index)
        xiangqian_level = xiangqian_level + 1

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("防御宝石镶嵌闪耀指南")
        print("使用方法 python3 ", sys.argv[0], "预计闪耀等级, 例如")
        print("python3 ", sys.argv[0], "100")
        print("本工具制作目的：")
        print("  1. 虽然闪耀消耗大，但请跟上")
        print("  2. 帮助你在碎片不足时达到防御最大化")
        print("  3. 如果在临界值，可咬咬牙，凑齐闪耀所需的碎片，同样的碎片加成更多")
        print("  4. 实在无法凑齐，就继续点镶嵌吧")
        print("  5. 碎片充足者，可无视本工具")
        print("  6. 若有bug，可以提出，非bug问题不在交流讨论范围")
    else:
        level = int(sys.argv[1])
        solution(level)
