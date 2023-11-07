from p1_random import P1Random

rng = P1Random()

game_continue = True
game_num = 0
player_wins = 0
dealer_wins = 0
ties = 0
# set up for stats

while game_continue:
    # 1. set up initial message that will read START GAME #1
    game_num += 1
    print("START GAME #", game_num)
    print("")  # will space out code
    player_hand = 0

    # 2. deals a card to the player randomly
    card = rng.next_int(13) + 1  # [1,13]
    # use if/elif/else chain for the card value
    if card == 1:
        print('Your card is a ACE!')
    elif 2 <= card <= 10:
        print(f'Your card is a {card}!')
    elif card == 11:
        print('Your card is a JACK!')
        card = 10
    elif card == 12:
        print('Your card is a QUEEN!')
        card = 10
    elif card == 13:
        print('Your card is a KING!')
        card = 10

    player_hand += card
    # will print hand value information from above
    print(f'Your hand is: {player_hand}')
    print("")
    # 3. keep asking users to choose the menu option so this while loop will continue going until no_winners is false
    no_winners = True
    while no_winners:
        print("1. Get another card")
        print('2. Hold hand')
        print('3. Print statistics')
        print('4. Exit')
        print("")
        # ask player to enter choice
        # need to use int(input()) for them to select the option number
        choice = int(input('Choose an option: '))
        print("")

        # if player wants another card
        if choice == 1:
            # deal a new card to the player
            card = rng.next_int(13) + 1  # [1,13]
            # use if/elif/else chain
            if card == 1:
                print('Your card is a ACE!')
            elif 2 <= card <= 10:
                print(f'Your card is a {card}!')
            elif card == 11:
                print('Your card is a JACK!')
                card = 10
            elif card == 12:
                print('Your card is a QUEEN!')
                card = 10
            elif card == 13:
                print('Your card is a KING!')
                card = 10

            player_hand += card
            print(f'Your hand is: {player_hand}')
            print("")
            # if layer_hand is equal to 21
            if player_hand == 21:
                no_winners = False
                print("BLACKJACK! You win!")
                player_wins += 1
                # track the number of games player wins
            # else if player_hand is greater than 21
            elif player_hand > 21:
                no_winners = False
                dealer_wins += 1
                print("You exceeded 21! You lose.")

        # if player wants to hold their hand
        elif choice == 2:
            # deal a card in [16,26] to the dealer
            dealer_hand = 0
            dealer_card = rng.next_int(11) + 16  # [16,26]
            dealer_hand += dealer_card
            # print hand value information
            print(f'Dealer\'s hand: {dealer_hand}')
            print(f'Your hand is: {player_hand}')
            print('')
            # compare dealer hand with player hand
            if player_hand > dealer_hand:
                no_winners = False
                player_wins += 1
                print('You win!')
                print('')
            elif dealer_hand > 21:
                no_winners = False
                player_wins += 1
                print('You win!')
                print('')
            elif player_hand < dealer_hand < 22:
                no_winners = False
                dealer_wins += 1
                print('Dealer wins!')
                print('')
            elif player_hand == dealer_hand:
                no_winners = False
                ties += 1
                print('It\'s a tie! No one wins!')
                print('')

        # if player wants to know their stats
        elif choice == 3:
            print(f'Number of Player wins: {player_wins}')
            print(f'Number of Dealer wins: {dealer_wins}')
            print(f'Number of tie games: {ties}')
            print(f'Total # of games played is: {game_num - 1}')
            tot_games = game_num - 1
            percent_won = player_wins / tot_games * 100
            print(f'Percentage of Player wins: {percent_won}%')
            print('')

        # if player wants to exit game
        elif choice == 4:
            no_winners = False
            game_continue = False

        else:
            print('Invalid input!')
            print('Please enter an integer value between 1 and 4.')