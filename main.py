############### Our Blackjack House Rules #####################
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
###############################################################
import random
from art import logo
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playerHand = []
dealerHand = []

def getHand(string):
  """Returns a valid hand based on string. False if not valid string."""
  if string.lower() == "player":
    return playerHand
  elif string.lower() == "dealer":
    return dealerHand
  else:
    return False

def dealCard(validHand):
  """Deals card to a valid hand."""
  validHand.append(random.choice(cards))

def calculateScore(validHand):
  """Calculates total based on cards in provided valid hand."""
  # Checks for blackjack (a hand with only 2 cards: ace + 10)
  if sum(validHand) == 21 and len(validHand) == 2:
    return 0

  # If we have an 11 (Ace) and the score is over 21, remove the 11 and replace it with a 1.
  if 11 in validHand and sum(validHand) > 21:
    validHand.remove(11)
    validHand.append(1)
  return sum(validHand)

def compareScore(playerScore, dealerScore):
  if playerScore > 21 and dealerScore > 21:
      return "Bust. You Lose!"

  if playerScore == dealerScore:
    return "Draw!"
  elif dealerScore == 0:
    return "Dealer Blackjack. You Lose!"
  elif playerScore > 21:
    return "Bust. You Lose!"
  elif dealerScore > 21:
    return "Dealer Bust. You Win!"
  elif playerScore > dealerScore:
    return "You Win!"
  else:
    return "You Lose!"

def getAction():
  """Gets a valid play action, hit or stand."""
  validResponse = False
  while not validResponse:
    action = input("Hit or Stand? ")
    if action.lower() == "hit":
      validResponse = True
      return "hit"
    elif action.lower() == "stand":
      validResponse = True
      return "stand"
    else:
      print("That is not a valid move.\n")

def play():
  print(logo)
  playerHand = []
  dealerHand = []
  isGameOver = False

  # Deal player and dealer 2 cards.
  for _ in range(2):
    dealCard(playerHand)
    dealCard(dealerHand)

  while not isGameOver:
    playerScore = calculateScore(playerHand)
    dealerScore = calculateScore(dealerHand)
    print(f"Your Hand: {playerHand}, Value: {playerScore}")
    print(f"Dealer Hand: {dealerHand}, Value: {dealerScore}")

    if playerScore == 0 or dealerScore == 0 or playerScore > 21:
      isGameOver = True
    else:
      action = getAction()
      if action == "hit":
        dealCard(playerHand)
      else:
        isGameOver = True

  while dealerScore != 0 and dealerScore < 17:
    dealCard(dealerHand)
    dealerScore = calculateScore(dealerHand)

  print()
  print(f"Your Final Hand: {playerHand}, Value: {playerScore}")
  print(f"Dealer Final Hand: {dealerHand}, Value: {dealerScore}")
  print(compareScore(playerScore, dealerScore))

while input("Want to play a game? 'y' or 'n': ") == "y":
  clear()
  play()