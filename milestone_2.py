import random

def choose_random_word(word_list):
    return random.choice(word_list)

def get_user_input():
    return input("Enter a single letter: ")

def is_valid_guess(guess):
    return len(guess) == 1 and guess.isalpha()

def main():

favorite_fruits = ["Grapes", "Apple", "Orange", "Pineapple", "Banana"]

word_list = favorite_fruits

word = random.choice(word_list)
print("Randomly chosen word:", word)

guess = input("Enter a single letter: ")

 if is_valid_guess(guess):
        # Print a message for a valid input
        print("Good guess!")
    else:
        # Print a message for an invalid input
        print("Oops! That is not a valid input.")

if __name__ == "__main__":
    main()
