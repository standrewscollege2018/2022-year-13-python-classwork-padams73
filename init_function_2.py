''' This program demonstrates how to use Classes in object orientation
    In this version, we set names for each enemy as they are created '''

class Enemy:
    ''' Enemies are the objects you will battle in the game. The enemy class
    stores the life score of every enemy and contains functions that do damage
    and take damage'''

    def __init__(self, name):
        ''' The init function is called whenever a new instance of the Enemy class
        is created '''

        # The name is sent to the init function when the new enemy is created
        # We set _name as the property
        self._name = name

        # Notice that the life property has an underscore. This indicates it is private
        self._life = 3

        print(f"I am a new enemy! My name is {self._name}")

    def attacked(self):
        ''' This function is called when the enemy is attacked. It prints a message
        and subtracts 1 from the _life score'''

        print("Ouch!")
        self._life -= 1

    def get_life(self):
        ''' This function is called when the program needs to get the current _life
        value of the enemy'''

        return self._life

    def get_name(self):
        ''' This function returns the name of the enemy '''

        return self._name

# Create an enemy
enemy1 = Enemy("Conan the Babarian")
# Attack the enemy and then display the remaining life
enemy1.attacked()
print(f"{enemy1.get_name()} now has life of {enemy1.get_life()}")
