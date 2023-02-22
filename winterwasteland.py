import random

from player import PlayerInfo
from enemy import EnemyInfo
from combat import CombatSystem

if __name__ == "__main__":
    #set up the random seed generator for the game
    random.seed()

    playerCharacter = PlayerInfo()
    playerCharacter.set_player_name()
    playerCharacter.take_player_heritage_choice()
    playerCharacter.print_player_character_template()
    
    test_enemy = EnemyInfo()
    test_combat = CombatSystem(playerCharacter)
    test_combat.combat(test_enemy)