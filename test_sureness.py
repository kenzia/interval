import unittest

from response import Response
from question import Question
from sureness import Sureness

class TestResponseMethods(unittest.TestCase):	
	def test_nickname_is_string(self):
		response1 = Response (4, 9, Question.get_question())
		sureness1 = Sureness ("real damn sure", [response1])
		self.assertIsInstance(sureness1.nickname, str)

	def test_response_is_response(self):
		response1 = Response (4, 9, Question.get_question())
		sureness1 = Sureness ("real damn sure", [response1])
		self.assertIsInstance(sureness1.responses, list)
		self.assertIsInstance(sureness1.responses[0], Response)

	def test_add_response_to_responses(self):
		response1 = Response (4, 9, Question.get_question())
		response2 = Response (1, 3, Question.get_question())
		sureness1 = Sureness ("real damn sure", [response1])
		sureness1.add_response(response2)
		self.assertIsInstance(sureness1.responses[1], Response)

if __name__ == '__main__':
	unittest.main()