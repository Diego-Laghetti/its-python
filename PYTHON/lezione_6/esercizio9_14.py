#esercizio9_14
from random import choice

class LotteryMachine:
    def __init__(self) -> None:
        self.pool: list[str] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'a', 'b', 'c', 'd', 'e'] 
        self.winning_ticket: list[str] = []  

    def draw_winning_ticket(self) -> None:
        while len(self.winning_ticket) < 4:
            pulled: str = choice(self.pool)
            if pulled not in self.winning_ticket:
                self.winning_ticket.append(pulled)

    def winning_message(self) -> str:
        print("The winning ticket is:", self.winning_ticket)
        print("Any ticket matching the winning 4 items wins a prize!!!")

lottery = LotteryMachine()
lottery.draw_winning_ticket() 
lottery.winning_message()



    


