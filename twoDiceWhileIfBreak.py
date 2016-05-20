# 2 Dice, continue throwing until 6s thrown

from random import randint

while True:
    throwOne = randint(1, 6)
    throwTwo = randint(1, 6)
    total = throwOne + throwTwo
    print(total)
    if (throwOne == 6 and throwTwo == 6):
         break
print('Double 6 thrown')
        

        
       
    
        

