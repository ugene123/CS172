class Employee():

  def __init__(self, id, hours, hourly_rate):
    self.__id = id
    self.__hours = hours
    self.__hourly_rate = hourly_rate
    self.__gross_pay = hours * hourly_rate

  def __str__(self):
    description = '\n\nEmployee ID: ' + self.__id
    description += '\nHours: ' + str(self.__hours)
    description += '\nHourly Rate: ' + str(self.__hourly_rate)
    description += '\nGross Pay: $' + str(self.__gross_pay)
    return description

  def getHours(self):
    return self.__hours

  def getHourlyRate(self):
    return self.__hourly_rate

  def getID(self):
    return self.__id
  
  def setHours(self, hours):
    self.__hours = hours
    self.__gross_pay = self.__hourly_rate * hours

  def setHourlyRate(self, hourly_rate):
    self.__hourly_rate = hourly_rate
    self.__gross_pay = self.__hours * hourly_rate

  