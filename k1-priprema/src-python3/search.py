# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
U ovom fajlu cete implementirati algoritme pretrage, koje pozivaju Pacman agenti u searchAgents.py
"""

import util

class SearchProblem:
    """
    Ova klasa definise strukturu problema pretrage, ali ne implementira nijednu od metoda (apstraktna klasa).
    NE TREBA nista u ovoj klasi da menjate.
    """

    def getStartState(self):
        """
        Vraca pocetno stanje problema pretrage.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Stanje pretrage

        Vraca True ako i samo ako je prosledjeno stanje validno ciljno stanje.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Stanje pretrage

        Za prosledjeno stanje, ova funkcija bi trebalo da vrati listu tripleta (successor, action, stepCost),
        gde je 'successor' sledece stanje u odnosu na trenutno (prosledjeno funkciji),
        'action' akcija koja je potrebna da bi se doslo u to stanje i
        'stepCost' inkrementalna cena za razvoj algoritma do successor-a.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: Lista akcija koje je potrebno izvrsiti
        Ova metoda vraca ukupnu cenu odredjene sekvence akcija
        Sekvenca akcija se mora sastojati od legalnih pokreta
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Vraca sekvencu pokreta koji daju resenje za tinyMaze. Za bilo koji drugi lavirint ova sekvenca ce biti neispravna,
    tako da je koristite iskljucivo za tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Najpre pretrazuje najdublje cvorove u stablu.

    Isprobajte i koristite sledece:
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    # TODO 1: Implementirati DFS
    raise util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Najpre pretrazuje najplice cvorove u stablu."""
    # TODO 2: Implementirati BFS
    raise util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    Heuristicka funkcija procenjuje cenu od trenutnog stanja do najblizeg sledeceg stanja u prostoru pretrage.
    Ova heuristika je trivijalna.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Najpre pretrazuje cvor koji ima najnizu kombinovanu cenu i heuristiku."""
    # TODO 3: Implementirati A*
    priority_queue = util.PriorityQueue()
    visited = []
    priority_queue.push([(problem.getStartState(), 'Stop', 0)], 0)
    while not priority_queue.isEmpty():
        path = priority_queue.pop()
        current_state = path[-1][0]
        if problem.isGoalState(current_state):
            return [state[1] for state in path][1:]
        if current_state not in visited:
            visited.append(current_state)
            for successor in problem.getSuccessors(current_state):
                if successor[0] not in visited:
                    successor_path = path[:]
                    successor_path.append(successor)
                    priority = heuristic(successor[0], problem) + successor[2]
                    priority_queue.push(successor_path, priority)
    return []



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
