import re
from typing import List

def load_data(file_name: str) -> List[List[str]]:
	s = ""
	allowed = {' ', '\'', '`'}
	for i in range(ord('a'), ord('z') + 1):
		allowed.add(chr(i))
	with open(file_name) as f:
		s = ' '.join(f.readlines()).lower()
	sentence_ends = {'.', '!', '?'}
	for item in set(s) - allowed - sentence_ends:
		s = s.replace(item, ' ')
	return [item for item in map(lambda x: x.split(), re.split("[" + ''.join(sentence_ends) + "]+", s)) if item]
