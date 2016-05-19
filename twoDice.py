# 2 Dice

from random import randint

noOfThrows = int(input('You have 2 dice, how many throws would you like? '))
throws = noOfThrows + 1
for x in range(1, throws):
    throwOne = randint(1, 6)
    throwTwo = randint(1, 6)
    total = throwOne + throwTwo
    print(total)


    if throwOne == throwTwo:
        print('Double thrown')
    elif total == 11:
        print('Eleven thrown')       
    elif total == 10:
        print('Ten thrown')
    elif total == 9:
        print('Nine thrown')       
    elif total == 8:
        print('Eight thrown')       
    elif total == 7:
        print('Seven thrown')
    elif total == 6:
        print('Six thrown')
    elif total == 5:
        print('Five thrown')
    elif total == 4:
        print('Four thrown')
    elif total == 3:
        print('Three thrown')
    elif total == 2:
        print('Two thrown')
print('That\'s all for now!')
    
    
        

