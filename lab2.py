correctNum = 6 # Variable for correct guess number
no = 0         # Variable for end of simulation

inputNum = input('Guess a number from 1 to 10. (Please enter 0 if you wish to end this simulation.) : ')
inputNum = int(inputNum)

while inputNum != no:
    if inputNum > correctNum and inputNum < 10:
        print('This is too high!')
        inputNum = input('Guess again! (Number from 1 to 10, 0 to end.) : ')
        inputNum = int(inputNum)        
    elif inputNum < correctNum:
        print('This is too low!')
        inputNum = input('Guess again! (Number from 1 to 10, 0 to end.) : ')
        inputNum = int(inputNum)
    elif inputNum > 10:
        print('This is not a number from 1 to 10')
        inputNum = input('Guess again! (Number from 1 to 10, 0 to end.) : ')
        inputNum = int(inputNum)           
    else:
        print('This is correct')
        break

print('End Simulation')    
