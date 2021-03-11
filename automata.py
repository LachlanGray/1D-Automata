import numpy as np
from itertools import product

class Automata():
	''' Cellular Automata 
	Contains the state of N cells, a rule table, and functions to explore behaviours. 
	Rule table is initialized randomly. 

	Args:
		N: number of automata in the ring
		r: automata radius; number of neirbours visible to either side for a cell

	Attributes:
		N, r
		rule: Dictionary with keys being the hash of every observable state, and values being the action to take. 
		state: 1D array, current state of all N automata
		begin_state: Initial state used for each run. 
	'''

	def __init__(self, N, r):
		self.N = N
		self.r = r

		local_states = np.array([local_state for local_state in product([0,1], repeat=2*r + 1 )])
		self.rule = {local_state.tobytes():np.random.randint(2) for local_state in local_states}
		
		state = np.array([np.random.randint(2) for _ in range(N)])
		self.state = np.concatenate([state[-r:], state, state[:r]])
		self.begin_state = self.state


	def update_rule(self, new_rule):
		'''Set a new rule table
		Args:
			new_rule: 1D array of length 2^{2r+1} actions, assuming keys in alphanumeric order. e.g. the first entry
			is for [0,0,0], the second [0,0,1], the third for [0,1,0], etc.
		'''
		self.rule = {local_state:action for local_state, action in zip(self.rule.keys(), new_rule)}

	def set_begin_state(self, state):
		'''Set the initial state
		Args:
			state: 1D array of length N 
		'''
		self.begin_state = np.concatenate((state[-self.r:], state, state[:self.r]))
		self.N = len(state)


	def tick(self):
		''' Apply the update rule
		Updates the state of all of the automata according to the rule table. 
		'''
		state = np.array([self.rule[self.state[a:b].tobytes()] for a, b in zip(range(0,self.N), range(2*self.r + 1, self.N + 2*self.r + 1))])
		self.state = np.concatenate((state[-self.r:], state, state[:self.r]))


	def play(self, M, reset_state=True, no_freeze=False):
		''' Apply the update rule M times

		Args: 
			M: Number of time steps to run for.
			reset_state: If true, the automata state is reset back to begin_state before playing, otherwise it continues from its curent state.
			no_freeze: If true, the run will abort early if the same global state repeats twice in a row
		'''
		if reset_state:
			self.state = self.begin_state
		game = []
		game.append(self.state[self.r:self.N + self.r])
		for _ in range(1,M):
			self.tick()
			game.append(self.state[self.r:self.N + self.r])
			if no_freeze and (self.state[self.r:self.N + self.r] == game[-1]).all():
				break
		return np.array(game)


	def maj_rule(self, M):
		''' Majority rule consensis
		Return the fraction of 1's in the global state after M iterations. 
		Will end before M iterations if the same state is repeated twice in a row. 

		Args:
			M: number of iterations

		'''
		
		self.state = self.begin_state
		for i in range(M):	
			prev = self.state
			self.tick()
			if (self.state == prev).all():
				break
		return np.sum(self.state[self.r:self.N + self.r])/self.N


	def print_rule(self):
		''' Print the Automata's rule
		'''
		for state, action in zip(self.rule.keys(), self.rule.values()):
			print (f'{np.frombuffer(state, dtype=int)}  >>>  {action}')





