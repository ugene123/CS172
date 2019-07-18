import datetime

class Receipt:
  def __init__(self, taxRate, purchases):
    self.__tax_rate = taxRate 
    self.__purchases = purchases 
  
  def __str__(self):
    fullReceipt = "---- Receipt " + str(datetime.datetime.now()) + " -----"

    subTotal = 0
    tax = 0

    for item in self.__purchases:
      # Format itemPrice to two decimal places..
      itemPrice = '%0.2f' % item.getPrice()
      fullReceipt += ("\n" + item.getName() + "_________________" + itemPrice)

      subTotal += item.getPrice()
      
      if(item.isTaxable()):
        tax += item.getTax(self.__tax_rate)
  

    fullReceipt += '\n\nSub Total_________________' + ('%0.2f' % subTotal)
    fullReceipt += '\nTax_________________' + ('%0.2f' % tax)
    fullReceipt += '\nTotal_________________' + ('%0.2f' % (tax + subTotal))
    return fullReceipt


  def addItem(self, item):
    self.__purchases.append(item)




    