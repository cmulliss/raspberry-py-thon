# 2 Dice

from random import randint

noOfThrows = int(input('You have 2 dice, how many throws would you like? '))
throws = noOfThrows + 1
for x in range(1, throws):
    throwOne = randint(1, 6)
    throwTwo = randint(1, 6)
    total = throwOne + throwTwo
    print(total)



    if total <= 11 and total >= 8:
        print('Not bad, you threw: ', total)
    elif total >10:
        print('Good throw!')
    else:
        print('Oh, bad luck! You threw: ', total)
    if throwOne == throwTwo:
        print('Double thrown, you threw 2 ',throwOne,'\'s')
    if total == 11:
        print('Eleven thrown')       
    if total == 10:
        print('Ten thrown')
    if total == 9:
        print('Nine thrown')       
    if total == 8:
        print('Eight thrown')       
    if total == 7:
        print('Seven thrown')
    if total == 6:
        print('Six thrown')
    if total == 5:
        print('Five thrown')
    if total == 4:
        print('Four thrown')
    if total == 3:
        print('Three thrown')
    if total == 2:
        print('Two thrown')
print('That\'s all for now!')
    
    
        

