import pickle
from typing import List
import random

class SentenceGenerator:
	def __init__(self, last_words = 2):
		self.nxt = dict()
		self.last = last_words
	
	def fit(self, data: List[List[str]]):
		for item in data:
			arr = [None] * self.last + item + [None] * self.last
			for i in range(len(arr) - self.last):
				t = tuple(arr[i: i + self.last])
				if t not in self.nxt:
					self.nxt[t] = []
				self.nxt[t].append(arr[i + self.last])
	
	def generate(self):
		cur = [None] * self.last
		res = []
		res.append(random.choice(self.nxt[tuple(cur)]))
		cur = cur[1:] + [res[-1]]
		while not res[-1] is None:
			res.append(random.choice(self.nxt[tuple(cur)]))
			cur = cur[1:] + [res[-1]]
		return ' '.join(res[:-1])

def save_model(model: SentenceGenerator, file_name: str) -> None:
	pickle.dump(model, open(file_name, "wb"))

def load_model(file_name: str) -> SentenceGenerator:
	model = pickle.load(open(file_name, "rb"))
	if not isinstance(model, SentenceGenerator):
		raise ValueError("File does not contain pickle dump of SentenceGenerator object")
	return model

