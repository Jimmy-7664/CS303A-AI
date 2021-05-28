import multiprocessing as mp
import time
import sys
import argparse
import os
import numpy as np
import random


class Node:
    def __init__(self, key):
        self.id = key
        self.connectTo = {}
        self.isconnectedTo = {}
        self.Acitve = False
        self.score = 0
        self.rand = 0
        self.mark = 0

    def addNeighbor(self, nbr, weight):
        self.connectTo[nbr] = weight

    def getConnections(self):
        return self.connectTo.keys()

    def getweight(self, nbr):
        return self.connectTo[nbr]


def Read(args):
    global Nodenum, graph
    graph = {}
    with open(args.file_name) as file:
        contents = file.readline()
        content = contents.split(" ")
        n = content[0]
        Nodenum = n
        m = content[1]
        Nodes = []
        for i in range(int(n) + 1):
            Nodes.append(Node(i))
        for i in range(int(m)):
            contents = file.readline()
            content = contents.split(" ")
            Nodes[int(content[0])].addNeighbor(int(content[1]), float(content[2]))
            graph[Nodes[int(content[0])], Nodes[int(content[1])]] = float(content[2])
    file.close()

    return Nodes


def generateRRS(Nodes, n):
    RRS = set()
    RRS1 = set()
    for i in range(n):
        rand = int(random.randint(1, int(Nodenum)))
        v = Nodes[rand]
        g = graph.copy()
        for k in list(g.keys()):
            if random.random() >= g[k]:
                del g[k]
                continue

        new_nodes, RRS0 = [v], [v]
        while new_nodes:
            # Limit to edges that flow into the source node
            temp = []
            for edge in g:
                if edge[1] in new_nodes:
                    temp.append(edge[0])

            # Extract the nodes flowing into the source node
            # Add new set of in-neighbors to the RRS
            RRS1 = list(set(RRS0 + temp))

            # Find what new nodes were added
            new_nodes = list(set(RRS1) - set(RRS0))

            # Reset loop variables
            RRS0 = RRS1[:]
        RRS.add(tuple(RRS1))
    return set(RRS)


def IMP(Nodes, args):
    RRS = generateRRS(Nodes, 1500)
    SeedSet = set()
    while len(SeedSet) < args.seed:
        t1 = time.time()

        maxnode = Nodes[0]
        maxcount = 0
        for node in Nodes:
            if node in SeedSet:
                continue
            count = 0
            for RR in RRS:
                if RR.__contains__(node):
                    count += 1
            if count >= maxcount:
                maxcount = count
                maxnode = node

        for RR in RRS.copy():
            if RR.__contains__(maxnode):
                RRS.discard(RR)
        SeedSet.add(maxnode)
        t2 = time.time()
        print(t2 - t1)

    for node in SeedSet:
        print(node.id)


if __name__ == '__main__':
    '''
    从命令行读参数示例
    '''
    # t = time.time()
    # print("从命令行读参数示例")
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--file_name', type=str, default='NetHEPT.txt')
    parser.add_argument('-k', '--seed', type=int, default='50')
    parser.add_argument('-m', '--model', type=str, default='IC')
    parser.add_argument('-t', '--time_limit', type=int, default=60)

    args = parser.parse_args()
    file_name = args.file_name
    k = args.seed
    model = args.model
    time_limit = args.time_limit
    Nodes = Read(args)
    IMP(Nodes, args)

    '''
    多进程示例
    '''

    '''
    程序结束后强制退出，跳过垃圾回收时间, 如果没有这个操作会额外需要几秒程序才能完全退出
    '''
    sys.stdout.flush()
