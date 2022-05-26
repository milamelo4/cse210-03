import random

class SecretWord:
    """The responislity of the secret word it to get a random word from a list, and draw lines for the guesser. It also checks if the guess is in the secret word
    Attributes:
        word_list = the list of words to pull from
        lives = how many times the player can guess a wrong answer
        answer = pulled from the director file as the guess from the player
        letters = the list of letters from the randomly chosen word
        lines = list of dashes that indicate how many letters are in the word and signal the player what has not been guessed
        lines_count = variable in check_answer method to loop through the list of lines
        word = the randomly chosen word
    """
    def __init__(self):  
        self._word_list = [
            'wares',
            'soup',
            'mount',
            'extend',
            'brown',
            'expert',
            'tired',
            'humidity',
            'backpack',
            'crust',
            'dent',
            'market',
            'knock',
            'smite',
            'windy',
            'coin',
            'throw',
            'silence',
            'bluff',
            'downfall',
            'climb',
            'lying',
            'weaver',
            'snob',
            'kickoff',
            'match',
            'quaker',
            'foreman',
            'excite',
            'thinking',
            'mend',
            'allergen',
            'pruning',
            'coat',
            'emerald',
            'coherent',
            'manic',
            'multiple',
            'square',
            'funded',
            'funnel',
            'sailing',
            'dream',
            'mutation',
            'strict',
            'mystic',
            'film',
            'guide',
            'strain',
            'bishop',
            'settle',
            'plateau',
            'emigrate',
            'marching',
            'optimal',
            'medley',
            'endanger',
            'wick',
            'condone',
            'schema',
            'rage',
            'figure',
            'plague',
            'aloof',
            'there',
            'reusable',
            'refinery',
            'suffer',
            'affirm',
            'captive',
            'flipping',
            'prolong',
            'main',
            'coral',
            'dinner',
            'rabbit',
            'chill',
            'seed',
            'born',
            'shampoo',
            'italian',
            'giggle',
            'roost',
            'palm',
            'globe',
            'wise',
            'grandson',
            'running',
            'sunlight',
            'spending',
            'crunch',
            'tangle',
            'forego',
            'tailor',
            'divinity',
            'probe',
            'bearded',
            'premium',
            'featured',
            'serve',
            'borrower',
            'examine',
            'legal',
            'outlive',
            'unnamed',
            'unending',
            'snow',
            'whisper',
            'bundle',
            'bracket',
            'deny',
            'blurred',
            'pentagon',
            'reformed',
            'polarity',
            'jumping',
            'gain',
            'laundry',
            'hobble',
            'culture',
            'whittle',
            'docket',
            'mayhem',
            'build',
            'peel',
            'board',
            'keen',
            'glorious',
            'singular',
            'cavalry',
            'present',
            'cold',
            'hook',
            'salted',
            'just',
            'dumpling',
            'glimmer',
            'drowning',
            'admiral',
            'sketch',
            'subject',
            'upright',
            'sunshine',
            'slide',
            'calamity',
            'gurney',
            'adult',
            'adore',
            'weld',
            'masking',
            'print',
            'wishful',
            'foyer',
            'tofu',
            'machete',
            'diced',
            'behemoth',
            'rout',
            'midwife',
            'neglect',
            'mass',
            'game',
            'stocking',
            'folly',
            'action',
            'bubbling',
            'scented',
            'sprinter',
            'bingo',
            'egyptian',
            'comedy',
            'rung',
            'outdated',
            'radical',
            'escalate',
            'mutter',
            'desert',
            'memento',
            'kayak',
            'talon',
            'portion',
            'affirm',
            'dashing',
            'fare',
            'battle',
            'pupil',
            'rite',
            'smash',
            'true',
            'entrance',
            'counting',
            'peruse',
            'dioxide',
            'hermit',
            'carving',
            'backyard',
            'homeless',
            'medley',
            'packet',
            'tickle',
            'coming',
            'leave',
            'swing',
            'thicket',
            'reserve',
            'murder',
            'costly',
            'corduroy',
            'bump',
            'oncology',
            'swatch',
            'rundown',
            'steal',
            'teller',
            'cable',
            'oily',
            'official',
            'abyss',
            'schism',
            'failing',
            'guru',
            'trim',
            'alfalfa',
            'doubt',
            'booming',
            'bruised',
            'playful',
            'kicker',
            'jockey',
            'handmade',
            'landfall',
            'rhythm',
            'keep',
            'reassure',
            'garland',
            'sauna',
            'idiom',
            'fluent',
            'lope',
            'gland',
            'amend',
            'fashion',
            'treaty',
            'standing',
            'current',
            'sharpen',
            'cinder',
            'idealist',
            'festive',
            'frame',
            'molten',
            'sill',
            'glisten',
            'fearful',
            'basement',
            'minutia']
        self._lives = 5
        self._answer = ""
        self._letters = []
        self._lines = []
        self._lines_count = 1
        self._word = ""

    def word_selector(self):
        """Gets a random word from the list
        Args:
            self (SecretWord): An instance of SecretWord
        """
        self._word = random.choice(self._word_list)
        # print(self._word)

    def draw_lines(self):
        """Makes lines that are the same length as the secret word so the player can know how many letters are in the word
         Args:
            self (SecretWord): An instance of SecretWord
        """
        self._letters = list(self._word)
        for i in self._letters :
            self._lines.append("_")
        for i in range(len(self._letters)):
            print (self._lines[i - 1], end=" ")
        print()

    def guess(self, answer):
        """Method to do check_answer, gets answer parameter from players guess
         Args:
            self (SecretWord): An instance of SecretWord
        """
        print()
        self._answer = answer     

    def check_answer(self):
        """Method to loop through the lists of the word and lines, putting the correctly guessed letter in the list and taking out the corresponding line
         Args:
            self (SecretWord): An instance of SecretWord
        """
        self._lines_count = 0
        answer = False
        for i in range(len(self._letters)):
            if self._letters[i - 1] == self._answer:
                self._lines[i - 1] = self._answer
                answer = True
        for i in range(len(self._letters)):
            print(self._lines[i], end=" ")
            if self._lines[i] == "_":
                self._lines_count += 1
        print()    
        if answer == False:
            self._lives -= 1
            
    def is_alive(self):
        """Method to determine if the jumper is still alive 
        Args:
            self (SecretWord): An instance of SecretWord
        Returns True if jumper has parachute left
        """
        return self._lives > 0 and self._lines_count > 0

