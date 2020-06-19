

from OpenTheLock import OpenTheLock


opener = OpenTheLock()

for i in range(1000):

	guess_correct_answer = opener.split_integer(i, 3)
	
	if opener.count_correctly_placed(guess_correct_answer, 682) == 1:
		if opener.count_incorrect_placement(guess_correct_answer, 614) == 1:
			if opener.count_incorrect_placement(guess_correct_answer, 206) == 2:
				if opener.count_correct_ignoring_placement(guess_correct_answer, 738) == 0:
					if opener.count_incorrect_placement(guess_correct_answer, 380) == 1:
						print("Correct answer:", guess_correct_answer)
