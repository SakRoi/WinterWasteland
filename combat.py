import random

class CombatSystem:
    """A defination of the games combat system, is basically Rock Paper Scissors"""

    def __init__(self, player_character) -> None:
        "intialization of the player character into the class"
        self.player = player_character
        self.enemy = None
        self.last_player_choice = None

        self.combat_win_dictionary = {
            "Rock":"Scissor",
            "Scissor":"Paper",
            "Paper":"Rock"
        }
        
        self.random_combat_ai_dictionary = {
            1:"Rock",
            2:"Paper",
            3:"Scissor"
        }

    def combat(self, enemy_entity) -> None:
        """A callable method for enemy encounters in the wasteland"""
        self.enemy = enemy_entity
        while self.enemy.enemy_health >= 1 and self.player.player_health >= 1:
            player_choice = self._player_combat_choice()
            enemy_choice = self._enemy_combat_choice(self.last_player_choice)
            self._hit_checker(player_choice, enemy_choice)
        print("You've slain the enemy!")
        self.enemy = None
        self.last_player_choice = None

    def _enemy_combat_choice(self, last_player_choice: str) -> str:
        """Chooses an appropriate AI for the enemy. Note that random and hard are the same"""
        if last_player_choice == None or self.enemy.enemy_difficulty == "hard":
            return self._random_combat_AI()
        elif self.enemy.enemy_difficulty == "easy":
            return self._easy_combat_AI(last_player_choice)
        elif self.enemy.enemy_difficulty == "medium":
            return self._medium_combat_AI(last_player_choice)
    
    def _player_combat_choice(self) -> str:
        """Get's player's input and validates it before using the selection against AI"""
        choice = ""
        while True:
            choice = input("Select from rock, paper or scissor: ").strip().title()
            if choice in ["Rock", "Paper", "Scissor"]:
                break
            else:
                print("Invalid input.")
        return choice
    
    def _easy_combat_AI(self, last_player_choice: str) -> str:
        """
        Easy combat AI helper method. Always tries to counter
        the player's move. E.g. If player chose paper last
        round, chooses scissors this round
        """

        # due to the combat_win_dictionary being win-lose and not lose-win,
        # we need to input last_losing_move back into the dictionary and use
        # it's value as the move

        last_losing_move = self.combat_win_dictionary[last_player_choice]
        current_predicted_winning_move = self.combat_win_dictionary[last_losing_move]

        return current_predicted_winning_move
    
    def _medium_combat_AI(self, last_player_choice: str) -> str:
        """
        helper method for medium difficulty combat AI.
        Copies the players last input to counter the
        counter move that player would play against the
        easy bot.
        """
        return last_player_choice

    def _random_combat_AI(self) -> str:
        """Always returns a random choice from RPS"""
        
        random_number = random.randint(1, 3)
        print(random_number)
        random_choice = self.random_combat_ai_dictionary[random_number]
        
        return random_choice

    def _hit_checker(self, player_choice: str, enemy_choice: str,) -> None:
        """check who wins and deal damage to the loser or both if draw,"""

        print(f"The enemy chose {enemy_choice}!")
        print(f"You chose {player_choice}!")

        if enemy_choice == player_choice:
            print("You both get scratched!")
            self.player.player_health -= self.enemy.enemy_damage//2
            self.enemy.enemy_health -= 1    
        elif enemy_choice == self.combat_win_dictionary[player_choice]:
            print("you hit the enemy!")
            self.enemy.enemy_health -= 1
        else:
            print("The enemy hits you!")
            self.player.player_health -= self.enemy.enemy_damage
        
        print(f"Player health: {self.player.player_health}")
        print(f"Enemy health: {self.enemy.enemy_health}")
        self.last_player_choice = player_choice