import sys
import warnings

if sys.version_info[0] < 3:
    warnings.warn('нужен третий питон', RuntimeWarning)
else:
    print('все ок')