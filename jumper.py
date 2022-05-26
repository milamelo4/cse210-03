from jumper_parts import jumper_parts

class Jumper:
    
  """The jumpers displays the parachute drawing """
  
  def __init__(self):
    
    self._jumper_parts = jumper_parts
  
    
      
  def get_parts(self, lives):    
    
    print(self._jumper_parts[lives])
    
  def winner(self):
    self._won = (self._jumper_parts[6])   
    print(self._won)
    
  def lost(self):
    self._lost =  (self._jumper_parts[5])
    print(self._lost)
 


