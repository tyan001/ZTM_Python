import random

answer = random.randint(1, 11)


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print("guess correctly")
            return True
    else:
        print("gg, thanks for the number not between 1-10")
        return False


if __name__ == "__main__":
    while True:
        try:
            guess = int(input("guess a number from 1 - 10"))
            if run_guess(guess, answer):
                break
        except ValueError:  
            print("please enter a numer")
