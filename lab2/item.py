class Item:
  def __init__(self, name, price, taxable):
    self.__name = name
    self.__price = price
    self.__taxable = taxable

  def __str__(self): 
    return self.__name + "________________________" + self.__price

  def getName(self):
    return self.__name

  def getPrice(self):
    return self.__price

  def isTaxable(self):
    return self.__taxable
  
  def getTax(self, taxRate):
    return self.__price * taxRate