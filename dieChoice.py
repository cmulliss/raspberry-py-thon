# One die, the kind with spots!

import random
throwDie = int(input('How many throws would you like? '))
for i in range (throwDie):
    throws = random.randint(1, 6)
    print(throws)
