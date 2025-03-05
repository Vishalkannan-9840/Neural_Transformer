import random
import hangman_word
import hangman_art


def word_list():
    hangman_words.word_list()

def art():
    hangman_art.stages()

lives = 6

print(hangman_art.logo)
chosen_word = random.choice(hangman_word.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"you have {lives} lives left")
    guess = input("Guess a letter: ").lower()
    print(f"You have entered {guess}")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You Guessed {guess}, That is not in the word.you lost a life")
        if lives == 0:
            game_over = True
            print(f"The correct word is {chosen_word}")

    if "_" not in display:
        game_over = True
        print("YAY!!,you guessed it correctly you won!!!!")
    print(hangman_art.stages[lives])
