import random
import os

class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

class HangmanPro:
    """A professional CLI Hangman game with ASCII art, OOP design, and robust validation."""
    
    def __init__(self):
        self.word_bank = ["PYTHON", "DEVELOPER", "ALGORITHM", "DATABASE", "ENCRYPTION"]
        self.max_attempts = 6
        self.hangman_art = [
            "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="
        ]

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def play(self):
        self.clear_screen()
        word = random.choice(self.word_bank)
        guessed_letters = set()
        wrong_guesses = 0

        print(f"{Colors.BOLD}{Colors.CYAN}=== PRO HANGMAN ==={Colors.RESET}")
        
        while wrong_guesses < self.max_attempts:
            print(f"{Colors.RED}{self.hangman_art[wrong_guesses]}{Colors.RESET}")
            
            display = "".join([char if char in guessed_letters else "_" for char in word])
            print(f"\n{Colors.BOLD}Word: {Colors.CYAN}{' '.join(display)}{Colors.RESET}")
            print(f"{Colors.YELLOW}Guessed Letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}{Colors.RESET}")
            
            if "_" not in display:
                print(f"\n{Colors.GREEN}{Colors.BOLD}🏆 VICTORY! You guessed the word '{word}'!{Colors.RESET}")
                return

            guess = input(f"\n{Colors.BOLD}Enter a letter: {Colors.RESET}").upper().strip()

            if len(guess) != 1 or not guess.isalpha():
                print(f"{Colors.RED}⚠ Invalid input. Please enter a single alphabetical character.{Colors.RESET}")
                continue
            if guess in guessed_letters:
                print(f"{Colors.YELLOW}⚠ You already guessed '{guess}'.{Colors.RESET}")
                continue

            guessed_letters.add(guess)

            if guess not in word:
                wrong_guesses += 1
                print(f"{Colors.RED}❌ Incorrect! '{guess}' is not in the word.{Colors.RESET}")
            else:
                print(f"{Colors.GREEN}✅ Correct guess!{Colors.RESET}")
                
        print(f"{Colors.RED}{self.hangman_art[wrong_guesses]}{Colors.RESET}")
        print(f"\n{Colors.RED}{Colors.BOLD}💀 GAME OVER! The word was '{word}'.{Colors.RESET}")

if __name__ == '__main__':
    game = HangmanPro()
    game.play()
