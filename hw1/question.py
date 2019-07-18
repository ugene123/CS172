class Question():
  def __init__(self, question, option1, option2, option3, option4, answer):
    self.__question = question
    self.__option1 = option1
    self.__option2 = option2
    self.__option3 = option3
    self.__option4 = option4
    self.__answer = answer

  def __str__(self):
    fullQuestion = self.__question
    fullQuestion += "\n1. " + self.__option1
    fullQuestion += "\n2. " + self.__option2
    fullQuestion += "\n3. " + self.__option3
    fullQuestion += "\n4. " + self.__option4 + "\n"
    return fullQuestion

  def getQuestion(self):
    return self.__question
    
  def getAnswer(self):
    return self.__answer
    
