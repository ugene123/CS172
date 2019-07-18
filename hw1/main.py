from question import Question
from player import Player

# Homework 1 - CS 172, Summer 2019
# Yevgeniy (Eugene) Yakovlev
# 7.5.19

def generateQuiz():
  # Create a set of 10 questions for the quiz
  quiz = []
  # Question 1
  quiz.append(Question('The beaver is the national emblem of which country?', 'Canada', 'United States', 'Spain', 'Iceland', 1))
  # Question 2
  quiz.append(Question('How many players are there in a baseball team?', '7', '9', '11', '12', 2))
  # Question 3
  quiz.append(Question('In Fahrenheit, at what temperature does water freeze?', '-100', '-32', '0', '32', 4))
  # Question 4
  quiz.append(Question('The Statue of Liberty was given to the US by which country?', 'United States', 'Portugal', 'France', 'Great Britain', 3))
  # Question 5
  quiz.append(Question('Which of the planets is closest to the sun?', 'Mercury', 'Venus', 'Mars', 'Earth', 1))
  # Question 6
  quiz.append(Question('How many letters are there in the German alphabet?', '26', '30', '33', '38', 2))
  # Question 7
  quiz.append(Question('In the sport of Judo, what color belt follows an orange belt?', 'Red', 'Green', 'Blue', 'Brown', 2))
  # Question 8
  quiz.append(Question('Who was the first president of the United States?', 'Abraham Lincoln', 'George Washington', 'Woodrow Wilson', 'Benjamin Franklin', 2))
  # Question 9
  quiz.append(Question('What is the largest bone in the human body?', 'Spine', 'Elbow', 'Femur', 'Skull', 3))
  # Question 10
  quiz.append(Question('Entomology is the branch of science that studies what?', 'Forests', 'Oceans', 'Plants', 'Insects', 4))

  return quiz

def getAnswer():
  answer = 0
  while(not (answer in [1,2,3,4])):
    try:
      answer = int(input("Enter your answer: "))
      # Check that answer is between 1 and 4, inclusively
      if(answer < 0 or answer > 4):
        raise ValueError
      return answer
    except:
      print('Error: Your answer has to be a value between 1 and 4. Please try again.')


def startGame():
  # Notify the users that a new game has started
  print('Welcome to Python intro programming quiz \n-----------------------------------------')

  # Create new player objects
  player1 = Player('Player 1')
  player2 = Player('Player 2')

  # Generate quiz and the 10 questions
  quiz = generateQuiz()
  
  # Loop through all the questions in the quiz
  for index, question in enumerate(quiz):
    # Check what player's turn it is. Alternate every other question
    if(index % 2 == 0):
      player = player1
    else:
      player = player2

    print("\n" + player.getName() + " here is your question:")
    print(question)
    answer = getAnswer()
    # Reward player if their answer is correct
    if(answer == question.getAnswer()):
      player.addScore(1)
      print('Excellent! You Score!')
    else: 
      print('That is incorrect. Better luck with the next question!')
    
  # All questions have been answered, print the final scores
  print('\nAnd the final score is:')
  print(player1.getName() + ": " + str(player1.getScore()))
  print(player2.getName() + ": " + str(player2.getScore()))

  # Check if scores are tied
  if(player1.getScore() == player2.getScore()):
    print('It\'s a tie! No one wins!')
  else:
    if(player1.getScore() > player2.getScore()):
      print(player1.getName() + " wins!")
    else:
      print(player2.getName() + " wins!")

# Start the game..
startGame()
