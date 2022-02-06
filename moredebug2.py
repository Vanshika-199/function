#QUESTION 1

def encrypt(message):
  ascii_message = [ord(char)+3 for char in message]
  encrypt_message = [ chr(char) for char in ascii_message]  
  print (''.join(encrypt_message))
def decrypt(message):
  ascii_message = [ord(char) for char in message]
  decrypt_message = [ chr(char) for char in ascii_message]  
  print (''.join(decrypt_message))
flag = True
while flag == False:
    choice = input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter E or D respectively!")
    if choice =='e':
        encrypt()
    elif choice == 'd':
        decrypt()    
    else:
        play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
        if play_again == 'Y':
            continue
        elif play_again == 'N':
            break
message = input("Enter the message you want to encrypt")
message = input("Enter the message you want to decrypt")
encrypt(message)
decrypt(message)

#QUESTION 2

import random
def getSecretNum(numDigits):
  numbers = list(range(10))
  random.shuffle(numbers)
  secretNum = ''
  for i in range(numDigits):
    secretNum += (numbers[i])
  print (secretNum)
def getClues(guess, secretNum):
  if guess == secretNum:
    return 'You got it!'
  clue = []
  for i in range(len(guess)):
    if guess[i] == secretNum[i]:
      clue.append('Fermi')
    elif guess[i] in secretNum:
      clue.append('Pico')
    if len(clue) == 0:
      return 'None'
  return ' '.join(clue)
def isOnlyDigits(num):
  if num =='':
    return False
  for i in num:
    if i not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
      return False
def playAgain():
  play = input("Do you want to play again? Yes or No?") 
  return play.lower.startswith('y')
NUMDIGITS = 3
MAXGUESS = 10
print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUMDIGITS))
print('Here are some clues:')
print('When I say:    That means:')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  None       No digit is correct.')
while True:
  secretNum = getSecretNum(NUMDIGITS)
  print('I have thought up a number. You have %s guesses to get it.' % (MAXGUESS))
  numGuesses = 1
  while numGuesses <= MAXGUESS:
    while len(guess) != NUMDIGITS or not isOnlyDigits(guess):
      print ('Guess' + (numGuesses))
      guess = input("Guess Again")
    clue = getClues(guess, secretNum)
    print(clue)
    numGuesses += 1
    if guess == secretNum:
      break
    if numGuesses < MAXGUESS:
      print ('You ran out of guesses. The answer was ' + secretNum)
  if not playAgain:
      break
