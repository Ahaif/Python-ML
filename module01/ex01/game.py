class GotCharacter:
    def __init__(self, first_name=None, is_alive=True):
        """
        A class representing a character in the Game of Thrones world.

        Parameters:
        - first_name (str): The first name of the character.
        - is_alive (bool): Indicates whether the character is alive (default is True).
        """
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        """
        A class representing the Stark family in the Game of Thrones world.

        Parameters:
        - first_name (str): The first name of the character.
        - is_alive (bool): Indicates whether the character is alive (default is True).
        """
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        """
        Prints the House words of the Stark family.
        """
        print(self.house_words)

    def die(self):
        """
        Changes the value of is_alive to False, indicating the character's death.
        """
        self.is_alive = False


# Example usage:
if __name__ == "__main__":
    arya = Stark("Arya")
    print(arya.__class__.__doc__)
    arya.print_house_words()
    print(arya.is_alive)
    arya.die()
    print(arya.is_alive)
