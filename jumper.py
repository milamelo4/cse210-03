from jumper_parts import jumper_parts

class Jumper:    
  """The jumpers displays the parachute drawing parts
  Attributes:
    _jumper_parts: Gets the jumper's parts from a list.
    """
  
  def __init__(self):
    """Constructs a new Jumper.
    Args: self (Jumper): An instance of Jumper.
    """
    self._jumper_parts = jumper_parts
      
  def get_parts(self, lives):
    """Prints the index of Jumper_parts list
    Args: self (Jumper): An instance of the Jumper
          lives (int): The amount of tries.
          """    
    print(self._jumper_parts[lives])
    
  def winner(self):
    """Prints the jumper part of the winner
    Args: (self): An instance of Jumper.
    """
    print(self._jumper_parts[6])   
    
  def lost(self):
    """Prints the jumper part of the loser
    Args: (self): An instance of Jumper.
    """
    print(self._jumper_parts[5])
    
 


