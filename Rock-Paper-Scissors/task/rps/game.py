import random


class RockPaperScissors:
    def __init__(self):
        self.users_input = None
        self.random_choice = None
        self.user_name = None
        self.current_score = None
        self.input_options = None
        self.options = ['rock', 'paper', 'scissors']
        self.winning_options = {
            'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
            'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
            'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
            'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
            'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
            'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
            'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
            'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
            'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
            'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
            'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
            'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
            'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
            'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
            'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}

    def input_data(self):
        self.users_input = input()
        if self.users_input == "!exit":
            print('Bye!')
        elif self.users_input == "!rating":
            print(f'Your rating: {self.current_score}')
        elif self.users_input not in self.options:
            print('Invalid input')
        else:
            self.random_option()

    def random_option(self):
        self.random_choice = random.choice(self.options)
        print(self.get_winner())

    def set_gaming_options(self):
        for option in self.input_options.split(','):
            if option not in self.options and option != '':
                self.options.append(option)
        print("Okay, let's start")

    def get_winner(self):
        if self.random_choice == self.users_input:
            self.current_score += 50
            return f"There is a draw ({self.random_choice})"
        elif self.random_choice in self.winning_options[self.users_input]:
            self.current_score += 100
            return f'Well done. The computer chose {self.random_choice} and failed'
        else:
            return f'Sorry, but the computer chose {self.random_choice}'

    def read_ratings(self):
        with open('rating.txt', 'r') as f:
            for line in f:
                line = line.split()
                if line[0] == self.user_name:
                    self.current_score = int(line[1])
                    break
                else:
                    self.current_score = 0

    def main(self):
        self.user_name = input('Enter your name:')
        print(f'Hello, {self.user_name}')
        self.read_ratings()
        self.input_options = input()
        self.set_gaming_options()
        while self.users_input != "!exit":
            self.input_data()


if __name__ == "__main__":
    test = RockPaperScissors()
    test.main()
