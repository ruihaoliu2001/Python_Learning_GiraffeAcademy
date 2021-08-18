
secret_word = "giraffe"
guess_word = ""
guess_limit = 3
guess_count = 0
out_of_guess = False

while guess_word != secret_word and not(out_of_guess):
    if guess_count < guess_limit:
        guess_word = input("Enter your guess: ")
        guess_count += 1
    else:
        out_of_guess = True

if not(out_of_guess):
    if guess_count == 1:
        print("You win! The time you guessed was " + str(guess_count))
    else:
        print("You win! The times you guessed were " + str(guess_count))
else:
    print("Out of guess, you lose!")


