# Yevgeniy (Eugene) Yakovlev 
# ID: 14153285
# CS 172, Summer 2019
# Employee Payroll Homework Assignment #4

class Node():

  def __init__(self, data, next = None):
    self.__data = data
    self.__next = next
  
  def getData(self):
    return self.__data

  def getNext(self):
    return self.__next

  def setData(self, data):
    self.__data = data

  def setNext(self, next):
    self.__next = next

  def __str__(self):
    return str(self.__data) + " whose next node is " + str(self.__next) 