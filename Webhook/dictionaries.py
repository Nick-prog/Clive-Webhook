import importlib, sys
_mod = importlib.import_module('src.tools.dictionaries')
sys.modules[__name__] = _mod

