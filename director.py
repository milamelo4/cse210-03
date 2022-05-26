from jumper import Jumper
from secret_word import SecretWord
from terminal_service import TerminalService
import random

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
        self.lives = 5

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
        if self.lives > 0:
            self._jumper.winner()
        else: 
            self._jumper.lost()

    def _get_inputs(self):
        """
        Reads text from user, calling in secret word class.
        Args:
            self (Director): An instance of Director.
        """ 
        if self._secret_word.word == "":
            self._secret_word.word_selector()
            self._secret_word.draw_lines()
        self._jumper.get_parts((self.lives - 5) * -1)
        new_answer = self._terminal_service.read_text('\nGuess a letter: ')
        self._secret_word.guess(new_answer)
        self._secret_word.check_answer()

    def _do_updates(self):
        """
        Args:
            self (Director): An instance of Director.
        """
        self.lives = self._secret_word.lives

    def _do_outputs(self):
        """
        Args:
            self (Director): An instance of Director.
        """
        if not self._secret_word.is_alive():
            self._is_playing = False

       

