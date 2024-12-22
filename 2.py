print('welcome to the treasure land')
direction = input('choose the direction: left or right: ')
if direction == 'left':
    action = input('swim or wait: ')
    if action == 'swim':
        print('game over')
    if action == 'wait':
        door = input('which door: red, blue or yellow: ')
        if door == 'yellow':
            print('you win')
        else:
            print('game over')
elif direction == 'right':
    print('game over')
