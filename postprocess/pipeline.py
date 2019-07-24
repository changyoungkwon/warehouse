import importlib.util
from pathlib import Path

class Pipeline:
  
  def __init__(self, functors_dirpath, functors_sequence):
    """Set the directory which includes modules"""
    self.functors = self._get_functors(functors_dirpath, functors_sequence)

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

  def _get_functors(self, functors_dirpath, functors_sequence):
    """Return functors' list for postprocess

    Functors returned by this function is defined in modules in 'functors' folder
    Assume that functor_paths is a list of string formatted "%s(module_name).%s(function_name)" 
    """
    functors = []
    # import module via Path
    for functor_fullname in functors_sequence: 
      module_name, functor_name = functor_fullname.split('.')
      functor_path = Path(functors_dirpath) / Path('{}.py'.format(module_name))
      spec = importlib.util.spec_from_file_location(module_name, str(functor_path))
      module = importlib.util.module_from_spec(spec)
      spec.loader.exec_module(module) 
      functors.append(getattr(module, functor_name))
    return functors