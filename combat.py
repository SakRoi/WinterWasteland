
class CombatSystem:
    """A defination of the games combat system, is basically Rock Paper Scissors"""

    def __init__(self, player_character) -> None:
        self.player = player_character
        self.first_turn = True
        self.enemy = None
        self.last_player_choice = None
    
    def combat(self, enemy_entity):

        self.enemy = enemy_entity
        while self.enemy.health >= 1 or self.player.health >= 1:
            player_choice = self._player_combat_choice()
            enemy_choice = _enemy_combat_choice(self.last_player_choice)
            #check who wins and deal damage to the loser or both if draw
    
            self.last_player_choice = player_choice

    
    def _enemy_combat_choice(self, player_choice: str) -> str:
        if player_choice == None:
            return self._random_combat_AI()
        elif self.enemy.difficulty == "easy":
            return self._easy_combat_AI(player_choice)
        elif self.enemy.difficulty == "medium":
            return self._medium_combat_AI(player_choice)
        
    
    def _player_combat_choice(self) -> str:
        return choice
    
    def _easy_combat_AI(self, player_choice: str) -> str:
        if self.first_turn == True:
            self._random_combat_AI()
        else:
    
    def _medium_combat_AI(self, player_choice: str) -> str:
        """
        helper method for medium difficulty combat AI.
        Copies the players last input to counter the
        counter move that player would play against the
        easy bot.
        """
        
        if self.first_turn == True:
            return self._random_combat_AI()
        else:
            return player_choice

    def _random_combat_AI(self) -> str:
        """Always returns a random choice from RPS"""
        
        return choice