import random
import terminal_service

class SecretWord:
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
        self.lives = 6
        self.answer = ""

    def word_selector(self):
        word = random.choice(self._word_list)
        return word

    def draw_lines(self):
        w = self.word_selector()
        res = list(w)
        lines = []
        for i in res :
            lines.append("_")
        for i in range(len(res)):
            print (lines[i - 1], end=" ")

        print()
        return res, lines
    
<<<<<<< Updated upstream:secret_word.py
    def guess(self, answer):
        
        print()
        self.answer = input("guess a letter: ")
=======
    def __guess(self):
        
        print()
        self.answer = input("Guess: ")
>>>>>>> Stashed changes:secrete_word.py
        

    def check_answer(self):
        lists = self.draw_lines()
        letters = lists[0]
        lines = lists[1] 
        lines_count = 1
        
        while self.lives > 0 and lines_count > 0:
            lines_count = 0
            answer = False
            self.guess(answer)
            for i in range(len(letters)):
                
                if letters[i - 1] == self.answer:
                    
                    lines[i - 1] = self.answer
                    answer = True
                
            for i in range(len(letters)):
                
                print(lines[i], end=" ")
                print()
                if lines[i] == "_":
                    lines_count += 1
                
            if answer == False:
                self.lives -= 1
            
                           
        print("The END")    

        
        
    

        




ex = SecretWord()

ex.check_answer()