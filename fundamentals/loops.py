secret_number = 9
guess_number = 0

while guess_number != secret_number:
    print("Guessing the number {guess_number}".format(guess_number=guess_number))
    guess_number+=1
    if guess_number == secret_number:
        print("Found the secret number: {secret_number}".format(secret_number=secret_number))