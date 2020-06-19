

class OpenTheLock:
	
	def __init__(self):
		
		pass
	
	@staticmethod
	def split_integer(the_integer: int, minimum_length=None):
		
		the_list = list()
		
		# lol
		for digit in str(the_integer):
			the_list.append(int(digit))
		
		if minimum_length is not None:
			while len(the_list) < minimum_length:
				the_list.insert(0, 0)
		
		return the_list
	
	def count_correct_ignoring_placement(self, correct_answer, guess):
		
		if isinstance(correct_answer, int):
			correct_answer = self.split_integer(correct_answer)
		if isinstance(guess, int):
			guess = self.split_integer(guess)
		
		count = 0
		
		for number in guess:
			if number in correct_answer:
				count += 1
		
		return count
	
	def count_correctly_placed(self, correct_answer, guess):
		
		if isinstance(correct_answer, int):
			correct_answer = self.split_integer(correct_answer)
		if isinstance(guess, int):
			guess = self.split_integer(guess)
			
		count = 0
		
		for i in range(len(correct_answer)):
			
			if i >= len(guess):
				break
			
			if correct_answer[i] == guess[i]:
				count += 1
		
		return count
	
	def count_incorrect_placement(self, correct_answer, guess):
		
		if isinstance(correct_answer, int):
			correct_answer = self.split_integer(correct_answer)
		if isinstance(guess, int):
			guess = self.split_integer(guess)
		
		count = 0
		
		for i in range(len(guess)):
			
			number = guess[i]
			
			# Must not have correct placement
			if i <= len(correct_answer) and correct_answer[i] != number:
				
				# Number must be in the answer, but elsewhere
				if number in correct_answer:
					
					count += 1
		
		return count
