import unittest

from response import Response
from question import Question

class TestResponseMethods(unittest.TestCase):	
	def test_guess_low_is_float(self):
		response1 = Response (4, 9, Question.get_question())
		self.assertIsInstance(response1.guess_low, float)
		response2 = Response(1.5, 11.2, Question.get_question())
		self.assertIsInstance(response2.guess_low, float)

	def test_guess_high_is_float(self):
		response1 = Response (4, 9, Question.get_question())
		self.assertIsInstance(response1.guess_high, float)
		response2 = Response(1.5, 11.2, Question.get_question())
		self.assertIsInstance(response2.guess_high, float)

	def test_guess_low_less_than_high(self):
		response1 = Response (4, 9, Question.get_question())
		self.assertTrue(response1.guess_low <= response1.guess_high)

	def test_question_is_question(self):
		response1 = Response (4, 9, Question.get_question())
		self.assertIsInstance(response1.question, Question)

if __name__ == '__main__':
	unittest.main()