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
  print('b. Enter Hours for all Employees')
  print('c. Display Payroll')
  print('d. Update Hourly Rate for Employee')
  print('e. Remove Employee from Payroll')
  print('q. Exit Program')

runProgram = True

while runProgram:
  displayUserInputOptions()
  userInput = input('\nEnter your choice: ')

  if(userInput not in ['a', 'b', 'c', 'd', 'e', 'q']):
    print('! INVALID INPUT: Please try selecting a valid option')

  else:
    if(userInput == 'a'):
      # Add New Employee
      idValid, hoursValid, hourlyRateValid = False, False, False
      
      while not idValid:
        employeeId = input('Enter Employee ID: ')
        found, node = employees.search(employeeId)
        if(not found):
          idValid = True
        else:
          print('Error: Duplicate Employee ID!')

      while not hoursValid:
        try:
          hours = float(input('Enter Hours Worked: '))
          if(hours < 0):
            print('Error: Hours can only be a positive number')
          else:
            hoursValid = True
        except:
          print('Error: Hours has to be a floating point number')

      while not hourlyRateValid:
        try:
          hourly_rate = float(input('Enter Hourly Rate: '))
          if(hourly_rate < 6):
            print('Error: Hourly rate cannot be less than $6.00')
          else:
            hourlyRateValid = True
        except:
          print('Error: Hourly Rate has to be a floating point number')

      employee = Employee(employeeId, hours, hourly_rate)
      employees.appendNode(employee)

    elif(userInput == 'b'):
      # Enter Employee Hours for each employee
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
              if(hours < 0):
                print('Error: Hours can only be a positive number')
              else:
                employee.setHours(hours)
                hoursValid = True
            except:
              print('Error: Hours has to be a floating point number')
          
          currentNode = currentNode.getNext()

        print('\nSuccessfully updated hours for all employees!')

    elif(userInput == 'c'):
      # Display Payroll - All employee info
      print('\n*** Payroll ***')
      if(employees.isEmpty()):
        print('Empty')
      else:  
        print(employees)

    elif(userInput == 'd'):
      # Update Hourly Rate for specific employee
      if(employees.isEmpty()):
        print('\nERROR: Payroll is empty')
      else:
        employeeID = input('Enter the ID of the employee to update hourly rate: ')
        found, currentNode = employees.search(employeeID)
        if(found):
          employee = currentNode.getData()
          hourlyRateValid = False
          while not hourlyRateValid:
            try:
              hourly_rate = float(input('Enter hourly rate for Employee ID (' + str(employee.getID()) + '): '))
              if(hourly_rate < 6):
                print('Error: Hourly rate cannot be less than $6.00')
              else:
                employee.setHourlyRate(hourly_rate)
                hourlyRateValid = True
            except:
              print('Error: Hourly Rate has to be a floating point number')
    
          print('\nSuccessfully updated hourly rate for employee (' + str(employee.getID()) + ')!')
        else:
          print('\nERROR: Employee (' + employeeID + ') does not exist!')

    elif(userInput == 'e'):
      # Remove Employee from employees
      if(employees.isEmpty()):
        print('\nERROR: Payroll is empty')
      else:
        employeeID = input('Enter the ID of the employee to remove from payroll: ')
        found, employee = employees.search(employeeID)
        if(found):
          employees.removeNode(employeeID)
        else:
          print('\nERROR: Employee (' + employeeID + ') does not exist!')

    elif(userInput == 'q'):
      runProgram = False
