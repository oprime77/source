import csv
import random
from copy import copy, deepcopy

# deepcopy : 메모리를 완전히 새롭게 생성
# copy : 껍데기만 카피, 내용은 동일한 곳을 가리킴
EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2
DRAW = 3
BOARD_FORMAT = "----------------------------\n| {0} | {1} | {2} |\n|--------------------------|\n| {3} | {4} | {5} |\n|--------------------------|\n| {6} | {7} | {8} |\n----------------------------"
NAMES = [' ', 'X', 'O']


# 보드 출력
def printboard(state):
    cells = []
    for i in range(3):
        for j in range(3):
            cells.append(NAMES[state[i][j]].center(6))
    print(BOARD_FORMAT.format(*cells))


# 빈 판
def emptystate():
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def gameover(state):
    # 가로/세로로 한 줄 완성한 플레이어가 있다면 그 플레이어 리턴
    for i in range(3):
        if state[i][0] != EMPTY and state[i][0] == state[i][1] and state[i][0] == state[i][2]:
            printboard(state)
            return state[i][0]
        if state[0][i] != EMPTY and state[0][i] == state[1][i] and state[0][i] == state[2][i]:
            printboard(state)
            return state[0][i]
    # 좌우 대각선
    if state[0][0] != EMPTY and state[0][0] == state[1][1] and state[0][0] == state[2][2]:
        printboard(state)
        return state[0][0]
    if state[0][2] != EMPTY and state[0][2] == state[1][1] and state[0][2] == state[2][0]:
        printboard(state)
        return state[0][2]
    # 판이 비었는지
    for i in range(3):
        for j in range(3):
            if state[i][j] == EMPTY:
                printboard(state)
                return EMPTY
    return DRAW


# 사람
class Human(object):
    def __init__(self, player):
        self.player = player

    # 착수
    def action(self, state):
        printboard(state)
        action = None
        while action not in range(1, 10):
            action = int(input('Your move? '))
        switch_map = {
            1: (0, 0),
            2: (0, 1),
            3: (0, 2),
            4: (1, 0),
            5: (1, 1),
            6: (1, 2),
            7: (2, 0),
            8: (2, 1),
            9: (2, 2)
        }
        return switch_map[action]

    def episode_over(self, winner):
        if winner == DRAW:
            print('Game over! It was a draw.')
        else:
            print('Game over! Winner: Player {0}'.format(winner))


def play(agent1, agent2):
    state = emptystate()
    for i in range(9):
        if i % 2 == 0:
            move = agent1.action(state)
        else:
            move = agent2.action(state)
        state[move[0]][move[1]] = (i % 2) + 1
        winner = gameover(state)
        if winner != EMPTY:
            if winner == 1:
                Fn = ("D:\Test400.csv")
                w = csv.writer(open(Fn, 'a'), delimiter=',',lineterminator='\n')
                w.writerow([state[0][0],
                        state[0][1],
                        state[0][2],
                        state[1][0],
                        state[1][1],
                        state[1][2],
                        state[2][0],
                        state[2][1],
                        state[2][2],
                       winner])
            elif winner == 2:
                Fn = ("D:\Test400.csv")
                w = csv.writer(open(Fn, 'a'), delimiter=',',lineterminator='\n')
                w.writerow([state[0][0],
                            state[0][1],
                            state[0][2],
                            state[1][0],
                            state[1][1],
                            state[1][2],
                            state[2][0],
                            state[2][1],
                            state[2][2],
                           winner])
            else:
                Fn = ("D:\Test400.csv")
                w = csv.writer(open(Fn, 'a'), delimiter=',',lineterminator='\n')
                w.writerow([state[0][0],
                            state[0][1],
                            state[0][2],
                            state[1][0],
                            state[1][1],
                            state[1][2],
                            state[2][0],
                            state[2][1],
                            state[2][2],
                            'DRAW'])
            return winner
    return winner


class Computer(object):
    def __init__(self, player):
        self.player = player

    def random(self, state):
        available = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == EMPTY:
                    available.append((i, j))
        return random.choice(available)

    # 컴퓨터가 착수
    def action(self, state):
        printboard(state)
        action = None
        move = self.random(state)
        state[move[0]][move[1]] = self.player
        return move

    def episode_over(self, winner):
        if winner == DRAW:
            print('Game over! It was a draw.')
        else:
            print('Game over! Winner: Player {0}'.format(winner))


def main(stopfight):
    num=0
    p1 = Computer(1)
    p2 = Computer(2)
    while stopfight > num:
        winner = play(p1, p2)
        p1.episode_over(winner)
        p2.episode_over(winner)
        num+=1
        print('{0}회 게임하였습니다'.format(num))

main(100000)
