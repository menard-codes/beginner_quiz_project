# The answers
answers = ['c', 'a', 'd']

# Quiz title and direction
print('\n\nWelcome to our Python Tutorial Quiz!!!\n')
print('Direction:')
print('Choose the letter of the correct answer\n')

# Question number 1:
print("1.) What will you get if you run print(type(True))?")
print('a. str\t\tb. int')
print('c. bool\t\td. float')
ans1 = input('Enter your answer here:\n>>>')

# Question number 2:
print('\n')
print("2.) What is the character used to escape other characters?")
print('a. \\ Backslash\t\t\tb. / Forward slash')
print('c. % Percent sign\t\td. none of the above')
ans2 = input('Enter your answer here:\n>>>')

# Question number 3:
print('\n')
print("2.) What is the type of this data: {1, 2, 3}")
print('a. Dictionary\tb. String')
print('c. List\t\t\td. Set')
ans3 = input('Enter your answer here:\n>>>')

# checking
score = 0
if ans1 == answers[0]:
	score += 1
if ans2 == answers[1]:
	score += 1
if ans3 == answers[2]:
	score += 1

# Tell the score
print(f'\n\nYou got {score} out of 3\n\n')
