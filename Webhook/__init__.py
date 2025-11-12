"""Lightweight package init with lazy attribute loading to avoid
import-time side effects. Accessing attributes like `Webhook.Pipedream`
will import the backing submodule on demand.
"""
import importlib
from typing import Any

_MAP = {
	'Pipedream': 'pipedream',
	'Definitions': 'dictionaries',
	'Request': 'requests',
	'CSV': 'csv',
	'logger': 'logger',
}

def __getattr__(name: str) -> Any:
	modname = _MAP.get(name)
	if modname:
		mod = importlib.import_module(f"{__name__}.{modname}")
		return getattr(mod, name, mod)
	raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

def __dir__():
	return list(globals().keys()) + list(_MAP.keys())

__all__ = list(_MAP.keys())