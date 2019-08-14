# Yevgeniy (Eugene) Yakovlev 
# ID: 14153285
# CS 172, Summer 2019
# Employee Payroll Homework Assignment #4

from employee import Employee
from linkedlist import LinkedList
from node import Node

employees = LinkedList()

print('*** CS 172 Payroll Simulator ***')

def displayUserInputOptions():
  print('\na. Add New Employee')
  print('b. Enter Hours Worked')
  print('c. Display Payroll')
  print('d. Update Employee Hourly Rate')
  print('e. Remove Employee from Payroll')
  print('q. Exit Program')

runProgram = True

while runProgram:
  displayUserInputOptions()
  userInput = input('\nEnter your choice: ')

  if(userInput not in ['a', 'b', 'c', 'd', 'e', 'q']):
    print('!!! INVALID INPUT: Please try selecting a valid option')

  else:
    if(userInput == 'a'):
      employeeId = input('Enter Employee ID: ')
      hoursValid, hourlyRateValid = False, False

      while not hoursValid:
        try:
          hours = float(input('Enter Hours Worked: '))
          hoursValid = True
        except:
          print('Error: Hours has to be a floating point number')

      while not hourlyRateValid:
        try:
          hourly_rate = float(input('Enter Hourly Rate: '))
          hourlyRateValid = True
        except:
          print('Error: Hourly Rate has to be a floating point number')

      employee = Employee(employeeId, hours, hourly_rate )
      employees.appendNode(employee)

    elif(userInput == 'b'):
      if(employees.isEmpty()):
        print('\nERROR: Payroll is empty')
      else:
        currentNode = employees.getHead()
        while currentNode != None:
          employee = currentNode.getData()

          hoursValid = False
          while not hoursValid:
            try:
              hours = float(input('Enter hours worked for Employee ID (' + str(employee.getID()) + '): '))
              employee.setHours(hours)
              hoursValid = True
            except:
              print('Error: Hours has to be a floating point number')
          
          currentNode = currentNode.getNext()

        print('\nSuccessfully updated hours!')

    elif(userInput == 'c'):
      print('\n*** Payroll ***')
      if(employees.isEmpty()):
        print('Empty')
      else:  
        print(employees)

    elif(userInput == 'd'):
      if(employees.isEmpty()):
        print('\nERROR: Payroll is empty')
      else:
        currentNode = employees.getHead()
        while currentNode != None:
          employee = currentNode.getData()
          hourlyRateValid = False
          while not hourlyRateValid:
            try:
              hourly_rate = float(input('Enter hourly rate for Employee ID (' + str(employee.getID()) + '): '))
              employee.setHourlyRate(hourly_rate)
              hourlyRateValid = True
            except:
              print('Error: Hourly Rate has to be a floating point number')

          currentNode = currentNode.getNext()
        print('\nSuccessfully updated hourly rates!')

    elif(userInput == 'e'):
      if(employees.isEmpty()):
        print('\nERROR: Payroll is empty')
      else:
        employeeID = input('Enter the ID of the employee to remove from payroll: ')
        if(employees.search(employeeID)):
          employees.removeNode(employeeID)
        else:
          print('\nERROR: Employee (' + employeeID + ') does not exist!')

    elif(userInput == 'q'):
      runProgram = False
