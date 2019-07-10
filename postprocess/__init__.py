import importlib
from pathlib import Path

class Pipeline:
  
  def __init__(self, functor_paths):
    """Initialize sequence, the order of functors to execute
    
    Sequence is a list of functor_path with an order
    """
    self.functors = self.__get_functors(functor_paths)

  def execute(self, input):
    """Execute each postprocess defined in functors
    
    Return dict {'functor_name':'Succeed or not(boolean)', ...}
    """
    is_functor_succeed = {} 
    for functor in self.functors:
      try:
        functor(input)
        is_functor_succeed[functor.__name__] = True 
      except:
        is_functor_succeed[functor.__name__] = False
        pass
    return is_functor_succeed

  def __get_functors(self, functor_paths):
    """Return functors' list for postprocess

    Functors returned by this function is defined in modules in 'functors' folder
    Assume that functor_paths is a list of string formatted "%s(module_name).%s(function_name)" 
    """
    functors = []
    for functor_path in functor_paths: 
      module_name, functor_name = functor_path.split('.')
      module = importlib.import_module("." + module_name, __name__ + ".functors")
      functors.append(getattr(module, functor_name))
    return functors
