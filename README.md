Capstone project to feature a card game "Crib" coded in python.
# HOW TO RUN
python3 game.py -> currently draft.py<br>
Make sure you're in the project root folder<br>
run `python3 draft.py`<br>
The game should begin and run till completion.<br>
# OVERVIEW
The game has 3 main parts but generally follows the following flow:
- game setup: Hands, Box, cut card and scores are all intialised first.
- As soon as the Box is created, the game moves to the pegging stage.
- In this stage players place a card one at a time.
- After completed the players' hands and box are scored.
- The round ends and player scores are all added up.
- This entire functionality above repeats until game ends.
- Once a player reaches the winning score, the game interrupts and exits immediately declaring a winner.
# PLAN VS END RESULT
Main controller: main function + round_functionality function:
- tracks scores
- initialises hands, box and cut card from 1 randomised deck
- calls pegging stage, and subsequently all scoring functions
- exits for winner
- controls overall flow of the game, repeating rounds, deciding who's turn it is, adding scores...<br>

Scoring:
- Each stage has it's own scoring function, as each stage has slightly different scoring rules.
- scoring_calculation.py contains all the scoring functions.
- Scoring pairs and runs was especially difficult, each have their own associated file consequently.<br>

Cards:
- have their own type alias, are used at every single point.
- the main way cards are ranked, ordered, calculated for scores are by using lists.
# PLAN
A main game controller function/class, one to control the individual players too.
The main game controller should keep track of:
- scores
- cards on the board
- - The box "crib"
- - The Cut Card
- - The pegging progress
- HOW to score (different rules for card combos)
- the decks current contents (which cards gone)

The player controllers should keep track of:
- Players hand
- (not sure but communicate how much score the hand has? maybe function for this? also needs to update properly when cards are played)

# MAIN PROBLEMS INITIALLY
How to track a players cards
How to allow players to view and select their cards, view can be automatic at start of turn.
How to populate and persist the cards placed down.
How to keep a box alive
Some way/function to calculate the score of a certain move/hand.
- includes pegging to check whether player just got 15/pair/pair royale/flush
- includes box/hand with box having cut card too
- includes edge cases like jacks (nob and heel)
How to display updating score without just overcrowding the output terminal
- Becomes a problem when its last round and pegging scores might cause win, but score only displays end of rounds for simplicity.
