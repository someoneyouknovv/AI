from SearchProblems.utils import *
from SearchProblems.uninformed_search import breadth_first_graph_search
from SearchProblems.informed_search import astar_search

class Explorer(Problem):

    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()
        x = state[0]
        y = state[1]
        obstacle1 = list(state[2])
        obstacle2 = list(state[3])

        gridX = 8
        gridY =6

        #da ja pridvizime 1 precka # 0 == nadolu
        if obstacle1[2] == 0:
            if obstacle1[1] == 0:
                obstacle1[2] = 1
                obstacle1[1] +=1
            else:
                obstacle1[1] -=1
        else:
            if obstacle1[1] == gridY-1:
                obstacle1[2] = 0
                obstacle1[1] -=1
            else:
                obstacle1[1] +=1

        #da ja pridvizime 2 precka # 0 == nadolu
        if obstacle2[2] == 0:
            if obstacle2[1] == 0:
                obstacle2[2] = 1
                obstacle2[1] +=1
            else:
                obstacle2[1] -=1
        else:
            if obstacle2[1] == gridY-1:
                obstacle2[2] = 0
                obstacle2[1] -=1
            else:
                obstacle2[1] +=1

        if x + 1 < 8 and (x+1,y) not in [obstacle1, obstacle2]:
            successors['Right'] = (x+1, y, tuple(obstacle1), tuple(obstacle2))

        if x - 1 > 0 and (x-1,y) not in [obstacle1, obstacle2]:
            successors['Left'] = (x-1, y, tuple(obstacle1), tuple(obstacle2))

        if y + 1 < 6 and (x, y+1) not in [obstacle1,obstacle2]:
            successors['Up'] = (x, y+1, tuple(obstacle1), tuple(obstacle2))

        if y - 1 > 0 and (x, y-1) not in [obstacle1, obstacle2]:
            successors['Down'] = (x, y-1, tuple(obstacle1), tuple(obstacle2))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == goal[0] and state[1] == goal[1]

    def h(self, node):
        x = node.state[0]
        y = node.state[1]
        h1 = self.goal[0]
        h2 = self.goal[1]

        return abs(x - h1) + abs(y - h2)

if __name__ == '__main__':
    man_x = 0
    man_y = 2
    obstacle1 = (2,5, 0)
    obstacle2 = (5,0, 1)
    goal = (7,4)

    expl = Explorer((man_x, man_y, obstacle1, obstacle2), goal)

    rez1 = breadth_first_graph_search(expl)
    print(rez1.solution())

    rez2 = astar_search(expl)
    print(rez2.solution())
