from question import Question

class Response:
	def __init__(self, guess_low, guess_high, question):
		assert guess_low <= guess_high
		assert isinstance(question, Question)
		self.guess_low = float(guess_low)
		self.guess_high = float(guess_high)
		self.question = question
