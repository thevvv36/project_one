import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

#--------------------------------------------------------------------------------------
class Card:

	def __init__(self,rank,suit):

		self.rank = rank
		self.suit = suit

	def __str__(self):
		return self.rank + ' of ' + self.suit

#------------------------------------------------------------------------------------
class Deck:

	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(rank,suit))


	def shuffle_deck(self):
		random.shuffle(self.deck)


	def __str__(self):
		deck_comp = ''
		for card in self.deck:
			deck_comp += '\n' + card.__str__()
		return 'the deck has:' + deck_comp


	def deal(self):
		single_card = self.deck.pop()
		return single_card


#-------------------------------------------------------------------------------
class Hand():
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self,card):

		self.cards.append(card)
		self.value += values[card.rank]
		if card.rank == 'aces':
			self.aces += 1

	def adjuste_for_ace(self):
		while self.value > 21 and self.aces:
			self.value -= 10
			self.aces -= 1
#---------------------------------------------------------------------------

class Chips():
	def __init__(self):
		self.total = 100
		self.bet = 0


	def win_bet(self):
			self.total += self.bet


	def bust_bet(self):
		self.total -= self.bet

#------------------------------------------------------------------------
def take_bet(Chips):
	while True:
		try:
			player_chips.bet = int(input('how do you want to bet :'))
		except ValueError:
			print('enter a corect value please')
		else:
			if player_chips.bet > player_chips.total: 
				print('sorry your bet can not exceed',chips.total)
			else:
				break

#-----------------------------------------------------------------------------

def hit(deck,hand):
	hand.add_card(deck.deal())
	hand.adjuste_for_ace()

def stand_or_hint(deck,hand):
	global playing
	while True:
		want = input(" do you want to hint or stand :").lower()
		if want[0] == 'h':
			hit(deck,hand)
		elif want[0] == 's':
			playing = False
		else:
			print("sorry try again ")
			continue
		break

#-------------------------------------------------------------------------
def show_some(player,dealer):
	print("dealers hands")
	print("<card hiden>")
	print(" ",dealer.cards[0])
	print("\n player's hand :",*player.cards,sep='\n')

def show_all(player,dealer):
	print("dealer's hand ",*dealer.cards,sep='\n')
	print("dealer hand ",dealer.value)
	print("player's hand",*player.cards,sep='\n')
	print("player's hand ", player.value)

def player_win(player,dealer,chips):
	print('player win')
	player_chips.win_bet()

def player_bust(player,dealer,chips):
	print('player bust')
	player_chips.bust_bet()

def dealer_win(player,dealer,chips):
	print('dealer win')
	player_chips.win_bet()

def dealer_bust(player,dealer,chips):
	print('dealer lose ')
	player_chips.bust_bet()




while True:
	print("WELCOM TO TH GAME HAHAHAHAHA...")
	print("THIS IS THE BLACKJACK GAME")

	deck = Deck()
	deck.shuffle_deck()

	player_hands = Hand()
	player_hands.add_card(deck.deal())
	player_hands.add_card(deck.deal())

	dealer_hands = Hand()
	dealer_hands.add_card(deck.deal())
	dealer_hands.add_card(deck.deal())

	player_chips = Chips()
	take_bet(player_chips)

	show_some(player_hands,dealer_hands)

	while playing:
		stand_or_hint(deck,player_hands)
		show_some(player_hands,dealer_hands)
		if player_hands.value > 21:
			player_bust(player_hands,dealer_hands,player_chips)
			break
		if player_hands.value <= 21:

			while dealer_hands.value <= 17:
				hit(deck,dealer_hands)

			show_all(player_hands,dealer_hands)

			if dealer_hands.value > 21:
				dealer_bust(player_hands,dealer_hands,player_chips)
			elif dealer_hands.value > player_hands.value:
				dealer_win(player_hands,dealer_hands,player_chips)
			elif dealer_hands.value < player_hands.value:
				player_win(player_hands,dealer_hands,player_chips)
			else:
				print("you push")
			break
	print("\n player winnings stand at",player_chips.total)

	new_game = input("do you want to play again enter yes or no : ")

	if new_game[0].lower()== 'y':

		continue
	else:
		print("thank you for playing ")
		break

