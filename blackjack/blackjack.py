import random

def deal_card():
  deck = [11,2,3,4,5,6,7,8,9,10,10,10]
  return random.choice(deck)

def check(card_deck):
  total = sum(card_deck)
  if total <= 21:
    return True
  return False

def add_card(card_deck):
  card_deck.append(deal_card())
  return card_deck

def generate_deck():
  deck = []
  for i in range(2):
    deck.append(deal_card())
  return deck

def calculate_deck(card_deck):
  total = sum(card_deck)
  if total == 21 and len(card_deck) == 2:
    return total
  if total > 21 and 11 in card_deck:
    for i in card_deck:
      if i == 11:
        pos = card_deck.index(i)
        card_deck[pos] = 1
    total = sum(card_deck)
  return total
      
def check_winner(player_deck, dealer_deck):
  player_total = calculate_deck(player_deck)
  dealer_total = calculate_deck(dealer_deck)
  if (player_total == 0 and dealer_total != 0) or (dealer_total == 0 and player_total != 0):
    print("You win")
  elif player_total == dealer_total:
    print("Draw")
  elif dealer_total > player_total and dealer_total <=21:
    print("You lose!")
  else:
    print("You win!")

def play():
  print("\n")
  playing = True
  cur_deck = generate_deck()
  dealer_deck = generate_deck()
  print(f"Your cards: {cur_deck}, current score: {sum(cur_deck)}")
  print(f"Dealers cards are: {dealer_deck}")
  while playing:
    if check(cur_deck):
      hit = input("Press 'y' to hit or 'n' to stand: ").lower()
      if hit == "y":
        cur_deck = add_card(cur_deck)
        print(f"{cur_deck}, current score: {sum(cur_deck)}")
      elif hit == "n":
        while calculate_deck(dealer_deck) < 18:
            dealer_deck = add_card(dealer_deck)
        print(f"Dealers cards are: {dealer_deck}") 
        check_winner(cur_deck,dealer_deck)
        playing = False
    else:
      print("Bust, You lose")
      playing = False
      
play()
while True:
  play_again = input("\n Would you like to play again 'y' or 'n' ?: ")
  if play_again == "y":
    play()
  else:
    break