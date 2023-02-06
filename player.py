

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

    def take_player_heritage_choice(self) -> None:
        """
        Takes players input, checks that it is an integer and then calls
        set player heritage with this input.
        """
        valid_choice = False
        while valid_choice != True:
            try:
                player_heritage_choice = int(input("What's our heritage? 1. Laestadian "))
            except:
                print("Invalid input, please enter a number")
            else:
                valid_choice = self.set_player_heritage()
                
    
    def set_player_heritage(self, player_heritage_choice: int) -> bool:
        if player_heritage_choice == 1:
            self.player_heritage = "Laestadian"
            return True
        else:
            self.player_heritage = "Unknown"

    def print_player_character_template(self) -> None:
        """A command to save the player's character as a template to be used later"""
        print(f"player_heritage = {self.player_heritage}\n")
        with open("PlayerTemplate.txt", "w") as PlayerTemplate:
            PlayerTemplate.write(f"player_name = {self.player_name}\n")
            PlayerTemplate.write(f"player_heritage = {self.player_heritage}\n")

playerCharacter = PlayerInfo()
playerCharacter.set_player_name()
playerCharacter.set_player_heritage()
playerCharacter.print_player_character_template()
