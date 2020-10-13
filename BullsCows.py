import random

def randomize_start():
    digits = set(range(10))
    first = random.randint(1, 9)
    others = random.sample(digits - {first},3)
    #print(str(first)+''.join(map(str,others)))
    game_number = str(first)+''.join(map(str,others))
    return game_number
    # print(game_number)

def error_check(attempt_count):
    while True:
        try:
            input_number = input("\nEnter a 4 digit number for attempt #" + str(attempt_count) + ": ")
            if len(input_number) == 4:
                if type(int(input_number)) is int:
                    flag = 0
                    for i in range(len(input_number)):
                        flag = input_number.count(input_number[i])
                        if flag > 1:
                            raise Exception
                    break
            else: raise TypeError
        except ValueError:
            print("Incorrect entry")
        except TypeError:
            print("Not a 4 digit number")
        except Exception:
            print("Enter unique digits in your 4-digit number")

    return input_number

def logic_check(input_number_2, game_number_2, attempts_2):
    bull = 0
    cow = 0
    for j in range(len(game_number_2)):
        if input_number_2[j] == game_number_2[j]:
            bull = bull + 1
        elif input_number_2[j] in game_number_2:
            cow = cow + 1

    print(input_number_2 + " -> " + "Bull: " + str(bull) + ", " + "Cow: " + str(cow))
    if bull == 4:
        print("You guessed the correct number in "+ str(attempts_2)+" attempts.")
        return bull
    #     exit()
    # else:
    #     return bull

game_attempts = 0
session_attempts = 0
game_count = 0
best_attempt = 999
game_number_2 = randomize_start()
while True:
    game_attempts = game_attempts + 1
    user_input = error_check(game_attempts)
    bull_confirm = logic_check(user_input, game_number_2, game_attempts)
    if bull_confirm == 4:
        game_count = game_count + 1
        if game_attempts < best_attempt:
            best_attempt = game_attempts
        session_attempts = session_attempts + game_attempts
        game_attempts = 0
        resume = input("\nDo you want to play again? (Type y if yes):"+"\t")
        if resume != 'y':
            print("\n" + "Session Details:" + "\n" + "1. Games Played: " + str(game_count) + "\n2. Best Result: "+ str(best_attempt) + " attempts" + "\n3. Average Attempts: " +
                  str(round(session_attempts/game_count,1)) + " per game")
            break
        else: game_number_2 = randomize_start()
