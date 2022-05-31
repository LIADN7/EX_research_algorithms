#!python3

"""
Shapley value calculation.

Programmer: Liad Nagi
Since: 2022-04
"""


import itertools
import logging
logger = logging.getLogger(__name__)

class demo_shapley():
	def values(self, abc: dict(), agents: list[str], just_avg: bool =True):
		"""
		Calculate the Shapley values for all players.
		:param abc:  a dict where each key is a string representing a subset of players, and its value is the cost of that subset.
		:param agents: a list of string where each point in the list represents a player.
		:param just_avg: if just the avg of the agents or want all the table.
		:return if just_avg: a dict where each key is a string representing a player, and each value is the player's Shapley value.
		:return else: a dict where each key is a string representing a player, and each value is dict with table of all the shapley value in each permutation.
		>>> # ex1
		>>> # ------
		>>> shap = shapley()
		>>> abc = {"": 0,"a": 0,"b": 0,"c": 100,"ab": 300,"ac": 200,"bc": 100,"abc": 500}
		>>> agents = ["a","b","c"]
		>>> res = shap.values(abc, agents)
		>>> print(res)
		{'a': 200.0, 'b': 150.0, 'c': 150.0}
		>>> res = shap.values(abc, agents, False)
		>>> print(res)
		{'a': {('a', 'b', 'c'): 0, ('a', 'c', 'b'): 0, ('b', 'a', 'c'): 300, ('b', 'c', 'a'): 400, ('c', 'a', 'b'): 100, ('c', 'b', 'a'): 400, 'AVG': 200.0}, 'b': {('a', 'b', 'c'): 300, ('a', 'c', 'b'): 300, ('b', 'a', 'c'): 0, ('b', 'c', 'a'): 0, ('c', 'a', 'b'): 300, ('c', 'b', 'a'): 0, 'AVG': 150.0}, 'c': {('a', 'b', 'c'): 200, ('a', 'c', 'b'): 200, ('b', 'a', 'c'): 200, ('b', 'c', 'a'): 100, ('c', 'a', 'b'): 100, ('c', 'b', 'a'): 100, 'AVG': 150.0}}
		>>> # ex2
		>>> # ------
		>>> abc = {"": 0,"a1": 10,"a2": 10, "a1a2": 15}
		>>> agents = ["a1","a2"]
		>>> res = shap.values(abc, agents)
		>>> print(res)
		{'a1': 7.5, 'a2': 7.5}
		>>> # ex3
		>>> # ------
		>>> abc = {'': 0, 'a': 10}
		>>> agents = ["a"]
		>>> res = shap.values(abc, agents)
		>>> print(res)
		{'a': 10.0}
		>>> # ex4
		>>> # ------
		>>> abc = {'': 0, 'a1': 100, 'B2': 150, 'c1': 250, 'a1B2': 200, 'a1c1': 250, 'B2c1': 300, 'a1B2c1': 370}
		>>> agents = ["a1", "B2", "c1"]
		>>> res = shap.values(abc, agents)
		>>> print(res)
		{'a1': 65.0, 'B2': 115.0, 'c1': 190.0}
		"""
		permo = list(itertools.permutations(agents))
		ag = dict()
		for i in agents:
			map_i = dict()
			sum = 0
			for j in permo:
				map_i[j] = self.get_cost_from_permo(i, j, abc)
				sum+=map_i[j]
			map_i["AVG"]=sum/len(permo)
			ag[i]=map_i
		if(not just_avg):
			return ag
		res = dict()
		for i in ag:
			res[i]=ag[i]["AVG"]

		return res



	def get_cost_from_permo(self, agent: str, permo: tuple(), abc: dict()):
		"""
		Calculate the value of agent in permutation from the abc.
		:param agent: the agent being tested.
		:param permo: the permo being tested.
		:param abc:  a dict where each key is a string representing a subset of players, and its value is the cost of that subset.
		:return: a value of the current state.
		>>> # ex1
		>>> # ------
		>>> shap = shapley()
		>>> abc = {"": 0,"a": 0,"b": 0,"c": 100,"ab": 300,"ac": 200,"bc": 100,"abc": 500}
		>>> agent = "a"
		>>> permo = ("a","b","c")
		>>> res = shap.get_cost_from_permo(agent, permo, abc)
		>>> print(res)
		0
		>>> # ex2
		>>> # ------
		>>> agent = "c"
		>>> permo = ("a","b","c")
		>>> res = shap.get_cost_from_permo(agent, permo, abc)
		>>> print(res)
		200
		>>> # ex3
		>>> # ------
		>>> abc = {'': 0, 'a1': 100, 'B2': 150, 'c1': 250, 'a1B2': 200, 'a1c1': 250, 'B2c1': 300, 'a1B2c1': 370}
		>>> agent = "B2"
		>>> permo = ("a1","B2","c1")
		>>> res = shap.get_cost_from_permo(agent, permo, abc)
		>>> print(res)
		100
		"""
		lst_end = list()
		lst_minus = list()
		flag=False
		for i in permo:
			if(agent is i):
				lst_end.append(i)
				break
			else:
				lst_end.append(i)
				lst_minus.append(i)
		sum_end=0
		sum_minus=0
		for i in abc:
			if(all(str(l) in i for l in lst_end)):
				sum_end=abc[i]
				break
		for i in abc:
			if(all(str(l) in i for l in lst_minus)):
				sum_minus=abc[i]
				break
		return sum_end - sum_minus
				


if __name__ == "__main__":
    import doctest
    (failures,tests) = doctest.testmod(report=True)
    print ("{} failures, {} tests".format(failures,tests))
