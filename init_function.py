''' This program demonstrates how to use Classes in object orientation'''

class Enemy:
    ''' Enemies are the objects you will battle in the game. The enemy class
    stores the life score of every enemy and contains functions that do damage
    and take damage'''

    def __init__(self):
        ''' The init function is called whenever a new instance of the Enemy class
        is created '''

        print("I am a new enemy!")
        

        # Notice that the life property has an underscore. This indicates it is private
        self._life = 3

    def attacked(self):
        ''' This function is called when the enemy is attacked. It prints a message
        and subtracts 1 from the _life score'''

        print("Ouch!")
        self._life -= 1

    def get_life(self):
        ''' This function is called when the program needs to get the current _life
        value of the enemy'''

        return self._life

# Create an enemy
enemy1 = Enemy()
# Attack the enemy and then display the remaining life
enemy1.attacked()
print(f"The enemy now has life of {enemy1.get_life()}")
