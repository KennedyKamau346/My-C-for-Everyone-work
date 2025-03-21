# Guessing game in Python
while True:
    try:
        line = input()
    except:   # if we get EOF
        break
    line = line.strip()
    guess = int(line)
    if guess == 42:
        print("Nice Work!")
        break
    elif guess < 42 :
        print("Too low - guess again")
    else :
        print("Too high - guess again")
