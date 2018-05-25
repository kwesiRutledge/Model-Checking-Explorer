class my_TS:
	""" This is an implementation of a transitions system according to what I think I understand from Baier and Katoen """

	def __init__(self, states , actions, transition_relation , initial_states, atomic_props , labelling_fcn):
		
		#Format Checking
		for transition in transition_relation:
			#Check to see if transition[0] and transition[1] are in states
			if not (transition[0] in states) and not (transition[2] in states):
				print('Error. Transition ',transition,'contains a state which is not in S.')
				return None
			if not (transition[1] in actions):
				print('Error. Transition ',transition,'contains an action which is not in Act.')
				return None

		# Assign the provided values to the tuple that describes the Transition System
		self.S = states;
		self.Act = actions;
		self.trans = transition_relation;
		self.I = initial_states;
		self.AP = atomic_props;
		self.L = labelling_fcn;

	def post(self,s,alpha):
		#Description:
		#	Find the direct alpha-successor of the the state s in the given Transition system
		#	Literally is the set of states for which a tranistion exists from initial state s to the target state when action alpha is applied.

		post_set = []
		for transition in self.trans:
			if (transition[0] is s) and (transition[1] is alpha):
				#IF the initial state and action match, then add the destination to our post_set
				post_set.append(transition[2])

		return post_set