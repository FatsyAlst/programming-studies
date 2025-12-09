# ===================================
# MARBLE TRADING GAME - GAMBLING SIMULATOR
# ===================================
# Scrimba Python 101 Course - Project 3
# A probability-based betting game where players draw marbles from a bag
# Green marbles win, red marbles lose - manage your gold wisely!

import random

# ===================================
# STEP 1: GAME SETUP - INITIALIZE VARIABLES
# ===================================

# Create a bag with 10 marbles (6 green = 60% win chance, 4 red = 40% lose chance)
bag = ('green', 'green', 'green', 'green', 'green', 'green', 'red', 'red', 'red', 'red')

# Starting amount of money (gold pieces)
start_purse = 1000

# Current money amount (tracks throughout game)
purse = start_purse

# Result of last round (positive for win, negative for loss)
result = 0

# How many rounds the player gets
rounds = 3

# Last marble drawn (used for display purposes)
marble = 'none'


# ===================================
# STEP 2: WELCOME MESSAGE
# ===================================
# Inform player of starting conditions
print(f'You start the game with {start_purse} gold pieces.')


# ===================================
# STEP 3: MAIN GAME LOOP
# ===================================
# Loop through each round, allowing player to bet and draw marbles

for draw in range(1, rounds + 1):
    # ===================================
    # STEP 3A: GET PLAYER'S BET
    # ===================================
    # Display current status and prompt for bet amount
    bet = int(input(f'''Current purse: {purse} | Last draw: {marble}
Round {draw} - How much do you want to bet?: 
'''))
    
    # ===================================
    # STEP 3B: DRAW MARBLE RANDOMLY
    # ===================================
    # Randomly select one marble from the bag
    marble = random.choice(bag)
    
    # ===================================
    # STEP 3C: DETERMINE WIN OR LOSS
    # ===================================
    # Green marble = win (gain the bet amount)
    # Red marble = loss (lose the bet amount)
    if marble == 'green':
        result = bet  # Positive value (gain)
    else:
        result = -bet  # Negative value (loss)
    
    # ===================================
    # STEP 3D: UPDATE PURSE
    # ===================================
    # Add result to purse (positive for win, negative for loss)
    purse += result
    
    # ===================================
    # STEP 3E: CHECK GAME OVER CONDITION
    # ===================================
    # Lose game if purse drops below 50% of starting amount
    if purse < 0.5 * start_purse:
        print(f'Game over! You lost too much gold!!!')
        break  # Exit the game loop early
    
    # ===================================
    # STEP 3F: DISPLAY ROUND RESULTS
    # ===================================
    # Show current purse, marble drawn, and win/loss amount
    print(f'Purse: {purse} | Last result: ({marble}): {result}')
    print('')  # Blank line for readability


# ===================================
# STEP 4: DISPLAY FINAL RESULTS
# ===================================
# Show starting vs ending amounts and calculate percentage gain/loss
print('starting/ ending purse: ', start_purse, '/', purse)
print('gain/loss ', ((purse - start_purse)/start_purse*100),'%')


# ===================================
# EXAMPLE OUTPUT
# ===================================
# You start the game with 1000 gold pieces.
# Current purse: 1000 | Last draw: none
# Round 1 - How much do you want to bet?: 
# 100
# Purse: 1100 | Last result: (green): 100
#
# Current purse: 1100 | Last draw: green
# Round 2 - How much do you want to bet?: 
# 200
# Purse: 900 | Last result: (red): -200
#
# Current purse: 900 | Last draw: red
# Round 3 - How much do you want to bet?: 
# 150
# Purse: 1050 | Last result: (green): 150
#
# starting/ ending purse:  1000 / 1050
# gain/loss  5.0 %


# ===================================
# GAME MECHANICS EXPLAINED
# ===================================
# Probability:
# - 6 green marbles out of 10 = 60% chance to win
# - 4 red marbles out of 10 = 40% chance to lose
# 
# Expected value per bet:
# - (0.6 × bet) + (0.4 × -bet) = 0.2 × bet
# - Positive expected value: Player has advantage!
#
# Game Over Condition:
# - If purse < 500 (50% of 1000), game ends early
# - Prevents total bankruptcy
#
# Strategy Tips:
# - Bet conservatively to avoid hitting the 50% limit
# - House edge favors player (60% win rate)
# - Risk management is key


# ===================================
# CONCEPTS USED IN THIS PROJECT
# ===================================
# 1. Tuple - Immutable bag of marbles
# 2. random.choice() - Random selection from sequence
# 3. Variables - Tracking game state (purse, result, marble)
# 4. for loop with range() - Iterating through rounds
# 5. range(1, n+1) - Starting loop from 1 instead of 0
# 6. input() with int() - Getting numeric user input
# 7. Multi-line f-strings with ''' - Formatted prompts
# 8. Conditional logic - if/else for win/loss determination
# 9. Mathematical operations - Addition, subtraction, percentages
# 10. break statement - Early game termination
# 11. Comparison operators - Checking game over condition
# 12. String formatting - Displaying results with f-strings


# ===================================
# FUTURE IMPROVEMENT CHALLENGES
# ===================================

# CHALLENGE 1: INPUT VALIDATION & ERROR HANDLING
# -----------------------------------------------
# Goal: Prevent invalid bets and crashes
# Tasks:
# - Validate bet is a positive integer
# - Prevent betting more than current purse
# - Set minimum bet amount (e.g., 10 gold)
# - Handle non-numeric input with try-except
# - Add "quit game" option during bet prompt
# - Warn if bet is more than 50% of purse
# Skills practiced: Input validation, exception handling, defensive programming

# CHALLENGE 2: VARIABLE DIFFICULTY MODES
# ---------------------------------------
# Goal: Add different game difficulties
# Tasks:
# - Easy mode: 7 green, 3 red (70% win rate)
# - Normal mode: 6 green, 4 red (60% win rate) - current
# - Hard mode: 5 green, 5 red (50% win rate)
# - Expert mode: 4 green, 6 red (40% win rate)
# - Let user choose difficulty at start
# - Adjust starting purse based on difficulty
# - Display probability percentages to player
# Skills practiced: Tuples, menu systems, game balance, probability

# CHALLENGE 3: BETTING STRATEGIES & HINTS
# ----------------------------------------
# Goal: Teach probability and strategy
# Tasks:
# - Calculate and show expected value of bet
# - Suggest optimal bet size based on purse
# - Track and display win/loss streaks
# - Show statistics (wins vs losses, win rate)
# - Add "Strategy Guide" explaining probability
# - Implement Kelly Criterion betting suggestion
# Skills practiced: Mathematics, statistics, strategy algorithms

# CHALLENGE 4: ENHANCED GAME LOOP
# --------------------------------
# Goal: Make rounds more dynamic
# Tasks:
# - Allow player to choose number of rounds at start
# - Add "Continue playing?" prompt after rounds complete
# - Implement round-based achievements (5 wins in a row)
# - Add bonus rounds with special conditions
# - Create sudden death mode (one loss = game over)
# Skills practiced: Game loop design, user choices, dynamic gameplay

# CHALLENGE 5: MARBLE BAG VARIATIONS
# -----------------------------------
# Goal: Add variety to marble types and outcomes
# Tasks:
# - Add gold marble (rare, 3x win multiplier)
# - Add blue marble (push - bet returned, no win/loss)
# - Add black marble (instant game over)
# - Let player choose bag composition before game
# - Implement "marble reveal" showing remaining marbles
# - Add "draw without replacement" mode (marbles removed)
# Skills practiced: Lists vs tuples, complex game mechanics, list manipulation

# CHALLENGE 6: COMPREHENSIVE STATISTICS
# --------------------------------------
# Goal: Track and display detailed analytics
# Tasks:
# - Track every bet, result, and marble drawn
# - Calculate actual win rate vs expected
# - Show largest win and largest loss
# - Display average bet size
# - Create bar chart of wins/losses using ASCII
# - Export game history to CSV file
# Skills practiced: Data tracking, statistics, file I/O, visualization

# CHALLENGE 7: SAVE/LOAD GAME SYSTEM
# -----------------------------------
# Goal: Allow persistent gameplay
# Tasks:
# - Save game state to JSON file (purse, round, history)
# - Load previous game on startup if exists
# - Track total earnings across all sessions
# - Create player profiles with names
# - Implement leaderboard for best performances
# - Add "Reset all progress" option
# Skills practiced: File I/O, JSON, data persistence, user profiles

# CHALLENGE 8: ANIMATION & VISUAL EFFECTS
# ----------------------------------------
# Goal: Make the game more engaging visually
# Tasks:
# - Add "drawing marble" animation (suspense dots: ...)
# - Clear screen between rounds for cleaner display
# - Use colors: green text for wins, red for losses
# - Create ASCII art marble bag visual
# - Add progress bar showing purse as percentage of start
# - Animate purse changes (counting up/down)
# Skills practiced: Terminal animation, ANSI colors, ASCII art, user experience

# CHALLENGE 9: MULTIPLAYER MODE
# ------------------------------
# Goal: Enable competitive play
# Tasks:
# - Two players take turns betting and drawing
# - Each player has separate purse
# - Declare winner after all rounds
# - Add "steal mode" where winners take from losers
# - Implement tournament bracket for 4+ players
# - Track head-to-head records
# Skills practiced: Multi-user systems, turn management, competitive logic

# CHALLENGE 10: RISK MANAGEMENT FEATURES
# ---------------------------------------
# Goal: Teach responsible gambling concepts
# Tasks:
# - Add "Insurance" - pay small fee to protect against losses
# - Implement "Stop Loss" - auto-stop at specific loss amount
# - Add "Take Profit" - auto-stop at specific gain amount
# - Create "Quit While Ahead" achievement for stopping with profit
# - Show risk level indicator for each bet (low/medium/high)
# Skills practiced: Risk management, financial concepts, responsible gaming

# CHALLENGE 11: POWER-UPS & SPECIAL ABILITIES
# --------------------------------------------
# Goal: Add strategic depth with special items
# Tasks:
# - "Peek" power-up: See next marble before betting (1 use)
# - "Double Down": 2x multiplier on next win (risky)
# - "Insurance": Protect one bet from losses
# - "Mulligan": Redraw marble once per game
# - Power-ups cost gold or earned through achievements
# - Balanced economy for power-up costs
# Skills practiced: Game design, balance, inventory systems

# CHALLENGE 12: OBJECT-ORIENTED REFACTOR
# ---------------------------------------
# Goal: Restructure using OOP principles
# Tasks:
# - Create Game class with bag, purse, rounds
# - Create Player class with name, purse, stats
# - Create MarbleBag class with draw() and reset() methods
# - Create Round class to encapsulate each betting round
# - Implement GameHistory class for tracking
# - Use inheritance for different game modes
# Skills practiced: OOP, classes, methods, inheritance, encapsulation

# CHALLENGE 13: PROBABILITY SIMULATOR
# ------------------------------------
# Goal: Educational tool for understanding probability
# Tasks:
# - Add "Simulation Mode" - auto-bet and run 1000 times
# - Show convergence to expected value
# - Graph distribution of results
# - Test different betting strategies automatically
# - Compare fixed vs variable bet sizing
# - Demonstrate law of large numbers
# Skills practiced: Simulation, probability theory, data analysis, graphing

# CHALLENGE 14: PROGRESSIVE JACKPOT
# ----------------------------------
# Goal: Add exciting big win potential
# Tasks:
# - Small portion of each bet goes to jackpot pool
# - Special "jackpot marble" added to bag (very rare)
# - Drawing jackpot marble wins entire pool
# - Jackpot carries over between games
# - Show growing jackpot amount in game display
# - Reset jackpot after win
# Skills practiced: Persistent data, rare events, excitement mechanics

# CHALLENGE 15: ACHIEVEMENTS & PROGRESSION
# -----------------------------------------
# Goal: Gamify the experience with goals
# Tasks:
# - Award badges: "First Win", "High Roller", "Comeback Kid"
# - Track milestones: 10 games played, 1000 gold earned
# - Unlock new marble bags with achievements
# - Create achievement showcase/trophy room
# - Add XP system and player levels
# - Unlock new features at higher levels
# Skills practiced: Gamification, progression systems, persistent data

# BONUS CHALLENGE: CASINO SIMULATION
# -----------------------------------
# Goal: Expand into full casino game collection
# Tasks:
# - Add Roulette game with betting options
# - Implement Blackjack with basic strategy
# - Create Slot Machine mini-game
# - Add Dice game (Craps simplified)
# - Shared gold wallet across all games
# - Compare house edge across different games
# Skills practiced: Multiple game implementations, game variety, casino mathematics