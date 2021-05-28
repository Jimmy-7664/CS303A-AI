import numpy as np
import random
import math
import time
from datetime import datetime, date
import functools

# values = [[100, -5, 10, 5, 5, 10, -5, 100],
#           [-5, -45, 1, 1, 1, 1, -45, -5],
#           [10, 1, 3, 2, 2, 3, 1, 10],
#           [5, 1, 2, 1, 1, 2, 1, 5],
#           [5, 1, 2, 1, 1, 2, 1, 5],
#           [10, 1, 3, 2, 2, 3, 1, 10],
#           [-5, -45, 1, 1, 1, 1, -45, -5],
#           [100, -5, 10, 5, 5, 10, -5, 100]
#           ]

xdirection = [-1, -1, 0, 1, 1, 1, 0, -1]
ydirection = [0, 1, 1, 1, 0, -1, -1, -1]
COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0


# values = np.array([[500, -25, 10, 5, 5, 10, -25, 500],
#                    [-25, -45, 1, 1, 1, 1, -45, -25],
#                    [10, 1, 3, 2, 2, 3, 1, 10],
#                    [5, 1, 2, 1, 1, 2, 1, 5],
#                    [5, 1, 2, 1, 1, 2, 1, 5],
#                    [10, 1, 3, 2, 2, 3, 1, 10],
#                    [-25, -45, 1, 1, 1, 1, -45, -25],
#                    [500, -25, 10, 5, 5, 10, -25, 500]])


# values = np.array([90, -60, 10, 10, 10, 10, -60, 90],
#                   [2, -60, -80, 5, 5, 5, 5, -80, -60],
#                   [3, 10, 5, 1, 1, 1, 1, 5, 10],
#                   [4, 10, 5, 1, 1, 1, 1, 5, 10],
#                   [5, 10, 5, 1, 1, 1, 1, 5, 10],
#                   [6, 10, 5, 1, 1, 1, 1, 5, 10],
#                   [7, -60, -80, 5, 5, 5, 5, -80, -60],
#                   [8, 90, -60, 10, 10, 1010, -60, 90])


# values = [[80, -20, 8, 6, 6, 8, -20, 80],
#           [-20, -20, 0, -1, -1, 0, -20, -20],
#           [8, 0, 3, 5, 5, 3, 0, 8],
#           [6, -1, 5, 1, 1, 5, -1, 6],
#           [6, -1, 5, 1, 1, 5, -1, 6],
#           [8, 0, 3, 5, 5, 3, 0, 8],
#           [-20, -20, 0, -1, -1, 0, -20, -20],
#           [80, -20, 8, 6, 6, 8, -20, 80]
#           ]

def cmp(a, b):
    if b[0] == a[0]:
        if a[1] < b[1]:
            return -1
        else:
            return 1
    if a[0] < b[0]:
        return 1
    else:
        return -1


# don't change the class name
class AI(object):
    # chessboard_size, color, time_out passed from agent
    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
        # You are white or black
        self.values1 = [[100, -5, 10, 5, 5, 10, -5, 100],
                        [-5, -45, 1, 1, 1, 1, -45, -5],
                        [10, 1, 3, 2, 2, 3, 1, 10],
                        [5, 1, 2, 1, 1, 2, 1, 5],
                        [5, 1, 2, 1, 1, 2, 1, 5],
                        [10, 1, 3, 2, 2, 3, 1, 10],
                        [-5, -45, 1, 1, 1, 1, -45, -5],
                        [100, -5, 10, 5, 5, 10, -5, 100]
                        ]
        self.values2 = [[80, -20, 8, 6, 6, 8, -20, 80],
                        [-20, -20, 0, -1, -1, 0, -20, -20],
                        [8, 0, 3, 5, 5, 3, 0, 8],
                        [6, -1, 5, 1, 1, 5, -1, 6],
                        [6, -1, 5, 1, 1, 5, -1, 6],
                        [8, 0, 3, 5, 5, 3, 0, 8],
                        [-20, -20, 0, -1, -1, 0, -20, -20],
                        [80, -20, 8, 6, 6, 8, -20, 80]
                        ]
        self.values3 = np.array([[500, -25, 10, 5, 5, 10, -25, 500],
                                 [-25, -45, 1, 1, 1, 1, -45, -25],
                                 [10, 1, 3, 2, 2, 3, 1, 10],
                                 [5, 1, 2, 1, 1, 2, 1, 5],
                                 [5, 1, 2, 1, 1, 2, 1, 5],
                                 [10, 1, 3, 2, 2, 3, 1, 10],
                                 [-25, -45, 1, 1, 1, 1, -45, -25],
                                 [500, -25, 10, 5, 5, 10, -25, 500]])
        self.values4 = np.array([[500, 5, 25, 15, 15, 25, 5, 500],
                                 [5, -100, 1, 1, 1, 1, -100, 5],
                                 [25, 1, 3, 2, 2, 3, 1, 25],
                                 [15, 1, 2, 1, 1, 2, 1, 15],
                                 [15, 1, 2, 1, 1, 2, 1, 15],
                                 [25, 1, 3, 2, 2, 3, 1, 25],
                                 [5, -100, 1, 1, 1, 1, -100, 5],
                                 [500, 5, 25, 15, 15, 25, 5, 500]])
        self.values5 = np.array([[500, 20, 25, 15, 15, 25, 20, 500],
                                 [20, -120, 1, 1, 1, 1, -120, 20],
                                 [25, 1, 3, 2, 2, 3, 1, 25],
                                 [15, 1, 2, 1, 1, 2, 1, 15],
                                 [15, 1, 2, 1, 1, 2, 1, 15],
                                 [25, 1, 3, 2, 2, 3, 1, 25],
                                 [20, -120, 1, 1, 1, 1, -120, 20],
                                 [500, 20, 25, 15, 15, 25, 20, 500]])
        self.color = color
        self.values = self.values4
        self.const_int = 500
        # if self.color==COLOR_BLACK:
        #     self.values=self.values1
        # the max time you should use, your algorithm's run time must not exceed the time limit.
        self.time_out = time_out
        # You need add your decision into your candidate_list. System will get the end of your candidate_list as yourision .
        self.candidate_list = []
        self.movable_list = []
        if self.color == COLOR_BLACK:
            self.count = 62
        else:
            self.count = 61

    # The input is current chessboard.
    def go(self, chessboard):
        # Clear candidate_list, must do this step
        self.count -= 2
        self.candidate_list.clear()
        # ==================================================================
        # Write your algorithm here
        # Here is the simplest sample:Random decision
        # a = datetime.now()  # 闁兼儳鍢茬欢杈亹閹惧啿顤呴柡鍐ㄧ埣濡拷
        self.movable_list = self.movable(chessboard, self.color)
        for k in self.movable_list:
            self.candidate_list.append(k)
        # if len(np.where(chessboard == 0) < 10 and len(self.movable_list) != 0):
        #     self.FinalCal(chessboard, self.color)
        if len(self.movable_list) != 0:
            self.candidate_list.append(self.movable_list[0])
            if self.count < 14:
                self.MinMax(chessboard, 7, -9999999, 9999999)
            else:
                self.MinMax(chessboard, 5, -9999999, 9999999)
            if self.candidate_list[-1] == (0, 0):
                self.values[1][1] += 200
            if self.candidate_list[-1] == (7, 0):
                self.values[6][1] += 200
            if self.candidate_list[-1] == (7, 7):
                self.values[6][6] += 200
            if self.candidate_list[-1] == (0, 7):
                self.values[1][6] += 200
        # b = datetime.now()  # 闁兼儳鍢茶ぐ鍥亹閹惧啿顤呴柡鍐ㄧ埣濡拷
        # durn = (b - a).total_seconds()  # 濞戞挶鍊撻柌婊堝籍閸洘锛熺€瑰壊鍣槐婵嬬嵁閺堝吀绨扮紒澶嬪笚濡绮堥崫鍕瘔闁哄鎷�
        # if durn <= 3 and self.count <= 8:
        #     time.sleep(3)

    # def FinalMinMax(self, chessboard, color):
    #     temp_move_list = self.movable(chessboard, color)
    #     if len(temp_move_list) == 0:
    #         if len(self.movable(chessboard, -color)) == 0:
    #             return self.calculatevalue3(chessboard)
    #         return self.FinalCal(chessboard, -color)
    #
    #     for move in temp_move_list:
    #         chessboard, relist = self.Move(chessboard, move, color)
    #         val = self.FinalCal(chessboard, -self.color)
    #         chessboard = self.Moveback(chessboard, -self.color, relist)
    #         if val == 9999999:
    #             self.candidate_list[-1] = move
    #             return val
    #
    # # def FinalCal(self, chessboard, color):
    # #     for
    # def calculatevalue3(self, chessboard):
    #     mlen = len(np.where(chessboard == self.color))
    #     ylen = len(np.where(chessboard == -self.color))
    #     if mlen > ylen:
    #         return 9999999
    #     return mlen

    def Move(self, chessboard, move, color):
        chessboard[move[0]][move[1]] = color
        rvlist = [move]
        for m in range(8):
            newx = move[0] + xdirection[m]
            newy = move[1] + ydirection[m]
            if 0 <= newx <= 7 and 0 <= newy <= 7 and chessboard[newx][newy] == -color:
                while 0 <= newx <= 7 and 0 <= newy <= 7 and chessboard[newx][newy] == -color:
                    newx += xdirection[m]
                    newy += ydirection[m]
                if 0 <= newx <= 7 and 0 <= newy <= 7 and chessboard[newx][newy] == color:
                    newxx = move[0] + xdirection[m]
                    newyy = move[1] + ydirection[m]
                    while 0 <= newxx <= 7 and 0 <= newyy <= 7 and chessboard[newxx][newyy] == -color:
                        chessboard[newxx][newyy] = color
                        rvlist.append((newxx, newyy))
                        newxx += xdirection[m]
                        newyy += ydirection[m]

        return chessboard, rvlist

    def movable(self, chessboard, color):
        weight_list = []
        idx = np.where(chessboard == COLOR_NONE)
        idx = list(zip(idx[0], idx[1]))
        temp_movable_list = []

        for i in range(len(idx)):
            for k in range(8):
                tempx = idx[i][0] + xdirection[k]
                tempy = idx[i][1] + ydirection[k]
                if (tempx < 0 or tempx > 7) or (tempy < 0 or tempy > 7):
                    continue
                if chessboard[tempx][tempy] == 0:
                    continue
                if chessboard[tempx][tempy] != color:
                    while tempx >= 0 and tempy >= 0 and tempx <= 7 and tempy <= 7 and chessboard[tempx][tempy] != 0 and \
                            chessboard[tempx][tempy] != color:
                        tempx += xdirection[k]
                        tempy += ydirection[k]
                    if tempx < 0 or tempy > 7 or tempy < 0 or tempx > 7:
                        continue
                    if chessboard[tempx][tempy] == color:
                        temp_movable_list.append((idx[i][0], idx[i][1]))
                        weight_list.append(self.values[idx[i][0]][idx[i][1]])
                        break

        if len(temp_movable_list) != 0:
            weight_list, temp_movable_list = zip(
                *sorted(list(zip(weight_list, temp_movable_list)), key=functools.cmp_to_key(cmp)))
        return temp_movable_list

    def calculatevalue(self, chessboard, cap, relen=0):
        blank = len(np.where(chessboard == COLOR_NONE))
        stabl = 0
        current_value = 0
        if blank > 50:
            current_value = cap * 10 + 2 * relen
        elif blank > 20:
            current_value = cap * 20 + relen
        else:
            current_value = cap * 10 + 6 * relen
        for i in range(8):
            for j in range(8):
                if self.color == chessboard[i][j]:
                    current_value += self.values[i][j]
                elif self.color == -chessboard[i][j]:
                    current_value -= self.values[i][j]
        st = self.stable(chessboard)
        if chessboard[0][7] != 0 or chessboard[0][0] != 0 or chessboard[7][0] != 0 or chessboard[7][7] != 0:
            stabl += st*2
        current_value += 10 * stabl
        return current_value

    def stable(self, chessboard):
        stablenum = 0
        if chessboard[0][0] == self.color:
            stablenum += 1
            i = 1
            while i <= 7 and chessboard[0][i] == self.color:
                stablenum += 1
                i += 1
            i = 1
            while i <= 7 and chessboard[i][0] == self.color:
                stablenum += 1
                i += 1
        elif chessboard[0][0] == -self.color:
            stablenum -= 1
            i = 1
            while i <= 7 and chessboard[0][i] == -self.color:
                stablenum -= 1
                i += 1
            i = 1
            while i <= 7 and chessboard[i][0] == -self.color:
                stablenum -= 1
                i += 1
        if chessboard[7][0] == self.color:
            stablenum += 1
            i = 1
            while i <= 7 and chessboard[7][i] == self.color:
                stablenum += 1
                i += 1
            i = 6
            while i >= 0 and chessboard[i][0] == self.color:
                stablenum += 1
                i -= 1
        elif chessboard[7][0] == -self.color:
            stablenum -= 1
            i = 1
            while i <= 7 and chessboard[7][i] == -self.color:
                stablenum -= 1
                i += 1
            i = 6
            while i >= 0 and chessboard[i][0] == -self.color:
                stablenum -= 1
                i -= 1
        if chessboard[0][7] == self.color:
            stablenum += 1
            i = 1
            while i <= 7 and chessboard[i][7] == self.color:
                stablenum += 1
                i += 1
            i = 6
            while i >= 0 and chessboard[0][i] == self.color:
                stablenum += 1
                i -= 1
        elif chessboard[0][7] == -self.color:
            stablenum -= 1
            i = 1
            while i <= 7 and chessboard[i][7] == -self.color:
                stablenum -= 1
                i += 1
            i = 6
            while i >= 0 and chessboard[0][i] == -self.color:
                stablenum -= 1
                i -= 1
        if chessboard[7][7] == self.color:
            stablenum += 1
            i = 6
            while i >= 0 and chessboard[7][i] == self.color:
                stablenum += 1
                i -= 1
            i = 6
            while i >= 0 and chessboard[i][7] == self.color:
                stablenum += 1
                i -= 1
        elif chessboard[7][7] == -self.color:
            stablenum -= 1
            i = 6
            while i >= 0 and chessboard[7][i] == -self.color:
                stablenum -= 1
                i -= 1
            i = 6
            while i >= 0 and chessboard[i][7] == -self.color:
                stablenum -= 1
                i -= 1
        return stablenum

    def calculatevalue2(self, chessboard, color):
        mlen = len(np.where(chessboard == self.color)[1])
        ylen = len(np.where(chessboard == -self.color)[1])

        if mlen > ylen:
            if color == self.color:
                return 999999
            if color == -self.color:
                return -999999
        return mlen

    def Min(self, chessboard, depth, alp, beta, relen=0):
        min_val = 99999
        temp_move_list = self.movable(chessboard, -self.color)
        if depth <= 0:
            return self.calculatevalue(chessboard, -len(temp_move_list), -relen)
        if len(temp_move_list) == 0:
            if len(self.movable(chessboard, self.color)) == 0:
                return self.calculatevalue2(chessboard, self.color)
            return self.Max(chessboard, depth, alp, beta)
        for move in temp_move_list:
            chessboard, relist = self.Move(chessboard, move, -self.color)
            val = self.Max(chessboard, depth - 1, alp, beta, len(relist))
            chessboard = self.Moveback(chessboard, self.color, relist)
            min_val = min(min_val, val)
            if val == -999999:
                return val
            if val <= alp:
                return val
            beta = min(beta, val)
        return min_val

    def Max(self, chessboard, depth, alp, beta, relen=0):
        max_val = -99999
        temp_move_list = self.movable(chessboard, self.color)
        if depth <= 0:
            return self.calculatevalue(chessboard, len(temp_move_list), relen)
        if len(temp_move_list) == 0:
            if len(self.movable(chessboard, -self.color)) == 0:
                return self.calculatevalue2(chessboard, -self.color)
            return self.Min(chessboard, depth, alp, beta)
        for move in temp_move_list:
            chessboard, relist = self.Move(chessboard, move, self.color)
            val = self.Min(chessboard, depth - 1, alp, beta, len(relist))
            chessboard = self.Moveback(chessboard, -self.color, relist)
            max_val = max(max_val, val)
            if val == 999999:
                return val
            if val >= beta:
                return val
            alp = max(alp, val)
        return max_val

    def MinMax(self, chessboard, depth, alp, beta):
        best_value = -999999
        for move in self.movable_list:
            chessboard, relist = self.Move(chessboard, move, self.color)
            val = self.Min(chessboard, depth - 1, alp, beta)
            chessboard = self.Moveback(chessboard, -self.color, relist)
            if val == 999999:
                self.candidate_list[-1] = move
                return
            if val > best_value:
                best_value = val
                self.candidate_list[-1] = move
        return

    # def AlpBeta(self, chessboard, color, alp, beta, depth):
    #     temp_move_list = self.movable(chessboard, color)
    #
    #     if depth <= 0:
    #         return self.calculatevalue(chessboard, len(temp_move_list))
    #     best_move = None
    #     if len(temp_move_list) == 0:
    #         if len(self.movable(chessboard, -color)) == 0:
    #             return self.calculatevalue(chessboard, 0)
    #         return -self.AlpBeta(chessboard, -color, -beta, -alp, depth)
    #     for move in temp_move_list:
    #         chessboard, rvlist = self.Move(chessboard, move, color)
    #         val = -self.AlpBeta(chessboard, -color, -beta, -alp, depth - 1)
    #         chessboard = self.Moveback(chessboard, -color, rvlist)
    #         if val >= beta:
    #             return beta
    #         if val > alp:
    #             alp = val
    #             best_move = move
    #     if depth == 6:
    #         self.candidate_list[-1] = best_move
    #     return alp

    def Moveback(self, chessboard, color, rvlist):

        for k in rvlist:
            if k == rvlist[0]:
                chessboard[k[0]][k[1]] = 0
            else:
                chessboard[k[0]][k[1]] = color
        return chessboard

# ==============Find new pos========================================
# Make sure that the position of your decision in chess board is empty.
# If not, the system will return error.
# Add your decision into candidate_list, Records the chess board
# You need add all the positions which is valid
# candidate_list example: [(3,3),(4,4)]
# You need append your decision at the end of the candidate_list,
# we will choose the last element of the candidate_list as the position you choose
# If there is no valid position, you must return a empty list.


# a_time = datetime.now()
# board = np.array(
#     [[0, 1, -1, 0, 0, 0, -1, 0],
#      [-1, 0, 1, -1, 0, -1, 0, -1],
#      [-1, -1, -1, 1, -1, -1, -1, -1],
#      [-1, -1, -1, -1, -1, -1, -1, -1],
#      [-1, -1, -1, -1, -1, -1, -1, -1],
#      [-1, -1, -1, -1, -1, -1, -1, -1],
#      [0, 0, -1, 0, 0, 0, 0, -1],
#      [0, 0, 0, 0, 0, 0, 0, 0], ]
#
# )
# ai = AI(8, -1, 100)
# ai.go(board)
# print(ai.candidate_list)
# b_time = datetime.now()  # 閼惧嘲褰囪ぐ鎾冲閺冨爼妫�
# durn = (b_time - a_time).total_seconds()  # 娑撱倓閲滈弮鍫曟？瀹割噯绱濋獮鏈典簰缁夋帗妯夌粈鍝勫毉閺夛拷
# print(durn)