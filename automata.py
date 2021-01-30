import numpy as np
from itertools import product

class Automata():
	def __init__(self, N, r):
		self.N = N
		self.r = r

		local_states = np.array([local_state for local_state in product([0,1], repeat=2*r + 1 )])
		
		self.rule = {local_state.tobytes():np.random.randint(2) for local_state in local_states}
		
		state = np.array([np.random.randint(2) for _ in range(N)])
		self.state = np.concatenate([state[-r:], state, state[:r]])
		
		self.begin_state = self.state


	def update_rule(self, new_rule):
		self.rule = {local_state:action for local_state, action in zip(self.rule.keys(), new_rule)}

	def set_begin_state(self, state):
		self.begin_state = np.concatenate((state[-self.r:], state, state[:self.r]))
		self.N = len(state)


	def tick(self):
		state = np.array([self.rule[self.state[a:b].tobytes()] for a, b in zip(range(0,self.N), range(2*self.r + 1, self.N + 2*self.r + 1))])
		self.state = np.concatenate((state[-self.r:], state, state[:self.r]))

	def play(self, M, reset_state=True, no_freeze=False):
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
		
		self.state = self.begin_state

		for i in range(M):
			
			prev = self.state

			self.tick()

			if (self.state == prev).all():
				break


		# fraction of 1's in the final state
		return np.sum(self.state[self.r:self.N + self.r])/self.N




