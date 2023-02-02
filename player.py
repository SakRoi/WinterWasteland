

class PlayerInfo:
    """The player info, includes such things as inventory, heritage and current state"""

    def __init__ (self) -> None:
        """Intializes player characters attributes"""
        player_name = ""
        player_heritage = ""
        player_health = 10
    
    def set_player_name(self) -> None:
        """A command to get the player character named"""
        self.player_name = input("What's our name? :")

    def set_player_heritage(self) -> None:
        """A command to get the player character's heritage"""
        player_heritage_choice = input("What's our heritage? 1. Laestadian ")
        if player_heritage_choice == 1:
            player_heritage = "Laestadian"
        else:
            player_heritage = "Unknown"

    def print_player_character_template(self) -> None:
        """A command to save the player's character as a template to be used later"""
        with open("PlayerTemplate.txt", "w") as PlayerTemplate:
            PlayerTemplate.write(f"player_name = {self.player_name}\n")
            #PlayerTemplate.write(f"player_heritage = {self.player_heritage}\n")
            #printing player_heritage for some reason doesn't work

playerCharacter = PlayerInfo()
playerCharacter.set_player_name()
playerCharacter.set_player_heritage()
playerCharacter.print_player_character_template()
