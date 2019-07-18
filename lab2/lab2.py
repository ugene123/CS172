from item import Item
from receipt import Receipt

print('Welcome to Receipt Creator')

receipt = Receipt(0.08, [])

addAnotherItem = True
while(addAnotherItem):
  itemName = input('Enter Item Name: ')
  itemPrice = float(input('Enter Item Price: '))
  isTaxableInput = input('Is the item taxable (yes/no): ')
  
  itemTaxable = True 
  if(isTaxableInput.lower() == 'no'):
    itemTaxable = False


  item = Item(itemName, itemPrice, itemTaxable)
  receipt.addItem(item)

  addAnotherItemInput = input('Add another item (yes/no):')
  if(addAnotherItemInput.lower() == 'yes'):
    addAnotherItem = True
  elif(addAnotherItemInput.lower() == 'no'):
    addAnotherItem = False


print(receipt)
  
  



