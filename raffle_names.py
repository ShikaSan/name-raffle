import random

def check_if_name_exists(arr_n, name_input):
    for i in arr_n: 
        if(i == name_input) : 
            return True
    return False

def raffle_draw(entrant_arr):
    i = len(entrant_arr)

    print('TIME TO START THE RAFFLE!')
    k = input('Press enter to continue...\n')
    
    while i != 0:
        rand_val = random.choice(entrant_arr)
        curr_val = rand_val
        
        print('The winner is: ' + curr_val)
        entrant_arr.remove(curr_val)
        k = input('Press enter to continue...\n')
        i = i - 1

    print('END OF RAFFLE')
    k2 = input('Press enter to continue...\n')
            
def mainFunc():
    entrant_pool = []
    ctr = 0
    print ('WELCOME TO THIS SIMPLE RAFFLE DRAW APP')
    k = input('Press enter to continue...')
    print ('\nHow many names to enter the raffle: ')
    num_of_names = int(input())
    
    while True:
        print('Enter a name:')
        raffle_entrant = input()

        is_exists = check_if_name_exists(entrant_pool, raffle_entrant)

        if is_exists == False:
            print('Name successfully added to raffle!\n')
            entrant_pool.append(raffle_entrant)
            ctr = ctr + 1
        else:
            print('Name already exists, please input another one.\n')

        if ctr == num_of_names:
            break
        
    raffle_draw(entrant_pool)

mainFunc()


    
    
