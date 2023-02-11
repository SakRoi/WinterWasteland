
class CombatSystem:
    """A defination of the games combat system, is basically Rock Paper Scissors"""

    def __init__(self, player_character) -> None:
        "intialization of the player character into the class"
        self.player = player_character
        self.enemy = None
        self.last_player_choice = None
    
    def combat(self, enemy_entity) -> None:
        """A callable method for enemy encounters in the wasteland"""
        self.enemy = enemy_entity
        while self.enemy.enemy_health >= 1 and self.player.player_health >= 1:
            player_choice = self._player_combat_choice()
            enemy_choice = self._enemy_combat_choice(self.last_player_choice)

            #check who wins and deal damage to the loser or both if draw, this right now is very simple
            print(f"The enemy chose {enemy_choice}!")
            print(f"You chose {player_choice}!")

            #TODO make this smarter and refactor!!!
            #Win
            if player_choice == "Paper":
                print("you hit the enemy!")
                self.enemy.enemy_health -= 1
            #Loss
            elif player_choice == "Scissor":
                print("The enemy hits you!")
                self.player.player_health -= self.enemy.enemy_damage
            #Draw
            elif player_choice == "Rock": 
                print("You both get scratched!")
                self.player.player_health -= self.enemy.enemy_damage//2
                self.enemy.enemy_health -= 1
            
            print(f"Player health: {self.player.player_health}")
            print(f"Enemy health: {self.enemy.enemy_health}")
            self.last_player_choice = player_choice
            #
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
        """Easy combat AI"""
        #always returns rock for testing purposes
        #return self._random_combat_AI()
        return "Rock"
    
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
        
        #set to only return rock for testing purposes
        return "Rock"