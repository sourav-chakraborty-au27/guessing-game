import random
num = random.randint(1,100)

print('Welcome to guess me!!')
print("I'm thinking of number 1 to 100")
print("If you guess within 10 of the number 'll notify 'Warm'")
print("If you guess more than 10 of the number 'll notify 'cold'")
print("if your guess is closer than the previous one will notify 'warmer' means coming closer, keep doing it")
print("if your guess is greater than the previous one will notify 'colder' means going away, don't do it")
guesses = [0]

while True:
    
    guess = int(input('I guessesed one, now its your turn. Guess a number between 1 to 100: '))

    if guess > 100 or guess < 1:
        print('Out of Bound')
        continue
    if guess == num:
        print(f'Congratulation! You guesses it in {len(guesses)} guess')
        break
    guesses.append(guess)

    if guesses[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print('warmer, going closer, keep doing it')
        else:
            print('colder, going away dont do it')
    else:
        if abs(num-guess) <= 10:
            print('warm, you are very close')
        else:
            print('cold, give a good try you are not close') 
