import random
from words import word_list

chosen_word = random.choice(word_list)    
blanks = []
for i in range(len(chosen_word)):
  blanks.append("_ ")
  
print(blanks)

def main():
  lives = 6
  valid = True
  stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
  while valid:
    guess = input(" Enter a guess: ").lower()
        
    for i in range(len(chosen_word)):
      if chosen_word[i] == guess:
        blanks[i] = guess
        
    if guess not in chosen_word:
      lives -= 1
      print(stages[lives])

    for i in blanks:
        print(i,end="")

    if lives == 0:
      valid = False
      print("\n")
      print("\nYou lose")
      print("The word was " + chosen_word)
      
    if "_ " not in blanks:
      valid = False
      print("\nYou Win")
      
      
  
main()