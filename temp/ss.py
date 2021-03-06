# coding=utf-8
import sys
def inRange(point, points_list, points2):
    count = 0
    for points in points_list:
        if point[0] >= points[0] and point[1] >= points[1] and point[0] < points[2] and point[1] < points[3]:
            count += 1

        if points2[0] == points[0] and points2[1] == points[1] and points2[2] == points[2] and points2[3] == points[3]:
            count += 1

    return count


def inRange2(point, points_list, points2):
    count = 0
    for points in points_list:
        if point[0] > points[0] and point[1] > points[1] and point[0] <= points[2] and point[1] <= points[3]:
            count += 1

        if points2[0] == points[0] and points2[1] == points[1] and points2[2] == points[2] and points2[3] == points[3]:
            count += 1

    return count

if __name__ == "__main__":
    # n = int(sys.stdin.readline().strip())
    # x1_list = [int(x) for x in sys.stdin.readline().strip().split()]
    # y1_list = [int(x) for x in sys.stdin.readline().strip().split()]
    # x2_list = [int(x) for x in sys.stdin.readline().strip().split()]
    # y2_list = [int(x) for x in sys.stdin.readline().strip().split()]
    # points_list = []
    # max_area = 1
    # for i in range(n):
    #     points_list.append([x1_list[i], y1_list[i], x2_list[i], y2_list[i]])
    # for points in points_list:
    #     max_area = max(inRange([points[0], points[1]], points_list, points), max_area)
    #     max_area = max(inRange2([points[2], points[3]], points_list, points), max_area)
    # print(max_area)

    import sys

    lines = sys.stdin.readlines()
    n = int(lines[0])
    x1 = list(map(int, lines[1].split()))
    y1 = list(map(int, lines[2].split()))
    x2 = list(map(int, lines[3].split()))
    y2 = list(map(int, lines[4].split()))
    # 遍历所有点的组合（包含了矩形所有角以及交点），看一下有多少矩形包含它
    res = 1
    for x in x1 + x2:
        for y in y1 + y2:
            cnt = 0
            for i in range(n):
                if x > x1[i] and y > y1[i] and x <= x2[i] and y <= y2[i]:
                    cnt += 1
            res = max(res, cnt)
    print(res)