# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""
from sets import Set
import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def startingState(self):
    """
    Returns the start state for the search problem 
    """
    util.raiseNotDefined()

  def isGoal(self, state): #isGoal -> isGoal
    """
    state: Search state

    Returns True if and only if the state is a valid goal state
    """
    util.raiseNotDefined()

  def successorStates(self, state): #successorStates -> successorsOf
    """
    state: Search state
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
    """
    util.raiseNotDefined()

  def actionsCost(self, actions): #actionsCost -> actionsCost
    """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
    """
    util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.startingState()
  print "Is the start a goal?", problem.isGoal(problem.startingState())
  print "Start's successors:", problem.successorStates(problem.startingState())
  """
  searchStack, visited, path = util.Stack(), Set([problem.startingState()]), []
  parent = dict()

  if problem.isGoal(problem.startingState()): return []

  for succesor in problem.successorStates(problem.startingState()):
    parent[succesor[0]] = problem.startingState(), None, 1
    searchStack.push(succesor)
    visited.add(succesor[0])

  while not searchStack.isEmpty():
    current = searchStack.pop()
    curr_cord = current[0]

    if problem.isGoal(curr_cord):
      curr_pair = curr_cord
      path.insert(0, current[1])
      while True:
        temp_obj = parent[curr_pair]
        if temp_obj[1] is None: break
        path.insert(0, temp_obj[1])
        curr_pair = temp_obj[0]

      break

    for succesor in problem.successorStates(curr_cord):
      if succesor[0] not in visited:
        visited.add(succesor[0])
        parent[succesor[0]] = current
        searchStack.push(succesor)

  return path

def breadthFirstSearch(problem):
  searchQueue, visited, path = util.Queue(), Set([problem.startingState()]), []
  parent = dict()

  if problem.isGoal(problem.startingState()): return []

  for succesor in problem.successorStates(problem.startingState()):
    parent[succesor[0]] = problem.startingState(), None, 1
    searchQueue.push(succesor)
    visited.add(succesor[0])

  while not searchQueue.isEmpty():
    current = searchQueue.pop()
    curr_cord = current[0]

    if problem.isGoal(curr_cord):
      curr_pair = curr_cord
      path.insert(0, current[1])
      while True:
        temp_obj = parent[curr_pair]
        if temp_obj[1] is None: break
        path.insert(0, temp_obj[1])
        curr_pair = temp_obj[0]

      break

    for succesor in problem.successorStates(curr_cord):
      if succesor[0] not in visited:
        visited.add(succesor[0])
        parent[succesor[0]] = current
        searchQueue.push(succesor)

  return path


def uniformCostSearch(problem):
  pq, visited, path = util.PriorityQueue(), Set([problem.startingState()]), []
  parent = dict()
  cost = dict()

  if problem.isGoal(problem.startingState()): return []

  for succesor in problem.successorStates(problem.startingState()):
    parent[succesor[0]] = problem.startingState(), None, 1
    cost[succesor[0]] = succesor[2]
    pq.push(succesor, succesor[2])
    visited.add(succesor[0])

  while not pq.isEmpty():
    current = pq.pop()
    curr_cord = current[0]

    if problem.isGoal(curr_cord):
      curr_pair = curr_cord
      path.insert(0, current[1])
      while True:
        temp_obj = parent[curr_pair]
        if temp_obj[1] is None: break
        path.insert(0, temp_obj[1])
        curr_pair = temp_obj[0]

      break

    for succesor in problem.successorStates(curr_cord):
      if succesor[0] not in visited:
        visited.add(succesor[0])
        parent[succesor[0]] = current
        cost[succesor[0]] = cost[curr_cord] + succesor[2]
        pq.push(succesor, cost[curr_cord] + succesor[2])

  return path

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  pq, visited, path = util.PriorityQueue(), Set([problem.startingState()]), []
  parent = dict()
  depth = dict()

  if problem.isGoal(problem.startingState()): return []

  for succesor in problem.successorStates(problem.startingState()):
    parent[succesor[0]] = problem.startingState(), None, 1
    depth[succesor[0]] = 1
    pq.push(succesor, 1 + heuristic(succesor[0], problem))
    visited.add(succesor[0])

  while not pq.isEmpty():
    current = pq.pop()
    curr_cord = current[0]

    if problem.isGoal(curr_cord):
      curr_pair = curr_cord
      path.insert(0, current[1])
      while True:
        temp_obj = parent[curr_pair]
        if temp_obj[1] is None: break
        path.insert(0, temp_obj[1])
        curr_pair = temp_obj[0]

      break

    for succesor in problem.successorStates(curr_cord):
      if succesor[0] not in visited:
        visited.add(succesor[0])
        parent[succesor[0]] = current
        depth[succesor[0]] = depth[curr_cord] + 1
        pq.push(succesor, depth[curr_cord] + 1 + heuristic(succesor[0], problem))

  return path


  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
