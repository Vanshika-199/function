#QUESTION 1

def numbers_less_than_twenty(list):
  counter = 0
  while counter < len(list):
    item = list[counter]
    if item > 20:
      list.remove(item)
    else:
      counter += 1
  return list
num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
print("Initial list",num_list)
num_list_sub_20 = numbers_less_than_twenty(num_list)
print ("List that doesn't contain numbers greater than 20:", num_list_sub_20)

#QUESTION 2 
\


from random import randint
def win():
    print ('You win!')
def lose():
    print ('You lose!')
while True:
    player_choice = input('What do you pick? (rock, paper, scissors)')
    player_choice.strip()
    random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    computer_choice =moves[random_move]

    if player_choice == computer_choice:
        print ('Draw!')
    elif  player_choice == 'rock' and computer_choice == 'scissors':
        win()
    elif  player_choice == 'paper' and computer_choice == 'scissors':
        lose()
    elif player_choice == 'scissors' and computer_choice == 'paper':
        win()
    elif player_choice == 'scissors' and computer_choice == 'rock':
        lose()
    elif player_choice == 'paper' and computer_choice == 'rock':
        win()
    elif player_choice == 'rock' and computer_choice == 'paper' :
        lose()
    again = input('Do you want to play again? (y or n)').strip()
    if again == 'n':
        break

#QUESTION 3


def find_in_list(query, mainlist):
    mainlist_len = len(query)
    range_for_loop = range(mainlist_len)
    index = None
    for i in range_for_loop:
        element = mainlist[i]
        if element==query:
            index = i
        return i
chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']
def encrypt_message(plain_msg):
    encrypted_msg = ""
    for character in encrypted_msg:
        if character in chars:
            char_index = find_in_list(character, chars)
            new_char = shifted_chars[char_index]
            encrypted_msg = encrypted_msg + new_char
        else:
            encrypted_msg = encrypted_msg + character
def decrypt_message(encrypted_msg):
    decrypted_msg = ""
    for character in decrypted_msg:
        if character in shifted_chars:
            char_index = find_in_list(character, shifted_chars)
            new_char = chars[char_index]
            decrypted_msg = decrypted_msg + new_char
        else:
            decrypted_msg = decrypted_msg + character
flag = True
while flag == True:
    choice = input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter e or d respectively!")
    if choice == 'e':
        plain_message = input("Enter message to encrypt??")
        print(encrypt_message(plain_message))  
    elif choice == 'd':
        encrypted_msg = input("Enter message to decrypt?")
        print(decrypt_message(encrypted_msg))
    else:
        play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
        if play_again == 'Y':
            continue
        elif play_again=='N':
            break

#QUESTION 4

from random import randint
alive = True
stamina = 10
def report(stamin):
    if stamina<=8:
        print ("The alien is strong! It resists your pathetic attack!")
    elif stamina<=5:
        print ("With a loud grunt, the alien stands firm.")
    elif stamina<=3:
        print ("Your attack seems to be having an effect! The alien stumbles!")
    elif stamina<=0:
        print ("The alien is certain to fall soon! It staggers and reels!")
    else:
        print ("That's it! The alien is finished!")
def fight(stam):
    while stam > 0:
        response = input("Enter a move 1.Hit 2.attack 3.fight 4.run:  ")
        if "hit" in response or "attack" in response:
            less = randint(0, stam)
            stam -= less
            report(stam)
        elif "fight" in response:
            print ("Fight how? You have no weapons, silly space traveler!")
        elif "run" in response:
            print ("Sadly, there is nowhere to run."),
            print ("The spaceship is not very big.")
        else:
            print ("The alien zaps you with its powerful ray gun!")
            return True
    return False

print ("A threatening alien wants to fight you!\n")
alive = fight(stamina)
if alive:
    print ("\nThe alien lives on, and you, sadly, do not.\n")
else:
    print ("\nThe alien has been vanquished. Good work!\n")

