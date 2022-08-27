# Mackayla Johnson

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
import sys
rooms = {
    'Great Hall': {'North': 'Gallery', 'South': 'Library', 'East':       'Kitchen', 'West': 'Wizard\'s Room'},
    'Library': {'North': 'Great Hall', 'East': 'Armory'},
    'Armory': {'West': 'Library'},
    'Kitchen': {'North': 'Dining Hall', 'West': 'Great Hall'},
    'Dining Hall': {'South': 'Kitchen'},
    'Wizard\'s Room': {'East': 'Great Hall'},
    'Gallery': {'South': 'Great Hall', 'East': 'Tower'},
    'Tower': {'West': 'Gallery'}

}

# Items found in each room
items = {
    'Library': 'Helmet',    
    'Armory': 'Sword',
    'Wizard\'s Room': 'Spell Book',
    'Kitchen': 'Lembas Bread',
    'Dining Hall': 'Sheild',
    'Tower': 'Lilla the Kitten'
}

# List of user's collected items
items_list = []

# Possible directions a user can move
direction = ['North', 'South', 'West', 'East']

# Standard directions for each room
def rules(room):
    print('You are currently in the {}'.format(room))
    print('You can change rooms using the following directions:')
    for direct in direction:
        print('{}'.format(direct))
    print('To stop playing the game, enter "exit".')


# Check that the direction the user inputs is valid, and inform them of the new room

def user_item(current_room):
  if current_room in items:
    item = items[current_room]
    if item not in items_list:
      print('You see a {}'.format(item))
      new_item = input('Would you like to get it? Y/N: ').capitalize()
      if new_item == 'Y':
        items_list.append(items[current_room])
        print('You currently have {}'.format(items_list))
        
      


# main loop
stop = 'go'
# Initiate current_room

while stop != 'Exit':
  print('Welcome to the castle!')
  current_room = 'Great Hall'
  rules(current_room)    
  user_input = ''  
  while user_input != 'Exit':
    user_input = input('Where would you like to go? ').capitalize()
    if user_input == 'Exit':
      print('Thank you for playing this simple game. I hope you enjoyed it! :)')
      print()
      exit()
    if user_input in rooms[current_room]:
      print('Changing rooms to {}'.format(rooms[current_room][user_input]))
      print('-' * 30)
      current_room = rooms[current_room][user_input]
      user_item(current_room)      
      #continue
    else:
      print('{} is not a valid input, try again.'.format(user_input))
      print('-' * 30)
      
    if current_room == 'Gallery':
      if len(items_list) == 5:
        print('You have met the Dragon and used your weapons to beat him. You may now pass to rescue Lilla the Kitten!')
      else:
        print('Watch out, the Dragon has seen you! You have now met your doom. Farewell, my friend. You must now start over. ')
        break
    if current_room == 'Tower':
      print('You have found Lilla the Kitten and won the game! Congratulations and thank you for playing the game!')
      exit() 
    
      