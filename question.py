class Question:
	def __init__(self, prompt, answer):
		if not isinstance(prompt, str):
			raise TypeError("Prompt must be a string")
		self.prompt = prompt
		self.answer = float(answer)

	@classmethod
	def get_question(cls):
		return Question("How many moons does Earth have?", 1.0)
