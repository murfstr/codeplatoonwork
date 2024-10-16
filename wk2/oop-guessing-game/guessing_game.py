class GuessingGame():
    def __init__(self, answer_number):
        self.answer_number = answer_number
        self.solved_status = False

    def guess(self, user_guess):
        if user_guess > self.answer_number:
            return 'high'
        elif user_guess == self.answer_number:
            self.solved_status = True
            return 'correct'
        else:
            return 'low'

    def solved(self):
        return self.solved_status

# new_game = GuessingGame(25)
# print(new_game.answer_number)


# game = GuessingGame(random.randint(1,100))
# last_guess  = None
# last_result = None

# while game.solved() == False:
#   if last_guess != None: 
#     print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
#     print("")

#   last_guess  = input("Enter your guess: ")
#   last_result = game.guess(last_guess)


# print(f"{last_guess} was correct!")