import importlib, sys
_mod = importlib.import_module('src.webhook.requests')
sys.modules[__name__] = _mod

