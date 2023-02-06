

class PlayerInfo:
    """The player info, includes such things as inventory, heritage and current state"""

    def __init__ (self) -> None:
        """Intializes player characters attributes"""
        player_name = ""
        player_heritage = ""
        player_health = 10
    
    def set_player_name(self) -> None:
        """A command to get the player character named"""
        self.player_name = input("What's our name?\n")

    def take_player_heritage_choice(self) -> None:
        """
        Takes players input, checks that it is an integer and then calls
        set player heritage with this input.
        """
        valid_choice = False
        while valid_choice != True:
            try:
                player_heritage_choice = int(input("What's our heritage? \n1. Oulu\n\
2. Heikki\n3. Rova\n4. Swedish\n5. Rad Scav\n"))
            except:
                print("Invalid input, enter a number and try again")
            else:
                valid_choice = self.set_player_heritage(player_heritage_choice)
                
    
    def set_player_heritage(self, player_heritage_choice: int) -> bool:
        """
        Check input against a if-else clauses, set
        a heritage and return a bool.
        Numbers from 1-5 return True while others return False,
        as they do not have a heritage set to them.
        """
        #TODO add information about the different heritages to different methods which can then be called here.
        if player_heritage_choice == 1:
            self.player_heritage = "Oulu"
            return True
        elif player_heritage_choice == 2:
            self.player_heritage = "Heikki"
            return True
        elif player_heritage_choice == 3:
            self.player_heritage = "Rova"
            return True
        elif player_heritage_choice == 4:
            self.player_heritage = "Swedish"
            return True
        elif player_heritage_choice == 5:
            self.player_heritage = "Rad Scav"
            return True
        else:
            print("Invalid choice, try again:")
            return False
            

    def print_player_character_template(self) -> None:
        """A command to save the player's character as a template to be used later"""
        print(f"player_heritage = {self.player_heritage}\n")
        with open("PlayerTemplate.txt", "w") as PlayerTemplate:
            PlayerTemplate.write(f"player_name = {self.player_name}\n")
            PlayerTemplate.write(f"player_heritage = {self.player_heritage}\n")

playerCharacter = PlayerInfo()
playerCharacter.set_player_name()
playerCharacter.take_player_heritage_choice()
playerCharacter.print_player_character_template()
