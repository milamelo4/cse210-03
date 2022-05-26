from jumper_parts import jumper_parts

class Jumper:
    
  """The jumpers displays the parachute drawing """
  
  def __init__(self):
    self._jumper_parts = jumper_parts
      
  def get_parts(self, lives):    
    print(self._jumper_parts[lives])
    
  def winner(self):
    print(self._jumper_parts[6])   
    
  def lost(self):
    print(self._jumper_parts[5])
    
 


