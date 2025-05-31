#esercizio9_15
from random import choice  # Import function to randomly select items

class LotteryMachine:
    def __init__(self) -> None:
        self.pool: list[str] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'a', 'b', 'c', 'd', 'e']  # Combined pool of numbers and letters
        self.winning_ticket: list[str] = []  
    def draw_winning_ticket(self) -> list[str]:
        self.winning_ticket = []
        while len(self.winning_ticket) < 4:
            pulled: str = choice(self.pool)
            if pulled not in self.winning_ticket:
                self.winning_ticket.append(pulled)

        return self.winning_ticket

    def announce_winner(self) -> None:
        print("The winning ticket is:", self.winning_ticket)
        print("Any ticket matching these 4 items wins a prize!")


    def simulate_until_win(self, my_ticket: list[str]) -> tuple[int, list[str]]:
        attempts = 0
        while True:
            new_ticket = self.draw_winning_ticket()
            attempts += 1
            if sorted(new_ticket) == sorted(my_ticket):
                return attempts, new_ticket

my_ticket: list[str] = ['3', 'a', '7', 'd']


machine = LotteryMachine()
attempts, winning_ticket = machine.simulate_until_win(my_ticket)

print(f"Your ticket: {my_ticket}")
print(f"Winning ticket: {winning_ticket}")
print(f"It took {attempts} attempts to win.")
