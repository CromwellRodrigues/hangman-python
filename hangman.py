import random
import stages
from logo import logo
from hangman_words import word_list


RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

encouragements = ["Nice!", "Great job!", "You're on fire!", "Keep going!"]
smh = ["Oops!", "Try again!", "Not quite!", "Better luck next time!"]


def play_hangman(): 
    stage = 0
    print(logo)

    # TODO  randomly choose word from word_list
    chosen_word = random.choice(word_list)
    # print(f"Chosen word : {chosen_word}")


    game_over = False

    correct_letters = set() 
    wrong_letters = set()


    while not game_over: 
        print(f"\n****** STAGE {stage}/6 OVER ******")
        
        # show current word state  
        display = "".join([char if char in correct_letters else " _ " for char in chosen_word])
        
        print(f"Word to guess : {display}")

        print(f"{RED}Wrong guesses: {', '.join(sorted(wrong_letters))}{RESET}")

        guess= input("Guess a letter: ").lower()
        
        # input validation 
        
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetical character.")
            continue
        
        if guess in correct_letters or guess in wrong_letters:
            print(f"You already guessed {guess}")
            continue
        
        if guess in chosen_word:
            correct_letters.add(guess)
            print(f" {GREEN}Good Guess ! {random.choice(encouragements)} !!: {guess}{RESET}")
            if all (char in correct_letters for char in chosen_word):
                print(f"\n{chosen_word}")
                print(f"\n🔴🟣🟡🟨⭕🔹🟩  {GREEN} You win! 🏆 {RESET} 🔵🔷🟠🔸🟢🔶🟪🪙")
                game_over = True
            continue
        
        else : 
            wrong_letters.add(guess)
            print(f" {RED} {random.choice(smh)} You guessed {guess}, that's not in the word. You lose a life.{RESET}")
            print(stages.stages[stage])  # Show current stage before incrementing
            stage += 1
            if stage == 6:
                print(f"********** {RED} You lose! 😢 {RESET} **********")
                print(f"\nThe word was: {chosen_word}\n")
                game_over = True

while True:     
    play_hangman() 
    
    replay = input("Do you want to play again ? (y/n): ")
    if replay != "y":
        
        print("Thanks for playing Hangman!") 
        
        break