from jumper_parts import jumper_parts

class Jumper:
    
  """The jumpers displays the parachute drawing """
  
  def __init__(self):
    
    self._jumper_parts = jumper_parts
    
      
  def get_parts(self):    
    return self._jumper_parts[0]
    
  def winner(self):
    self._won = (self._jumper_parts[6])   
    return self._won
    
  def lost(self):
    self._lost =  (self._jumper_parts[5])
    return self._lost
 


