import importlib, sys
_mod = importlib.import_module('src.webhook.logger')
sys.modules[__name__] = _mod

