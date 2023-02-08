
class CombatSystem:
    """A defination of the games combat system, is basically Rock Paper Scissors"""

    def __init__(self, player_character) -> None:
        self.player = player_character
        self.first_turn = True
        self.enemy = None
        self.last_player_choice = None
    
    def combat(self, enemy_entity):

        self.enemy = enemy_entity
        while self.enemy.enemy_health >= 1 or self.player.player_health >= 1:
            player_choice = self._player_combat_choice()
            enemy_choice = self._enemy_combat_choice(self.last_player_choice)
            #check who wins and deal damage to the loser or both if draw
            if player_choice == "Paper":
                self.enemy.enemy_health -= 1
                print(self.enemy.enemy_health)
            self.last_player_choice = player_choice
        print("You've slain the enemy!")
        self.enemy = None
        self.first_turn = True

    def _enemy_combat_choice(self, last_player_choice: str) -> str:
        if last_player_choice == None:
            return self._random_combat_AI()
        elif self.enemy.difficulty == "easy":
            return self._easy_combat_AI(last_player_choice)
        elif self.enemy.difficulty == "medium":
            return self._medium_combat_AI(last_player_choice)
    
    def _player_combat_choice(self) -> str:
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
        if self.first_turn == True:
            self.first_turn == False
            return "Rock"
            #commented out for testing purposes
            #return self._random_combat_AI()
        else:
            return "Rock"
    
    def _medium_combat_AI(self, last_player_choice: str) -> str:
        """
        helper method for medium difficulty combat AI.
        Copies the players last input to counter the
        counter move that player would play against the
        easy bot.
        """

        if self.first_turn == True:
            self.first_turn == False
            return self._random_combat_AI()
        else:
            return player_choice

    def _random_combat_AI(self) -> str:
        """Always returns a random choice from RPS"""
        
        #set to only return rock for testing purposes
        return "Rock"