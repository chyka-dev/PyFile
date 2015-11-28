#-*- coding:utf-8 -*-

""" PyString v1.0
Python 2 & 3 compatible string class.

Usage:
    >>> string = String("hoge") #py2 or 3
    >>> string = String(u"hoge") #py2
    >>> string = String(b"hoge") #py3
"""

import six

class PyString(str):
    """内部でstr->unicode, bytes->str変換する。
    """
    def __new__(cls, value="", encoding="utf-8", *args, **kwargs):
        # str
        if six.PY2 and isinstance(value, str):
            return str.__new__(str, value, *args, **kwargs).decode(encoding)

        if six.PY3 and isinstance(value, str):
            return str.__new__(str, value, *args, **kwargs)

        # PY3 bytes
        if six.PY3 and not isinstance(value, str):
            # encode once, and decode again, 'cause str() doesn't accept bytes
            value = value.decode(encoding)
            return str.__new__(str, value, *args, **kwargs)

        # PY2 unicode 
        # encode once, and decode again, 'cause str() doesn't accept unicode
        value = value.encode(encoding)
        return str.__new__(str, value, *args, **kwargs).decode(encoding)

    def encode(self, *args, **kwargs):
        return super(String, self).encode(*args, **kwargs)

