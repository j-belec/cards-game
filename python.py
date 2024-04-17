import random 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

class Card:
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
    self.value = values[rank]
  
  def __str__(self):
    return self.rank + " of " + self.suit
    
class Deck:
  def __init__(self):
    self.all_cards = [];
    for suit in suits:
      for rank in ranks:
        self.all_cards.append(Card(suit, rank))

  def shuffle(self):
    random.shuffle(self.all_cards)
  
  def deal_one(self):
    return self.all_cards.pop()
  
  def split(self, jugador1, jugador2):
     for i in range(0, len(self.all_cards)):
        if(i % 2 == 0):
           jugador1.add_cards(self.deal_one())
        else:
           jugador2.add_cards(self.deal_one())

class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = [] 
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


#########
##GAME##
#########
player_one = Player("One")
player_two = Player("Two")

my_deck = Deck()
my_deck.shuffle()
my_deck.split(player_one, player_two)

game_on = True
round_num = 0

while game_on:
  round_num += 1

  print("--- RONDA " + str(round_num) + " ---")

  #if one of the player has no cards the other one wins
  if(len(player_one.all_cards) == 0):
     print("Player on run out of card! Player two wins!!")
     game_on= False
     break
  if(len(player_two.all_cards) == 0):
     print("Player two run out of cards! Player one wins!!")
     game_on= False
     break

  print("play1")
  print(len(player_one.all_cards))
  print("play1")
  print(len(player_two.all_cards))
  

  cards_player_one_round = []
  cards_player_two_round = []

  cards_player_one_round.append(player_one.remove_one())
  cards_player_two_round.append(player_two.remove_one())

  war = True

  while war:
    if(cards_player_one_round[-1].value > cards_player_two_round[-1].value):
      print("player 1 wins this round")
      player_one.add_cards(cards_player_one_round)
      player_one.add_cards(cards_player_two_round)
      war = False

    elif(cards_player_one_round[-1].value < cards_player_two_round[-1].value):
      print("player 2 wins this round")
      player_two.add_cards(cards_player_one_round)
      player_two.add_cards(cards_player_two_round)
      war = False

    else:
      print('WAR!!!')

      if len(player_one.all_cards) < 5:
          print("Player One unable to play war! Player Two Wins!")
          game_on = False
          break

      elif len(player_two.all_cards) < 5:
          print("Player Two unable to play war! Player One Wins!")
          game_on = False
          break
      
      # if both players have 5 cards in their deck th war will start, so we'll add the next cards
      else:
          for num in range(5):
              cards_player_one_round.append(player_one.remove_one())
              cards_player_two_round.append(player_two.remove_one())



  
