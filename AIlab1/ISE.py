# -*- coding: utf-8 -*-
# written by mark zeng 2018-11-14
# modified by Yao Zhao 2019-10-30
# re-modified by Yiming Chen 2020-11-04

import multiprocessing as mp
import time
import sys
import argparse
import os
import numpy as np
import random

core = 8


class Node:
    def __init__(self, key):
        self.id = key
        self.connectTo = {}
        self.Acitve = False
        self.score = 0
        self.rand = 0

    def addNeighbor(self, nbr, weight):
        self.connectTo[nbr] = weight

    def getConnections(self):
        return self.connectTo.keys()

    def getweight(self, nbr):
        return self.connectTo[nbr]


def IC(args, t):
    with open(args.file_name) as file:
        contents = file.readline()
        content = contents.split(" ")
        n = content[0]
        m = content[1]
        Nodes = []
        for i in range(int(n) + 1):
            Nodes.append(Node(i))
        for i in range(int(m)):
            contents = file.readline()
            content = contents.split(" ")
            # print(content)
            Nodes[int(content[0])].addNeighbor(int(content[1]), float(content[2]))
    file.close()
    # print(Nodes[20].getConnections())
    ActiveSet = set()
    with open(args.seed) as file:
        contents = file.readline()
        Nodes[int(contents)].Acitve = True
        ActiveSet.add(Nodes[int(contents)])
        while True:
            contents = file.readline()
            if contents != '':
                ActiveSet.add(Nodes[int(contents)])
            else:
                break
    file.close()
    startSet = ActiveSet
    totalcount = 0

    # N = 1000
    # for i in range(N):
    N = 0
    while True:
        ActiveSet = startSet
        for node in Nodes:
            node.Acitve = False
        for node in ActiveSet:
            node.Acitve = True
        count = len(ActiveSet)
        while (len(ActiveSet) != 0):
            newActiveSet = set()
            for seed in ActiveSet:
                neighbor = seed.getConnections()
                for index in neighbor:
                    if Nodes[index].Acitve:
                        continue
                    else:
                        rand = random.random()
                        if rand <= seed.getweight(index):
                            Nodes[index].Acitve = True
                            newActiveSet.add(Nodes[index])
            count += len(newActiveSet)
            ActiveSet = newActiveSet
        totalcount += count
        # print(count)
        N += 1
        t1 = time.time()
        if (t1 - t + 5) >= args.time_limit:
            break
    return totalcount / N


def LT(args, t):
    with open(args.file_name) as file:
        contents = file.readline()
        content = contents.split(" ")
        n = content[0]
        m = content[1]
        Nodes = []
        for i in range(int(n) + 1):
            Nodes.append(Node(i))
        for i in range(int(m)):
            contents = file.readline()
            content = contents.split(" ")
            # print(content)
            Nodes[int(content[0])].addNeighbor(int(content[1]), float(content[2]))
    file.close()
    # print(Nodes[20].getConnections())
    ActiveSet = set()
    with open(args.seed) as file:
        contents = file.readline()
        Nodes[int(contents)].Acitve = True
        ActiveSet.add(Nodes[int(contents)])
        while True:
            contents = file.readline()
            if contents != '':
                ActiveSet.add(Nodes[int(contents)])
            else:
                break
    file.close()
    startSet = ActiveSet
    totalcount = 0
    N = 0
    # N=1000
    # for i in range(N):
    while True:
        ActiveSet = startSet
        for node in Nodes:
            node.Acitve = False
            node.rand = random.random()
            node.score = 0
        for node in ActiveSet:
            node.Acitve = True
        count = len(ActiveSet)
        while (len(ActiveSet) != 0):
            newActiveSet = set()
            for seed in ActiveSet:
                neighbor = seed.getConnections()
                for index in neighbor:

                    if Nodes[index].Acitve:
                        continue
                    else:
                        Nodes[index].score += seed.getweight(index)
                        if Nodes[index].rand <= Nodes[index].score:
                            Nodes[index].Acitve = True
                            newActiveSet.add(Nodes[index])
            count += len(newActiveSet)
            ActiveSet = newActiveSet
        # print(count)
        totalcount += count
        N += 1
        t1 = time.time()
        if (t1 - t + 5) >= args.time_limit:
            break
        # print(count)
    return totalcount / N


if __name__ == '__main__':
    '''
    从命令行读参数示例
    '''
    t = time.time()
    # print("从命令行读参数示例")
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--file_name', type=str, default='network.txt')
    parser.add_argument('-s', '--seed', type=str, default='seeds.txt')
    parser.add_argument('-m', '--model', type=str, default='IC')
    parser.add_argument('-t', '--time_limit', type=int, default=60)

    args = parser.parse_args()
    file_name = args.file_name
    seed = args.seed
    model = args.model
    time_limit = args.time_limit

    # if args.model == 'IC':
    #     print(IC(args, t))
    # else:
    #     print(LT(args, t))

    '''
    多进程示例
    '''
    # print("多进程示例")
    # np.random.seed(0)
    # pool = mp.Pool(core)
    # result = []
    #
    # for i in range(core):
    #     result.append(pool.apply(IC, args=(args,t)))
    # pool.close()
    # pool.join()
    # total=0
    # print(result)
    # for i in range(core):
    #     total+=result[i]
    # print(total/8)

    '''
    程序结束后强制退出，跳过垃圾回收时间, 如果没有这个操作会额外需要几秒程序才能完全退出
    '''
    sys.stdout.flush()

