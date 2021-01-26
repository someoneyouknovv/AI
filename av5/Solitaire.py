from SearchProblems.utils import *
from SearchProblems.uninformed_search import breadth_first_graph_search
from SearchProblems.informed_search import astar_search

class Solitaire(Problem):

    def __init__(self, initial, N, obstacles):
        super().__init__(initial, None)
        self.N = N
        self.obstacles = obstacles

    def successor(self, state):
        successors = {}

        for p in state:
            x = p[0]
            y = p[1]

            if x - 2 >= 0 and y + 2 < self.N: #gore desno
                temp_list = list(state)
                if (x - 1, y + 1) in temp_list and (x - 2, y + 2) not in temp_list:
                    temp_list.remove(p)
                    temp_list.remove((x - 1, y + 1))
                    temp_list.append((x - 2, y + 2))
                    successors['Gore Levo: (x=' + str(x) + ',y=' + str(y) + ')'] = tuple(temp_list)

            if x + 2 < self.N and y + 2 < self.N: #gore desno
                temp_list = list(state)
                if (x + 1, y + 1) in temp_list and (x + 2, y + 2) not in temp_list:
                    temp_list.remove(p)
                    temp_list.remove((x + 1, y + 1))
                    temp_list.append((x + 2, y + 2))
                    successors['Gore Desno: (x=' + str(x) + ',y=' + str(y) + ')'] = tuple(temp_list)

            if x - 2 >= 0 and y - 2 >= 0: #dolu levo
                temp_list = list(state)
                if (x - 1, y - 1) in temp_list and (x - 2, y - 2) not in temp_list:
                    temp_list.remove(p)
                    temp_list.remove((x - 1, y - 1))
                    temp_list.append((x - 2, y - 2))
                    successors['Dolu Levo: (x=' + str(x) + ',y=' + str(y) + ')'] = tuple(temp_list)

            if x + 2 < self.N and y - 2 >= 0: #dolu desno
                temp_list = list(state)
                if (x + 1, y - 1) in temp_list and (x + 2, y - 2) not in temp_list:
                    temp_list.remove(p)
                    temp_list.remove((x + 1, y - 1))
                    temp_list.append((x + 2, y - 2))
                    successors['Dolu Desno: (x=' + str(x) + ',y=' + str(y) + ')'] = tuple(temp_list)

            if x - 2 >= 0: # levo
                temp_list = list(state)
                if (x - 1, y) in temp_list and (x - 2, y) not in temp_list:
                    temp_list.remove(p)
                    temp_list.remove((x - 1, y))
                    temp_list.append((x - 2, y))
                    successors['Levo: (x=' + str(x) + ',y=' + str(y) + ')'] = tuple(temp_list)

            if x + 2 < self.N: #desno
                temp_list = list(state)
                if (x + 1, y) in temp_list and (x + 2, y) not in temp_list:
                    temp_list.remove(p)
                    temp_list.remove((x + 1, y))
                    temp_list.append((x + 2, y))
                    successors['Desno: (x=' + str(x) + ',y=' + str(y) + ')'] = tuple(temp_list)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        possible = self.successor(state)
        return possible[action]

    def goal_test(self, state):
        if len(state) == 1:
            if state[0][0] == N//2 and state[0][1] == N-1:
                return True

        return False


if __name__ == "__main__":
    #5 3 2,0 1,1 1,3 4 4,1 4,2 4,3 4,4
    N = int(input())
    number_of_points = int(input())

    points = []
    for _ in range(0, number_of_points):
        points.append(tuple(map(int, input().split(','))))

    points = tuple(points)
    number_of_obstacles = int(input())
    obstacles = []

    for _ in range(0, number_of_obstacles):
        obstacles.append(tuple(map(int, input().split(","))))

    solitaire = Solitaire(points,N,obstacles)
    result = breadth_first_graph_search(solitaire)
    print(result.solution())