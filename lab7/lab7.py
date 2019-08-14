from room import Room
from maze import Maze

# my_rooms = []
# my_rooms.append(Room("Entrance"))
# my_rooms.append(Room("Living Room"))
# my_rooms.append(Room("Exit"))
# #room 0 is south of room 1
# my_rooms[0].setNorth(my_rooms[1])
# my_rooms[1].setSouth(my_rooms[0])
# #Room 2 is east of room 1
# my_rooms[1].setEast(my_rooms[2])
# my_rooms[2].setWest(my_rooms[1])

# my_maze = Maze(my_rooms[0], my_rooms[2])

my_rooms = []
for i in range(1, 11):
  room = Room("Room #" + str(i))
  my_rooms.append(room)

for i in range(0, 9):
  my_rooms[i].setNorth(my_rooms[i+1])
  my_rooms[i+1].setSouth(my_rooms[i])

my_maze = Maze(my_rooms[0], my_rooms[9])

def checkIfRoomExists(roomExists):
  if(not roomExists):
    print('\n!!!! INVALID DIRECTION, TRY AGAIN !!!!')

gameOver = False
while not gameOver:
  currentRoom = my_maze.getCurrrent()
  print("\nThe current room is: ")
  print(currentRoom)

  command = input('\nEnter Direction to Move (North, East, South, West) or (Restart):\n').lower()

  roomExists = True
  if(command == 'restart'):
    my_maze.reset()
  elif(command == 'north'):
    roomExists = my_maze.moveNorth()
  elif(command == 'east'):
    roomExists = my_maze.moveEast()
  elif(command == 'south'):
    roomExists = my_maze.moveSouth()
  elif(command == 'west'):
    roomExists = my_maze.moveWest()
  else:
    print("Invalid Command!")

  checkIfRoomExists(roomExists)

  if(my_maze.atExit()):
    gameOver = True
    print('\n\n\n\n\n\n\nYOU WIN! You found the Exit. You are FREE! :D')