from copy import deepcopy

inf = 99999


def floyd_warshall(n: list) -> list:
    """
    floyd-warshall 求最短路径算法
    :param n: 路径-节点 图
    :return: 最短路径-节点 图
    """
    point = deepcopy(n)
    for k in range(len(point)):
        for i in range(len(point)):
            for j in range(len(point)):
                if point[i][j] > (int(point[i][k]) + int(point[k][j])):
                    point[i][j] = (point[i][k] + point[k][j])

    return point


def dijkstra(n: list) -> dict:
    """
    dijkstra 求最短路径算法
    :param n: 路径-节点 图
    :return: 节点-最短路径 字典
    """
    result = {f'0-{i}': n[0][i] for i in range(len(n))}

    for i in range(len(n)):
        for j in range(len(n)):
            if (n[3][4] != 0 or n[3][4] != inf) and result[f'0-{j}'] > (result[f'0-{i}'] + n[i][j]):
                result[f'0-{j}'] = (result[f'0-{i}'] + n[i][j])

    return result
