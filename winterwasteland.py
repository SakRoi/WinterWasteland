from player import PlayerInfo
from enemy import EnemyInfo
from combat import CombatSystem

if __name__ == "__main__":
    playerCharacter = PlayerInfo()
    playerCharacter.set_player_name()
    playerCharacter.take_player_heritage_choice()
    playerCharacter.print_player_character_template()
    test_enemy = EnemyInfo()
    test_combat = CombatSystem(playerCharacter)
    