from game_data import data
import random

correct = 0
random.shuffle(data)

def check(A, B):
  if data[A]['follower_count'] > data[B]['follower_count']:
    return True
  return False

def guess():
  question = input("Who has more followers? 'A' or 'B': ")
  return question

def play(correct):
  playing = True
  
  while playing:
    for i in range(0,len(data)):
      a, b = data[i], data[i+1]
      print(f"Compare A: {a['name']}")
      print(f"Against B: {b['name']}")
      follower_guess = guess()
      answer = check(i,i+1)
      if answer and follower_guess =="A":
        correct += 1
      elif not answer and follower_guess == "B":
        correct += 1
      else:
        playing = False
        break
      print("\n")
      
  return (f"\nGame over, you got {correct} correct")

print(play(correct))