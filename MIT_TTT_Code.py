EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2
DRAW = 3
BOARD_FORMAT = """----------------------------
| {0} | {1} | {2} |
|--------------------------|
| {3} | {4} | {5} |
|--------------------------|
| {6} | {7} | {8} |
----------------------------"""
NAMES = [' ', 'X', 'O']


def printboard(state):
    """ Print the board from the internal state."""
    cells = []
    for i in range(3):
        for j in range(3):
            cells.append(NAMES[state[i][j]].center(6))
    print(BOARD_FORMAT.format(*cells))


# printboard([[1, 2, 0], [0, 1, 0], [2, 0, 0]])
# print(BOARD_FORMAT.format('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'g'))
# print(BOARD_FORMAT.format('x', 'o', 'x', 'o', 'x', ' ', ' ', ' ', ' '))
# print(BOARD_FORMAT.format('x'.center(6), 'o', 'x', 'o', 'x', ' ', ' ', ' ', ' '))
def emptystate():
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]

# state= emptystate()
# printboard(state)

def gameover(state):
    # 가로/세로로 한 줄 완성한 플레이어가 있다면 그 플레이어 리턴
    for i in range(3):
        if state[i][0] != EMPTY and state[i][0] == state[i][1] and state[i][0] == state[i][2]:
            return state[i][0]
        if state[0][i] != EMPTY and state[0][i] == state[1][i] and state[0][i] == state[2][i]:
            return state[0][i]
    # 좌우 대각선
    if state[0][0] != EMPTY and state[0][0] == state[1][1] and state[0][0] == state[2][2]:
        return state[0][0]
    if state[0][2] != EMPTY and state[0][2] == state[1][1] and state[0][2] == state[2][0]:
        return state[0][2]
    # 판이 비었는지
    for i in range(3):
        for j in range(3):
            if state[i][j] == EMPTY:
                return EMPTY
    return DRAW

# state=([[1, 0, 0], [0, 0, 0], [0, 0, 0]])
# state=([[1, 2, 0], [0, 0, 0], [0, 0, 0]])
# state=([[1, 0, 0], [1, 0, 0], [1, 0, 0]])
# state=([[0, 2, 0], [0, 2, 0], [0, 2, 0]])
# print(gameover(state))

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
            return winner
    return winner
if __name__ == "__main__":
    p1 = Human(1)
    p2 = Human(2)
    while True:
        winner = play(p1, p2)
        p1.episode_over(winner)
        p2.episode_over(winner)

