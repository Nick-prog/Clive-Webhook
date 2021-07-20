from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.py', base=base, target_name = 'Webhook')
]

setup(name='Clive Webhook',
      version = '1.0',
      description = 'Python programmed webhook capturer for Clive forms.',
      options = {'build_exe': build_options},
      executables = executables)
