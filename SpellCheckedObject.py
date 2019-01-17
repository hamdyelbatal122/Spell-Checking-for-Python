import difflib
from functools import partial
import warnings


class SpellCheckedObject(object):
    def __handler__(self, attr, *args, **kwargs):
        return attr.__call__(*args, **kwargs)

