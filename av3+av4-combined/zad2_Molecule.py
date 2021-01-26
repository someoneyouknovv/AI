from SearchProblems.utils import *
from SearchProblems.uninformed_search import breadth_first_graph_search
from SearchProblems.informed_search import astar_search

def moveRight(x,y, a,b,c,d, obstacles):
    while x + 1 < 8 and [x+1,y] != [a,b] and [x+1,y] != [c,d] and [x+1,y] not in obstacles:
        x+=1
    return x+1, y

def moveLeft(x,y, a,b,c,d, obstacles):
    while x - 1 > 0 and [x-1,y] != [a,b] and [x-1,y] != [c,d] and [x-1,y] not in obstacles:
        x-=1
    return x-1, y

def moveUp(x,y, a,b,c,d, obstacles):
    while y + 1 < 6 and [x,y+1] != [a,b] and [x,y+1] != [c,d] and [x,y+1] not in obstacles:
        y+=1
    return x, y+1

def moveDown(x,y, a,b,c,d, obstacles):
    while y - 1 < 0 and [x,y-1] != [a,b] and [x,y-1] != [c,d] and [x,y-1] not in obstacles:
        y-=1
    return x, y-1

class Molecule(Problem):

    def __init__(self,obstacles, initial, goal=None):
        super().__init__(initial, goal)
        self.gridX = 8
        self.gridY = 7
        self.obstacles = obstacles

    def successor(self, state):
        successors = dict()
        h1X, h1Y = state[0], state[1]
        oX, oY = state[2], state[3]
        h2X, h2Y = state[4], state[5]

        #h1
        x_new, y_new = moveRight(h1X , h1Y , oX , oY , h2X, h2Y, self.obstacles)
        if [x_new, y_new] != [h1X, h1Y]:
            successors['RightH1'] = (x_new, y_new , oX , oY , h2X, h2Y)

        x_new, y_new = moveLeft(h1X, h1Y, oX, oY, h2X, h2Y, self.obstacles)
        if [x_new, y_new] != [h1X, h1Y]:
            successors['LeftH1'] = (x_new, y_new, oX, oY, h2Y, h2Y)

        x_new, y_new = moveUp(h1X, h1Y, oX, oY, h2X, h2Y, self.obstacles)
        if [x_new, y_new] != [h1X, h1Y]:
            successors['UpH1'] = (x_new, y_new, oX, oY, h2Y, h2Y)

        x_new, y_new = moveDown(h1X, h1Y, oX, oY, h2X, h2Y, self.obstacles)
        if [x_new, y_new] != [h1X, h1Y]:
            successors['DownH1'] = (x_new, y_new, oX, oY, h2Y, h2Y)

        #o
        x_new, y_new = moveRight(oX, oY, h1X, h1Y, h2X, h2Y, self.obstacles)
        if [ x_new, y_new] != [oX, oY]:
            successors['RightO'] = (x_new, y_new, h1X, h1Y, h2X, h2Y)

        x_new, y_new = moveLeft(oX, oY, h1X, h1Y, h2X, h2Y, self.obstacles)
        if [x_new, y_new] != [oX, oY]:
            successors['LeftO'] = (x_new, y_new, h1X, h1Y, h2X, h2Y)

        x_new, y_new = moveUp(oX, oY, h1X, h1Y, h2X, h2Y, self.obstacles)
        if [x_new, y_new] != [oX, oY]:
            successors['UpO'] = (x_new, y_new, h1X, h1Y, h2X, h2Y)

        x_new, y_new = moveDown(oX, oY, h1X, h1Y, h2X, h2Y, self.obstacles)
        if [x_new, y_new] != [oX, oY]:
            successors['Down0'] = (x_new, y_new, h1X, h1Y, h2X, h2Y)

        #h2

        x_new, y_new = moveRight( h2X, h2Y, oX, oY, h1X, h1Y, self.obstacles)
        if [x_new,y_new] != [h2X, h2Y]:
            successors['RightH2'] = (x_new,y_new, oX, oY, h1X, h1Y)

        x_new, y_new = moveLeft(h2X, h2Y, oX, oY, h1X, h1Y, self.obstacles)
        if [x_new, y_new] != [h2X, h2Y]:
            successors['LeftH2'] = (x_new,y_new, oX, oY, h1X, h1Y)

        x_new, y_new = moveUp(h2X, h2Y, oX, oY, h1X, h1Y, self.obstacles)
        if [x_new, y_new] != [h2X, h2Y]:
            successors['UpH2'] = (x_new,y_new, oX, oY, h1X, h1Y)

        x_new, y_new = moveDown(h2X, h2Y, oX, oY, h1X, h1Y, self.obstacles)
        if [x_new, y_new] != [h2X, h2Y]:
            successors['DownH2'] = (x_new,y_new, oX, oY, h1X, h1Y)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[1] == state[3] == state[5] and state[0] + 1 == state[2] and state[2] + 1 == state[4]

    def h(self, node):
        state = node.state
        h1 = state[0], state[1]
        o = state[2], state[3]
        h2 = state[4], state[5]
        value = 0

        # проверка за позициите на H1 и O и потребниот број на чекори за да се спојат
        if h1[0] != o[0]:
            if h1[1] != (o[1] - 1):
                # ако атомот на водорот не е во иста редица и во колона веднаш до атомот
                # на кислород ни требаат најмалку 2 турнувања (turn down/up + left/right)
                # за да се спојат
                value += 2
            else:
                # ако атомот на водорот не е во иста редица, но е во колона веднаш до атомот
                # на кислород ни треба најмалку 1 турнувањe (turn up or down) за да се спојат
                value += 1
        else:  # h1[0] == o[0]
            if h1[1] > o[1]:
                # ако атомот на водорот е во иста редица, но во колона од десна страна на
                # атомот на кислород ни требаат најмалку 3 турнувања (turn 2 x down/up + left/right)
                # за да се спојат
                value += 3
            elif h1[1] < (o[1] - 1):
                # ако атомот на водорот е во иста редица, но во колона од лева страна на
                # атомот на кислород ни треба најмалку 1 турнување (turn right) за да се спојат
                value += 1

        # проверка за позициите на H2 и O и потребниот број на чекори за да се спојат
        if h2[0] != o[0]:
            if h2[1] != (o[1] + 1):
                # ако атомот на водорот не е во иста редица и во колона веднаш до атомот
                # на кислород ни требаат најмалку 2 турнувања (turn down/up + left/right)
                # за да се спојат
                value += 2
            else:
                # ако атомот на водорот не е во иста редица, но е во колона веднаш до атомот
                # на кислород ни треба најмалку 1 турнувањe (turn up or down) за да се спојат
                value += 1
        else:  # h2[0] == o[0]
            if h2[1] < o[1]:  # ако атомот на водорот е во иста редица, но во колона од лева страна на
                # атомот на кислород ни требаат најмалку 3 турнувања (turn 2 x down/up + left/right)
                # за да се спојат
                value += 3
            elif h2[1] > (o[1] + 1):
                # ако атомот на водорот е во иста редица, но во колона од десна страна на
                # атомот на кислород ни треба најмалку 1 турнување (turn left) за да се спојат
                value += 1

        if h1[0] == h2[0] and h1[0] != o[0]:
            # ако водородните атоми се во ист ред тогаш можеме да имаме само едно турнување на
            # атомот на кислород up/down (а претходно сме пресметале турнување на H1 и турнување на H2)
            value -= 1

        return value

if __name__ == '__main__':
    obstacles = [(0, 1), (1, 1), (1, 3), (2, 5), (3, 1), (3, 6), (4, 2),
                 (5, 6), (6, 1), (6, 2), (6, 3), (7, 3), (7, 6), (8, 5)]
    h1_x = int(input())
    h1_y = int(input())
    o_x = int(input())
    o_y = int(input())
    h2_x = int(input())
    h2_y = int(input())
    # 217226
    molecule = Molecule(obstacles, (h1_x, h2_y, o_x, o_y, h2_x, h2_y))

    sol = breadth_first_graph_search(molecule)
   # print(sol.solution())

    answer = astar_search(molecule)
    print(answer.solution())
