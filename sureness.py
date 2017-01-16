from question import Question
from response import Response

class Sureness:
	def __init__(self, nickname, responses):
		if not isinstance(nickname, str):
			raise TypeError("Nickname must be a string")
		assert isinstance(responses, list)
		self.nickname = nickname
		self.responses = responses

	def add_response(self, response):
		self.responses += [response]