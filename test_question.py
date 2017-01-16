import unittest

from question import Question

class TestQuestionMethods(unittest.TestCase):
	def test_prompt_is_string(self):
		question1 = Question("What is 2x2?", 4)
		self.assertIsInstance(question1.prompt, str)
		
	def test_answer_is_float(self):
		question1 = Question ("What is 3x3?", 9.0)
		self.assertIsInstance(question1.answer, float)
		question2 = Question("What is 2x2?", 4)
		self.assertIsInstance(question2.answer, float)

	def test_get_question(self):
		question1 = Question.get_question()
		self.assertIsInstance(question1, Question
)
if __name__ == '__main__':
	unittest.main()