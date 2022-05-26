from jumper import Jumper
from secret_word import SecretWord
from terminal_service import TerminalService

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:    
        jumper (Jumper) The character that is showing correct and incorrect guesses.
        is_playing (boolean): Whether or not to keep playing.
        secrete_word (SecreteWord) The word that is going to be guessed.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._jumper = Jumper()
        self._is_playing = True
        self._secret_word = SecretWord()
        self._terminal_service = TerminalService()
        self._lives = 5

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        print()
        self._terminal_service.write_text("Welcome to the Jumper Game! Save the jumper by guessing correct letters!")
        self._terminal_service.write_text("An incorrect guess will start destroying the parachute. Be careful!")
        print()
       
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
        if self._lives > 0:
            self._jumper.winner()
        else: 
            self._jumper.lost()
            self._terminal_service.write_text(f'\nThe secret word was: "{self._secret_word._word}"')
            print()

    def _get_inputs(self):
        """
        Reads text from user, calling in secret word class.
        Args:
            self (Director): An instance of Director.
        """ 
        if self._secret_word._word == "":
            self._secret_word.word_selector()
            self._secret_word.draw_lines()
        self._jumper.get_parts((self._lives - 5) * -1)
        new_answer = self._terminal_service.read_text('\nGuess a letter [a-z]: ')
        self._secret_word.guess(new_answer)
        self._secret_word.check_answer()
       

    def _do_updates(self):
        """ Updates the lives of the jumper.
        Args:
            self (Director): An instance of Director.
        """
        self._lives = self._secret_word._lives


    def _do_outputs(self):
        """Looks at method in secret word to keep playing if player is still alive
        Args:
            self (Director): An instance of Director.
        """
        if not self._secret_word.is_alive():
            self._is_playing = False

       

