tracker = 0

def moveForwards():
    global tracker 
    tracker += 1
    print('moved forward by one step.')

def turnRight():
    global tracker
    tracker -= 1
    print('turning right')

 # to move robor other direction   
def move():
    global tracker
    tracker -= 2

    return tracker