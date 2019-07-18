# Yevgeniy (Eugene) Yakovlev 
# Jason Abraham
# CS 171 - Lab 1
# Wednesday, June 26, 2019

# Your program must meet all the following requirements:
###     Contains a function get_file() that reads a filename for the user. If the file cannot be opened, repeatedly ask the user until a valid file name is input. The function should have a try/catch statements to deal with any possible errors.
###     Print a welcome message to the user and asks for the name of the file to spellcheck. You must use the above function.
###     Read through the file and print out any word that is not spelling correctly. You must use the spellchecker class to complete this lab.
###     Now switch Driver/Observer roles!
###     When an incorrectly spelled word is found, also print what line the error appeared on. The first line in a file should be line number 1.
###     Print out a summary with the number of words spelled correctly, incorrectly, and percent of words that are correct. This must exactly match the formatting shown in the examples.


from spellchecker import spellchecker

def get_file():
  file = None
  # Repeatedly ask the user until a valid file name is given as an input..
  while (file == None):
    try:
      # Get filename as input
      file_name = str(input("Enter the name of the file to read:\n"))
      try:
        file = open(file_name, "r")
        return file
      except IOError:
        print("Error: File does not appear to exist. ")

    except:
      # Execption while reading filename as string
      print('Try again! Filename has to be a valid string')


def startProgram():
  print('Welcome to Text File Spellchecker.')
  # Ask user for filename and return file object
  file = get_file()
  # Read file 

  # Set spellchecker words from english_words.txt
  SP = spellchecker('english_words.txt')

  # Keep counter of items tracked
  spelled_correctly = 0
  spelled_incorrectly = 0
  line_number = 0

  # Loop through lines in file
  for line in file.readlines():
    line_number += 1
    # Loop through words in line
    for word in line.split():

      # do something with word
      exists = SP.check(word)
      if(exists):
        # Spelled correctly
        spelled_correctly += 1
      else:
        # Spelled incorrectly
        spelled_incorrectly += 1
        print('Possible Spelling Error on line', str(line_number) + ': ' + word)

  # print(spelled_correctly, 'words passed spell checker.')
  print("{:,}".format(spelled_correctly), 'words passed spell checker.')
  print("{:,}".format(spelled_incorrectly), 'words failed spell checker.')

  words_passed_percent = '%0.2f' % (spelled_correctly / (spelled_correctly + spelled_incorrectly) * 100)

  print("{0}% of the words passed.".format(words_passed_percent))


startProgram()
