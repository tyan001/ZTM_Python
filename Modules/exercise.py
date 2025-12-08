import sys
import random
if __name__ == "__main__":
    
    num = random.randint(0,10)
    
    while True:
        try:
            guess = int(sys.argv[1])# first one at index 0 is always the file name
        except Exception as e:
            print(f"Getting this type of error {e}")
            break
        else:
            if guess == num:
                print('You guess correctly')
            else:
                print(f'Nice try the answer was {num}')
            break