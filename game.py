from random import randint
secret = randint(1,10)
print ('Welcome!')
guess = 0
while guess != secret:
    g = input ('Guess the number:')
    guess = int(g)
    if guess == secret:
        print ('You win!')
    else:
        if guess > secret:
            print ('To hight')
        else:
            print('To low')
print('Game over!')
        
    