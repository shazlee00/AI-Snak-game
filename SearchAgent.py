"""
search(intial_state):
	#node{ state , path , ..... }
	initialize fringe with intital state
	while fringe is not empty :
		pick a node from the fringe according to a strategy
		if visited : continue
		if goal : return solution
		from state get possible actions
		from actions gets next states
		append successors to the fringe
	return failure 
"""

from Snake_functions import *

def solve(strategy,intial_state,food):
	#print("this is intial state: ")
	#print(intial_state.head.distance(food))
	#print(food.position())
	fringe=[]; visited=[]
	initial_node=init_node(strategy,intial_state,food)
	fringe.append(initial_node)
	print('****this is the fringe size',fringe)
	while len(fringe)>0:
		selected_node=select_node(strategy,fringe)
		current_node=fringe.pop(selected_node)
		#print("this is current_node:  ",current_node['state'])

		if current_node['state'] in visited : continue
		visited.append(current_node['state'])
		if isgoal(current_node['state'],food):
			return get_solution(strategy,current_node,len(visited))
		possible_actions=get_actions(current_node['state'])
		print("possible_actions: ",possible_actions)
		for action in possible_actions:
			print("current_node['state']: ",current_node['state'])
			next_state=get_state(action,current_node['state'])
			print("get_state: ",next_state)
			next_node=add_node(strategy,current_node,action,next_state,food)
			fringe.append(next_node)
		print('****this is the fringe size',len(fringe))	
	return None

def init_node(strategy,intial_state,food):
	#print("**this is intial_state:  ",intial_state)
	initial_node = {}
	initial_node['state']=intial_state
	initial_node['path']=[]
	if strategy=='UCS':
		initial_node['cost']=0
	if strategy == 'Greedy':
		initial_node['heuristic']=compute_heuristic(intial_state,food)
	if strategy =='Astar':
		initial_node['cost']=0
		initial_node['f']=initial_node['cost']+compute_heuristic(intial_state,food)
	return initial_node

def add_node(strategy,current_node,action,next_state,food):
	next_node = {}
	next_node['state']=next_state
	#next_node['path']=current_node['path'][:]; next_node['path'].append(action)
	next_node['path']=[current_node['path'],action]
	if strategy=='UCS':
		next_node['cost']=current_node['cost']+compute_cost(action,current_node['state'],food)
	if strategy=='Greedy':
		next_node['heuristic']=compute_heuristic(next_node['state'],food)
	if strategy=='Astar':
		next_node['cost']=current_node['cost']+compute_cost(action,current_node['state'],food)
		next_node['f']=next_node['cost']+compute_heuristic(next_node['state'],food)
	return next_node

def select_node(strategy,fringe):
	if strategy == 'DFS': return -1
	if strategy == 'BFS': return 0
	if strategy == 'UCS': return get_min('cost',fringe)
	if strategy == 'Greedy': return get_min('heuristic',fringe)
	if strategy == 'Astar': return get_min('f',fringe)

def get_min(key,fringe):
	idx_min= 0
	for i in range(1,len(fringe)):
		if fringe[i][key] < fringe[idx_min][key] :
			idx_min=i
	return idx_min

def get_solution(strategy,current_node,expanded_nodes):
	solution={}
	#solution['solution']=current_node['path']
	solution['solution']=get_path(current_node['path'])
	solution['complexity']=expanded_nodes
	if strategy in ('UCS','Astar'):
		solution['cost']=current_node['cost']
	return solution

def get_path(path):
	if len(path)==0: return []
	else: return get_path(path[0])+[path[1]]

"""
class SearchAgent:
	def __init__(self,searchstrategy,searchproblem):
		self.SearchStrategy=searchstrategy
		self.SearchProblem=searchproblem
	def solve(self,intial_state): pass

class SearchProblem:
	def __init__(self,env):
		self.environment=env
	def get_actions(self,state): pass
	def get_state(self,action,prev_state): pass
	def isgoal(self,state): pass
	def compute_cost(self,state,action): pass
	def compute_heuristic(self,state): pass

class SearchStrategy:
	def init_node(self,intial_state): pass
	def add_node(self,current_node,action,next_state): pass
	def select_node(self,fringe): pass
	def get_solution(self,strategy,current_node,expanded_nodes): pass
"""
